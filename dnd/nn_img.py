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
		self.context.model_paths["stable-diffusion"] = "C:\\AI\\web\\project1\\dnd\\models_img\\Deliberate_v3.safetensors"
		self.context.model_paths["lora"] = "C:\\AI\\web\\project1\\dnd\\models_img\\delib_6_8_f_m.safetensors"
		load_model(self.context, "stable-diffusion")
		load_model(self.context, "lora")
	
	def generate_image(self, prompt,  guidance_scale, seed, width, height, lora_alpha):
		images = generate_images(self.context, prompt=prompt, guidance_scale=guidance_scale, sampler_name="dpmpp_2m", seed=seed, width=width, height=height, lora_alpha=lora_alpha)
		name = "image"+str(time.strftime('%X')).replace(':','-')+".png"
		path = "./static/nn/" + name
		im1 = images[0].save(path) 
		return path

# im = self.model.generate_image(prompt, seed, width, height, lora_alpha)
# m = Model()
