import numpy as np
# doc string

def calc_spread(odds_list):
    num_odds = len(odds_list)
    inverse_odds_list = [1/x for x in odds_list]
    spread = round((1/sum(inverse_odds_list))-1,5)
    return spread 

def calc_probs(odds_list):
    num_odds = len(odds_list)
    spread = calc_spread(odds_list)
    probs = [(spread + 1)/x for x in odds_list]
    return probs

def calc_break_even(odds_list):
    inverse_odds_list = [1/x for x in odds_list]
    break_even_odd = 1/(1-sum(inverse_odds_list))
    return break_even_odd

x = [11, 9.5, 12, 22, 50, 120,	250,
12,	6.7,	8.5,	15,	40,	120,	250,
19,	12,	12,	23,	70,	200,	250,
45,	25,	28,	60,	150,	250,	250,
120,	80,	100,	150,	250,	250,	250,
250,	200,	250,	250,	250,	250,	250,
250,	250,	250, 250,	250,	250,	250]

x = [3.2, 3.4, 2.25]

probs = calc_probs(x)
print(probs)


spread = calc_spread(x)
print(spread)
