a = "パトカー"
b = "タクシー"
# d = "猫てゃん"
c = ""
for police, taxi in zip(a, b):
  c += police + taxi

print(c)