from PIL import Image

bakgrunn = Image.open("referanse.jpg")
layer = Image.open("filter.png")

bakgrunn.paste(layer, (0, 0), layer)
bakgrunn.save("resultat.png")
