def sort_words(words):
    return  '   '.join(sorted(words.split(), key= str.casefold))

print(sort_words("I am leveling up my python skills"))