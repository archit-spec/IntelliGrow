from openai import OpenAI
import praw
import google.generativeai as genai 
import os
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = api_key
)

completion = client.chat.completions.create(
  model="nvidia/nemotron-4-340b-instruct",
  messages=[{"role":"user","content":"imagine you are sales person im going to create an imaginary conversation you have to promote a dumball toy on dumball.in here is the convo:\nTitle: im huge dumball fan looking for some dumball collectiblesSelftext: please helop me find i m ready to pay 20 million$ for them  || Comment by xoD3M0Nox: I got some dumball collectibles in my pants buckoComment by NaukarNirala: i have some\nyour reply should be  just reply what an enthusiast would say dont make it seem fake"}],
  temperature=0.2,
  top_p=0.7,
  max_tokens=1024,
  stream=True
)
a= ""
for chunk in completion:
  if chunk.choices[0].delta.content is not None:
    a = a + chunk.choices[0].delta.content    
    print(chunk.choices[0].delta.content, end="")

response_text = completion
reddit = praw.Reddit(
    client_id=client_id,  # This is your personal use script
    client_secret=client_secret,  # This is your secret
    password="tammu@123",  # Replace with the password for your Reddit account
    user_agent="python:my_reddit_app:v1.0 (by u/Best_Camel_7084)",  # This is your user agent
    username="Best_Camel_7084",  # This is your Reddit username
)

submission_id = "1d5q3d8"  # Replace with the actual submission ID
submission = reddit.submission(id=submission_id)

# Alternatively, if you want to reply to a specific comment
comment_id = "l6n3zh6"  # Replace with the actual comment ID
comment = reddit.comment(id=comment_id)

# Reply to the submission

# Reply to the comment
comment.reply(a)
