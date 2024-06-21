from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

class TextModel():
	def __init__(self):
		self.model_name_or_path = "TheBloke/CAMEL-13B-Role-Playing-Data-GPTQ"
		self.model = AutoModelForCausalLM.from_pretrained(self.model_name_or_path,
													 device_map="auto",
													 trust_remote_code=True,
													 revision="main")

		self.tokenizer = AutoTokenizer.from_pretrained(self.model_name_or_path, use_fast=True)

		prompt = "Let's play role-play game D&D. You are my master. My character is 28 y.o. tiefling called Luke. Tell me about my friends and start the adventure."

		self.first_try = True
		self.setting = ''


	def brush_text(self, text):
		# answer = self.tokenizer.decode(output[0])
		answer1 = text[text.find('### Response:')+13::]

		if answer1.find('Next request') != -1:
			answer1 = answer1[:answer1.find('Next request'):]

		if answer1.find('</s>') != -1:
			answer1 = answer1[:answer1.find('</s>'):]

		if answer1.find('### End') != -1:
			answer1 = answer1[:answer1.find('### End'):]

		answer1 = answer1 + '...'

		return answer1

	def generate_text(self, first_try=True, prompt="My character is 28 y.o. tiefling called Luke. Tell me about my friends and start the adventure.", temperature=0.7, do_sample=True, top_p=0.95, top_k=40, max_new_tokens=512):
		if first_try:
			self.prompt_template=f'''You are playing a role of Dungeons and Dragons master. Make a story based on the character mentioned below.
### Instruction:
{prompt}
### Response:

'''
			first_try = False
		else:
			self.prompt_template=f'''You are playing a role of Dungeons and Dragons master. Take into account our previous dialogue and continue writing a story.
### Instruction:
{prompt}
### Response:

'''
		input_ids = self.tokenizer(self.prompt_template, return_tensors='pt').input_ids.cuda()
		output = self.model.generate(inputs=input_ids, temperature=temperature, do_sample=do_sample, top_p=top_p, top_k=top_k, max_new_tokens=max_new_tokens)
		print(self.tokenizer.decode(output[0]))

		res = self.brush_text(self.tokenizer.decode(output[0]))

		return res



# model = TextModel()
# prompt = "My character is 28 y.o. tiefling called Luke. Tell me about my friends and start the adventure."

# while True:
# 	prompt = input()
# 	model.generate_text(prompt)
# 	