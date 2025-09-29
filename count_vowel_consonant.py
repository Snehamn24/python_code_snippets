str = "Mathematics"

vowels = ['a','e','i','o','u']

str = str.lower()

vowels_count = 0
consonant_count = 0

for ch in str:
    if ch.isalpha():
        if ch in vowels:
            vowels_count+=1
        else:
            consonant_count+=1

print(f"Number of Vowels : {vowels_count}")

print(f"Number of Consonants: {consonant_count}")