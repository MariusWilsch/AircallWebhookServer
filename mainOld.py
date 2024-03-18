# from flask import Flask, request, jsonify
# from google.cloud import storage
# import json, requests

# app = Flask(__name__)


# @app.route("/")
# def index():
#     return "Hello, World!"


# @app.route("/aircall/webhook", methods=["POST"])
# def handle_webhook():
#     data = request.json

#     # For demonstration purposes
#     print(json.dumps(data, indent=2))
#     # Process the data asynchronously here
#     # not implemented yet

#     recording_url = data.get("recording")

#     # Download the file
#     response = requests.get(recording_url)

#     if response.status_code != 200:
#         return jsonify(success=False), 200

#     file_name = recording_url.split("/")[-1].split("?")[0]

#     # Initialize a Cloud Storage client
#     storage_client = storage.Client()

#     # Get the bucket in Cloud Storage
#     bucket = storage_client.bucket("aircall-recordings")

#     # Upload the file to the bucket
#     bucket.blob(f"recordings/{file_name}").upload_from_string(response.content)

#     # Create a new blob and upload the file

#     return jsonify(success=True), 200


# if __name__ == "__main__":
#     app.run(port=500)


# # @app.route("/aircall/webhook", methods=["POST"])
# # def handle_webhook():
# #     data = request.json

# #     # For demonstration purposes
# #     print(json.dumps(data, indent=2))
# #     # Process the data asynchronously here
# #     # not implemented yet

# #     recording_url = data.get("recording")

# #     # Download the file
# #     response = requests.get(recording_url)

# #     if response.status_code != 200:
# #         return jsonify(success=False), 200

# #     file_name = recording_url.split("/")[-1].split("?")[0]

# #     # Initialize a Cloud Storage client
# #     storage_client = storage.Client()

# #     # Get the bucket in Cloud Storage
# #     bucket = storage_client.bucket("aircall-recordings")

# #     # Upload the file to the bucket
# #     bucket.blob(f"recordings/{file_name}").upload_from_string(response.content)

# #     # Create a new blob and upload the file

# #     return jsonify(success=True), 200
