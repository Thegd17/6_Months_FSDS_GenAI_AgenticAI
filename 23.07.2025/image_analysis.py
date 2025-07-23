import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import requests
from io import BytesIO # bytes io is used for buffer memory to store or capture images

def load_image_url(url):
    response = requests.get(url)
    return Image.open(BytesIO(response.content))


elephant_url = "https://upload.wikimedia.org/wikipedia/commons/3/37/African_Bush_Elephant.jpg"
feather_url = "https://m.media-amazon.com/images/I/81JSw5mE54L._UF894,1000_QL80_.jpg"
elephant = load_image_url(elephant_url)
feather = load_image_url(feather_url)

plt.figure(figsize=(6,4))
plt.imshow(elephant)
plt.title("Elephant")
plt.axis('off')
plt.show()

plt.figure(figsize=(6,4))
plt.imshow(feather)
plt.title("Feather")
plt.axis('off')
plt.show()
