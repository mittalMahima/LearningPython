import math

def buystocks(prices):
    buy_price = math.inf
    max_profit = 0
    
    for price in prices:
        if buy_price < price:
            # Today's profit
            profit = price - buy_price
            max_profit = max(profit, max_profit)
        else:
            buy_price = price
            
    return max_profit

if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print("Maximum profit is ",buystocks(prices))
