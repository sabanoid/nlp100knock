def make_sentence(x, y, z):
    text = str(x) + "時の" + str(y) + "は" + str(z)
    return text

result = make_sentence(12, "気温", 22.4)

print(result)