import random

def random_name_gen():
    first_name = ""
    visemes = ["p","b","m","f","v","th","t","d","k","g","ch","s","n","l","r","a","e","ih","oh","ou"]
    
    for i in range(0,5):
        first_name += visemes[random.randint(0,len(visemes)-1)]
    return first_name