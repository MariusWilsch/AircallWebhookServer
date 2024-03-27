import os
import assemblyai as aai
from assemblyai import TranscriptError
from upload_to_gcp import upload_transcription_to_cloud_storage


def transcribe_with_AAI(recording_url, id):
    aai.settings.api_key = os.getenv("AAI_API_KEY")
    aai.settings.polling_interval = 2
    transcriber = aai.Transcriber(
        config=aai.TranscriptionConfig(
            speaker_labels=True,
            language_code="de",
            punctuate=True,
            content_safety=False,
        )
    )
    try:
        transcript = transcriber.transcribe(data=recording_url)
    except TranscriptError as e:
        print(f"An error occurred during transcription: {e}")
        return None
    utterances_whole = "\n".join(
        [f"{u.speaker}: {u.text}" for u in transcript.utterances]
    )
    upload_transcription_to_cloud_storage(transcript, file_name=id)
    print(utterances_whole)
    return utterances_whole
