import random

d = {
    "Management" : 22.0,
    "Business" : 31.6,
    "Legal" : 1.4,
    "Arts" : 44.9
}

def randOcc(dict):
    perc = random.random() * 100;
    for key,val in dict.iteritems():
        perc -= val
        if perc <= 0:
            return key
    return "Unoccupied"

print(randOcc(d))
        
