import time

meme_dict = {
            "CRINGE"  : "Something embarrasing",
            "LOL"     : "Something funny",
            "ROFL"    : "Something very funny",
            "SHEESH"  : "Not 100% agree",
            "CREEPY"  : "Scary",
            "AGGRO"   : "Mad, Aggressive",
            "LMAO"    : "Something funny",
            "RIZZ"    : "The ability to pull boys/girls",
            "AI-SLOP" : "AI Vidoes with low-quality effort",
            "RAGEBAIT": "Making someone angry",
            "DELULU"  : "Short for delusional",
            "LOWKEY"  : "Kind of",
            "DRIP"    : "God Clothings/Accessories",
            "BRO"     : "Brother, Man",
            "FAM"     : "Brother, Man",
            "67"      : "The Holy Number"
            }

print("Welcome to the Big 25 Dictionaries.")

while True:
    time.sleep(1)
    word = input("\nType the word you want to learn!")

    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("What?")
