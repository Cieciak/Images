import numpy as np
from PIL import Image

image = Image.open('Oropo.png').convert('LA')
image = np.array(image)
image = image[:,:,0]
image = np.round((image / 256) * 4)
out = ''
for i in range(128):
    for j in range(128):
        if image[i, j] == 0:
            out += '█'
        elif image[i, j] == 1:
            out += '▓'
        elif image[i, j] == 2:
            out += '▒'
        elif image[i, j] == 3:
            out += '░'
        else:
            out += ' '
    out += '\n'

with open('dump.txt', 'w', encoding='UTF-8') as file:
    file.write(out)