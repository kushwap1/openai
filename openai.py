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
	response = openai.Completion.create(
		engine="text-davinci-003",
		prompt=log_file_contents,
		temperature=0.9,
		max_tokens=150,
		top_p=1,
		frequency_penality=0,
		presence_penalty=0)

	return response

log_file_contents = parse_log_file(sys.argv[1])

response = generate_summary(log_file_contents)

print(response['choices'][0]['text'])
