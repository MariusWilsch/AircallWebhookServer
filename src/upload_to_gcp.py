import json, requests
from google.cloud import storage

# GCP Client
client = storage.Client()
bucket = client.get_bucket("aircall_recordings")


def upload_summary_to_cloud_storage(summary, file_name):
    try:
        blob = bucket.blob(f"summaries/{file_name}")
        blob.upload_from_string(summary, content_type="text/plain; charset=utf-8")
        print(f"Summary uploaded to cloud storage: {blob.public_url}")
    except Exception as e:
        print(f"An error occurred during cloud storage upload: {e}")


def upload_transcription_to_cloud_storage(transcription, file_name):
    try:
        blob = bucket.blob(f"transcriptions/{file_name}")
        json_transcription = json.dumps(transcription, indent=2)
        blob.upload_from_string(json_transcription, content_type="application/json")
        print(f"Transcription uploaded to cloud storage: {blob.public_url}")
    except Exception as e:
        print(f"An error occurred during cloud storage upload: {e}")


def upload_recording_to_cloud_storage(recording_url: str, id: str):
    response = requests.get(recording_url)
    if response.status_code != 200:
        print("Failed to download recording.")
        return False
    print("Recording downloaded successfully.")
    try:
        blob = bucket.blob(f"recordings/{id}.mp3")
        blob.upload_from_string(response.content, content_type="audio/mpeg")
        print(f"Recording uploaded to cloud storage: {blob.public_url}")
    except Exception as e:
        print(f"An error occurred during cloud storage upload: {e}")
    return True
