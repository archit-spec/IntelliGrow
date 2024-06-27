import praw
import google.generativeai as genai 
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192

}

#read json 

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

reddit = praw.Reddit(
    client_id=client_id,  # This is your personal use script
    client_secret=client_secret,  # This is your secret
    password="tammu@123",  # Replace with the password for your Reddit account
    user_agent="python:my_reddit_app:v1.0 (by u/Best_Camel_7084)",  # This is your user agent
    username="Best_Camel_7084",  # This is your Reddit username
)

# Replace 'submission_id' with the ID of the submission you want to read
submission_id = "1d5q3d8"
submission = reddit.submission(id=submission_id)
print(submission.)
# Print the title and selftext of the submission
print(f"Title: {submission.title}")
print(f"Selftext: {submission.selftext}")

# Expand the comment tree
submission.comments.replace_more(limit=None)

# Print all comments and their replies
for comment in submission.comments.list():
    print(f"Comment by {comment.author}: {comment.body}")
    for reply in comment.replies:
        print(f"  Reply by {reply.author}: {reply.body}")
