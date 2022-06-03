import ctypes
import wikipedia as wiki
word = input("who is you searching? ")
info = wiki.summary(word)
ctypes.windll.user32.MessageBoxW(
    0, info[:400], word, 0
)
