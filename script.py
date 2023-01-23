import time
import pywhatkit
import openai
import schedule
import random

responses = []
prompts = ['A sweet good night message for family',
           'a sweet good night message for family and fill it with emojis', 'A sweet good night message for family. Fill the message with appropriate emojis', 'A sweet good night message for family with emojis']
# you can change the prompts. These are sample prompts for better results.


def message():
    for text in prompts:
        # Define OpenAI API key
        openai.api_key = ""  # Enter your OpenAI API key between the quotation marks

        # Set up the model and prompt
        model_engine = "text-davinci-003"
        prompt = text

        # Generate a response
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        response = completion.choices[0].text
        responses.append(response)

    print(responses)  # For testing purposes

    pywhatkit.sendwhatmsg_instantly(
        "Enter the receiver's phone number here", random.choice(responses), 20, True, 10)


def job():
    message()
    return


# schedule.every(2).minutes.do(job)  # use this only for testing purposes as sending messages at 2 min interval for too long may get you banned.
schedule.every().day.at("Enter time here in in 24 hr format HH:MM").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)  # wait one minute
