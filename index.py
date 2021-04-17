import numpy as np
from PIL import Image

while True:
    image_link = input('Image >>')
    if image_link == 'quit': quit()
    text_file = image_link.split('.')[0] + '.txt'
    image = Image.open(image_link).convert('LA')
    width, height = image.size
    image = np.array(image)
    image = image[:,:,0]
    image = np.round((image / 256) * 4)
    out = ''
    for i in range(height):
        for j in range(width):
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

    with open(text_file, 'w', encoding='UTF-8') as file:
        file.write(out)