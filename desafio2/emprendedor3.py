import sys
price = float(sys.argv[1])
users = float(sys.argv[2])
spents = float(sys.argv[3])
profit = (price * users) - spents
profit_base = 1000
if profit > 0:
    profit = profit * 0.65
if len(sys.argv) > 4:
    print((profit/int(sys.argv[4]))*100)
else:
    print((profit/profit_base)*100)