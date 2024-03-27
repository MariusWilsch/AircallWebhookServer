import requests, threading, uuid, traceback, time, os
from flask import Flask, request, jsonify
from openai import OpenAI
from pprint import pprint
from dotenv import load_dotenv

# Helper functions
from upload_to_gcp import (
    upload_recording_to_cloud_storage,
)
from src.send_mail import send_mail
from src.transcribe import transcribe_with_AAI
from src.get_summary import summary_workflow

# Load the environment variables
load_dotenv()

# Initialize the Flask app
app = Flask(__name__)


# Define the home route
@app.route("/")
def home():
    return "<h1 style='text-align: center;'>Aircall Webhook Server is Running</h1>"


transcription_in_progress = {}


@app.route("/aircall/webhook", methods=["POST"])
def handle_webhook():
    data = request.json
    return_val = jsonify(success=True), 200

    # Validate the webhook request
    recording_url = data["data"].get("recording", None)
    if not validate_webhook(data, recording_url):
        return return_val
    # Mark the recording with recording_url as key as being transcribed
    transcription_in_progress[recording_url] = True
    # Upload the recording to the cloud storage
    id = str(uuid.uuid4())
    if not upload_recording_to_cloud_storage(recording_url=recording_url, file_name=id):
        return return_val
    # Start a new thread to transcribe the audio
    threading.Thread(target=startWorkflow, args=(recording_url, id)).start()
    # Return a success response
    return return_val


def validate_webhook(data, recording_url):
    if data["event"] != "call.ended":
        print("Event is not 'call.ended'. Skipping webhook processing.")
        return False

    if not recording_url:
        print("No recording URL found for this event.")
        return False

    if recording_url in transcription_in_progress:
        print("This recording is already being transcribed.")
        return False
    return True


def startWorkflow(recording_url, id):
    try:
        # Transcribe the audio using AssemblyAI
        transcript = transcribe_with_AAI(recording_url, id)
        del transcription_in_progress[recording_url]
        if transcript is None:
            print("Transcription failed.")
            return
        # Generate a summary of the transcription
        summary = summary_workflow(transcript, id)
        if summary is None:
            print("Summary generation failed.")
            return
        # Send the summary to the email
        send_mail(summary)
    except Exception as e:
        print(f"An error occurred during the workflow: {e}")
        traceback.print_exc()


if __name__ == "__main__":
    app.run(port=5000)
