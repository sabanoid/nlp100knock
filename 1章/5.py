def make_ngram(sequence, n):
    result = []
    
    count = len(sequence) - n + 1
    
    for i in range(count):
        part = sequence[i:i + n]
        result.append(part)
        
    return result


text = "I am an NLPer"

char_trigram = make_ngram(text, 3)

words = text.split()
word_bigram = make_ngram(words, 2)

print("tri-gram:", char_trigram)
print("bi-gram:", word_bigram)