from PIL import Image
import numpy as np

pictures = ['lunar01_raw.jpg', 'lunar02_raw.jpg', 'lunar03_raw.jpg']

for pic in pictures:
    img = Image.open(pic)
    data = np.array(img)

    min_val = np.min(data)
    max_val = np.max(data)

    new_pixels = ((data - min_val) * (255.0 / (max_val - min_val))).astype(np.uint8)

    new_name = pic.replace('.', '_better.')
    Image.fromarray(new_pixels).save(new_name)
