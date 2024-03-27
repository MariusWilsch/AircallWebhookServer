import os, traceback, time
from openai import OpenAI
from src.upload_to_gcp import upload_summary_to_cloud_storage

systemprompt = """
    You have the task to summarise a call between Ulrich Wilsch and his client. The call should be reported in actionable points and conclusions made in the call.

    It should satisfy certain conditions:

    1. Filter out the small talk

    2. Mr. Wilsch has 2 business. 1 related to Morocco and 1 related to deals with IBM Power I, IBM iSeries, AS400, technical documentation, descriptions of services, software maintenance, and hardware maintenance, if something falls outside these 2 categories put it under Wilsch GmbH. (Wilsch GmbH(. You have to make a SEPARATION between these two when creating the report.

    3. Unlike the discussions on Morocco, conversations regarding Wilsch GmbH & CoKG should not be condensed but rather described in detail, highlighting the technical aspects and services offered by the company.

    4. Output should always be written in German even if transcript is in English.

    5. Output is in bullet point format and each line is written extremely condensed. You must create separate headlines for Morocco and Wilsch GmbH & CoKG sales talk.

    6. If the caller proposes a different time to call due to various reasons please include that as an action point.

    7. If there are no relevant points to be made, please write "No relevant points to be made" in german in addition to the bullet points.

"""

# Open AI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Optional settings
# seed = 1
# tempature = 0.5


def summary_workflow(transcript: str, id: str) -> str:
    """
    This function starts the workflow for generating a summary of the transcription.

    Parameters:
      transcript (str): The transcription to be summarised.
      id (str): The ID of the transcription.

    Returns:
      str: The summary of the transcription.
    """
    # Get the summary from GPT-3.5
    summary = gpt_judge_content(transcript)

    # Upload the summary to cloud storage
    if summary is not None:
        upload_summary_to_cloud_storage(summary=summary, file_name=id)

    return summary


def gpt_judge_content(content) -> str:
    """
    This function uses the OpenAI GPT API to generate a summary of the transcription.

    Parameters:
      content (str): The content to be summarised.
      systemprompt (str): The system prompt to be used for the GPT API.

    Returns:
      str: The summary of the content.
    """

    max_tries = 3
    for attempts in range(max_tries):
        try:
            response = client.chat.completions.create(
                model="gpt-4-0125-preview",
                messages=[
                    {"role": "system", "content": systemprompt},
                    {"role": "user", "content": content},
                ],
                temperature=0.5,
            )
            print("Summary: ", response.choices[0].message.content)
            return response.choices[0].message.content
        except Exception as e:
            print(f"An error occurred: {e}")
            traceback.print_exc()

            if attempts < max_tries - 1:  # Don't sleep for the last attempt
                time.sleep(3)
            else:
                print("Max retries reached. Giving up.")
                return None
