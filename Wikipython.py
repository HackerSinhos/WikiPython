import ctypes
import wikipedia as wiki

word = input("Who are you searching? ")

try:
    info = wiki.summary(word)
    ctypes.windll.user32.MessageBoxW(
        0, info[:400], word, 0
    )
except wiki.exceptions.DisambiguationError:
    ctypes.windll.user32.MessageBoxW(
        0, "The word provided does not match any Wikipedia page!", "Error", 0
    )
