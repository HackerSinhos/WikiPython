import wikipedia as wiki
word = input("What are you searching? ")

try:
    info = wiki.summary(word)
    print(info)
except wiki.exceptions.DisambiguationError:
    print("The word provided does not match any Wikipedia page!")
