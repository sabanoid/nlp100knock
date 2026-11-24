import random


def typoglycemia(text):
    words = text.split()
    result = []
    
    for word in words:
        if len(word) <= 4:
            result.append(word)
        else:
            first = word[0]
            middle = list(word[1:-1])
            last = word[-1]
            
            random.shuffle(middle)
            
            new_word = first + "".join(middle) + last
            result.append(new_word)
            
    return " ".join(result)


sentence = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

output = typoglycemia(sentence)
print(output)