#!/usr/bin/python3
"""fuctio for debofuscate img"""
from PIL import Image


def desofuscar(i_fil, limite=10):
    img = Image.open(i_fil)
    img = img.convert('RGB')
    pixeles = img.load()

    for x in range(img.size[0]):
        for y in range(img.size[1]):
            if (pixeles[x, y][0] < limite) \
                    and (pixeles[x, y][1] < limite) \
                    and (pixeles[x, y][2] < limite):
                pixeles[x, y] = (0x80, 0x80, 0x80, 255)

    img.show()
    img.save('desofuscar.png')
