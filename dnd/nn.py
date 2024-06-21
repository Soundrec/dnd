import sdkit
from sdkit.generate import generate_images
from sdkit.models import load_model
from sdkit.utils import log, save_images
import time
import random

from PIL import Image  
import PIL 

class Model():
	def __init__(self):
		self.context = sdkit.Context()
		self.context.model_paths["lora"] = "C:\\AI\\models_res\\dnd.safetensors"
		self.context.model_paths["stable-diffusion"] = "C:/AI/LoRA/models/Deliberate_v2.safetensors"
		load_model(self.context, "stable-diffusion")
		load_model(self.context, "lora")
		print('d')
		print(self.context.read())
		print(self.context.watch())
	
	def generate_image(self, prompt, seed, width, height, lora_alpha):
		images = generate_images(self.context, prompt=prompt, seed=seed, width=width, height=height, lora_alpha=lora_alpha)
		name = "image"+str(time.strftime('%X')).replace(':','-')+".png"
		path = "./static/nn/" + name
		im1 = images[0].save(path) 
		return path
