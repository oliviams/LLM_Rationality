import openai
import time
from prompts import *
import pandas as pd

# Insert your OpenAI API key here
openai.api_key = 'YOUR-API-KEY'


def request(task):
    """ChatGPT prompter"""
    response = openai.ChatCompletion.create(
        model="gpt-4", #gpt-3.5-turbo
        messages=[
            {"role": "user", "content": task}])
    answer = response['choices'][0]['message']['content']
    return answer


all_tasks = []
for prompt in prompts:
    task = []
    for i in range(10):
        time.sleep(40)
        task.append(request(prompt))
    all_tasks.append(task)

df = pd.DataFrame(all_tasks)
df = df.set_axis(['Wason Classic', 'Wason Context', 'AIDS Classic', 'AIDS Freq', 'Hospital',
                  'Monty Short', 'Monty Long', 'Linda Classic', 'Births Random', 'Births Ordered',
                  'High School', 'Psych Experiment', 'Marbles'])

df.to_csv('GPT_4_rationality_tasks.csv')
