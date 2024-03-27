def transcribe_audio(recording_url, id):
    settings = ConnectionSettings(
        url="https://asr.api.speechmatics.com/v2",
        auth_token=os.getenv("SPEECHMATICS_API_KEY"),
    )
    conf = {
        "type": "transcription",
        "transcription_config": {
            "language": "de",
            "enable_entities": True,
            "diarization": "speaker",
            "operating_point": "enhanced",
        },
        "fetch_data": {"url": recording_url},
    }
    max_tries = 3
    for attempt in range(max_tries):
        with BatchClient(settings) as client:
            try:
                # Since we're providing a URL via fetch_data, audio parameter is set to None
                job_id = client.submit_job(audio=None, transcription_config=conf)
                print(f"Job {job_id} submitted successfully, waiting for transcript")

                transcript = client.wait_for_completion(
                    job_id, transcription_format="txt"
                )

                del transcription_in_progress[recording_url]
                print(transcript)

                start_summary(transcript, id)
                upload_transcription_to_cloud_storage(transcript, file_name=id)
                return

            except Exception as e:
                print(f"An unexpected error occurred: {e}", job_id)
                job_response = client.check_job_status(job_id)
                pprint(job_response, indent=2)
                traceback.print_exc()

                if attempt < max_tries - 1:  # Don't sleep for the last attempt
                    time.sleep(3)  # Wait for 10 seconds before retrying
                else:
                    print("Max retries reached. Giving up.")
