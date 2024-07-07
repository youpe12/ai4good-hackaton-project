# -*- coding: utf-8 -*-

#chat completion: make conversation with chatgpt and complete the conversation.
#openai.api_key = "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"

from openai import OpenAI
client = OpenAI(
    api_key= "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"
)

messages = []
messages.append({"role": "system", "content": "You are a teaching assistant, and you have to check whether students are understanding well about the class material."})
messages.append({"role": "system", "content": "Keep in mind that students are middle-aged and they need encouragement."})
messages.append({"role": "system", "content": "Use Korean."})

first_answer = client.chat.completions.create(model="gpt-3.5-turbo",messages = messages)
first_content = first_answer.choices[0].message.content.strip()
messages.append({"role" : "assistant", "content" : f"{first_content}"})
print(f"GPT : {first_content}")

while True:
  user_content = input("user: ")

  messages.append({"role" : "user", "content" : f"{user_content}"})

  completion = client.chat.completions.create(model="gpt-3.5-turbo",messages = messages)

  assistant_content = completion.choices[0].message.content.strip()

  messages.append({"role" : "assistant", "content" : f"{assistant_content}"})

  print(f"GPT : {assistant_content}")
