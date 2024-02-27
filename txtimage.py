from transformers import pipeline
from diffusers import StableDiffusionPipeline
from PIL import Image
import PIL
model_id = "stabilityai/stable-diffusion-2"
pipe = StableDiffusionPipeline.from_pretrained(model_id)
def generate_image(prompt):
  image = pipe(prompt)
  return image.images[0]
text = input("Enter your text prompt: ")
generated_image = generate_image(text)

# Display or save the generated image
# ...
generated_image.save("image.png")