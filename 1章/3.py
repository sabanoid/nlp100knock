from re import split
pie = []
str_pie = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
list_pie = str_pie.split()
for i in list_pie:
  pie.append(len(i))
print(pie)