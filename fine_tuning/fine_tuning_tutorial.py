import time
from openai import OpenAI
import os
import openai

os.environ["OPENAI_API_KEY"] = "API_KEY"
print(os.environ.get("OPENAI_API_KEY"))
client = OpenAI(api_key="API_KEY")
file_response = openai.files.create(
    file = open("prompt01.jsonl", "rb"),
    purpose = 'fine-tune'
)
# openai.files.list()  # check the uploaded file id
# Get the file ID
file_id = file_response['id']

# Check the file's status
status = file_response['status']
while status != 'processed':
    print(f"File status: {status}. Waiting for the file to be processed...")
    time.sleep(10)  # Wait for 10 seconds
    file_response = openai.File.retrieve(file_id)
    status = file_response['status']

# Create the fine-tuning job using the file ID
if status == 'processed':
    fine_tuning_response = openai.FineTuningJob.create(
      training_file=file_id,
      model="gpt-3.5-turbo"
    )
    fine_tuning_job_id = fine_tuning_response['id'] # Store the fine-tuning job ID
else:
    print(f"File processing failed with status: {status}")

# openai.FineTuningJob.create(training_file="file_id", model="gpt-3.5-turbo")  # fine-tuning process
# openai.FineTuningJob.cancel(training_file="file_id")  # terminate fine-tuning process

# # fine-tuning을 완료한 모델에 inference를 진행
# completion = openai.ChatCompletion.create(
#     model = "ft:gpt-3.5-turbo:my-org:custom_suffix:id", 
#     messages=[
#         {"role":"system", "content": "Jay is a kind teaching assistant chatbot that speaks in Korean."},
#         {"role":"user", "content": "뜨개질 유튜버를 추천해줄래?"}
#     ]
# )
# print(completion.choices[0].message)
