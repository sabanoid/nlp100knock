a = "パトカー"
b = "タクシー"
c = ""
for police, taxi in zip(a, b):
  c += police + taxi

print(c)