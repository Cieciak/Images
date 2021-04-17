import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

image = Image.open('Numbers.png').convert('LA')
image = np.array(image)[:,:,0]
numbers = np.split(image, (10, 12))
print(len(numbers))
plt.matshow(numbers, cmap = 'gray')
plt.show()