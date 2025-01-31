import random

def random_name_gen():
    first_name = ""
    visemes = ["p","b","m","f","v","th","t","d","k","g","ch","s","n","l","r","a","e","ih","oh","ou"]
    
    for i in range(0,5):
        first_name += visemes[random.randint(0,len(visemes)-1)]
    return first_name

def calc_expected_value(out_a_value,out_a_prob,out_b_value,out_b_prob):
    return (out_a_value * out_a_prob) + (out_b_value * out_b_prob)


'''
outcome,        wins    loses
value,          500     -100
probability     20%     80%

ev = 500(.20) + -100(.80)
ev = 100 + -80
ev = 20

w/ 3 players in a race, the default % of winning is 33
'''