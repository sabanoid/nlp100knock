def make_sentence(x, y, z):
    text = str(x) + "時の" + str(y) + "は" + str(z)
    return text

x = 12
y = "気温"
z = 22.4

result = make_sentence(x, y, z)

print(result)