import json
from difflib import get_close_matches
data=json.load(open("dict.json"))
def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys()))>0:
        yn=input("Did you mean %s instead?Enter Y if yes else N is No:"%get_close_matches(w,data.keys())[0])
        yn=yn.lower()
        if yn=="y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn=="n":
            return "The word doesn't exist.Please double check it"
        else:
            return "We didi not understand your entry"

    else:
        return "The word doesn't exist.Please double check it"
word=input("Enter the word")
output=translate(word)
if type(output)==list:
    for item in output:
        print(item)
else:
        print(output)
input("Press ENTER to exit")
