#Jennifer Jenkins
#Write a function readcurrency(filename)
#that takes a filename as its argument.
#This function reads the lines of a file, which are of the form
#USD 1.141911 Where the first value is a currency and the second value is the
#Euro's value in that currency.
#Return a list of dictionaries from this data, with each
#line of the file corresponding to an element in the dictionary.
import json

def readcurrency(filename):
    currency_list = []
    with open(filename, 'r') as fh:
        all_lines = fh.readlines()
    for line in all_lines:
        symbol, rate = line.split()
        currency_list.append({"symbol":symbol, "rate":float(rate)})
    return currency_list

def save(json_filename, data):
    with open(json_filename, 'w') as fh:
        json.dump(data, fh, indent=4)
        

        
print(readcurrency("currency.txt"))
save('currency.json', readcurrency("currency.txt"))



