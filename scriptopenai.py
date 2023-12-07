#! /usr/bin/python

import os 
import sys
import openai

def parse_log_file(log_file):
	with open(log_file, 'r') as f:
		log_file_contents = f.read()
	return log_file_contents

def generate_summary(log_file_contents):
	openai.api_key = os.environ.get('OPENAI_SECRET_KEY')
	response = openai.completions.create(
		model="text-davinci-003",
		prompt="As a code reviewer, create summary for this log. Use markdown formatting for better readability." + log_file_contents,
		temperature=0.7,
		max_tokens=1024,
		top_p=1
		)

	return response

log_file_contents = parse_log_file(sys.argv[1])

response = generate_summary(log_file_contents)

# print(response['choices'][0]['text'])
print(response.choices[0].text)

with open('summary.txt', 'w') as f:
	f.write(response.choices[0].text)
	f.close()

