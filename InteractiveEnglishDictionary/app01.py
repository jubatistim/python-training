import json
from difflib import get_close_matches

data = json.load(open(r"data\data.json"))

def translate(word):    
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        word = word.lower()
        if word in data:
            return data[word]
        elif len(get_close_matches(word, data.keys())) > 0:
            yn = input("The word doesn't exist. Did yo mean %s instead? Y for yes and N for no: " % get_close_matches(word, data.keys())[0])
            if yn == "Y":
                return translate(get_close_matches(word, data.keys())[0])
            elif yn == "N":
                return "The word doesn't exist. Please double check it!"
            else:
                return "We didn't understand your entry."
        else:
            return "The word doesn't exist. Please double check it!"

while True:    
    word = input("Enter a word (!ex to exit): ")

    if word.lower() == "!ex":
        break

    output = translate(word)

    if isinstance(output, str):
        print (output)
    else:
        for o in output:
            print(o)