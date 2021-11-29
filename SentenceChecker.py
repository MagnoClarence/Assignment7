# Program 1:
# Create a program that ask for a sentence as input.
# Display the number of words, vowels and consonants in the input 
# ex.
# input: Bahala kayo dyan
# output: - words: 3 - vowels: 6 - consonants: 8

sentence = input("Enter a sentence: ")
wordLength = sentence.split()

vowels = "aeiouAEIOU"
vowelCounter = 0
consonantCounter = 0
numberCounter = 0
for x in wordLength:
    for y in x:
        if y in vowels:
            vowelCounter += 1
        else:
            consonantCounter += 1

        
print(f"words: {len(wordLength)} \nvowels: {vowelCounter} \nconsonants: {consonantCounter}\n")