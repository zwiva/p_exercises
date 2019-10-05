from sys import argv
price = float(argv[1])
prem_user = float(argv[2])
free_user = float(argv[3])
spents = float(argv[4])
profit = ((2 * price * prem_user) + (free_user * 0)) - spents
if profit > 0:
    profit = profit * 0.65
print(profit)
