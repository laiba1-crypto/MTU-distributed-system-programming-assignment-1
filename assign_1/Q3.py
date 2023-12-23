# Implementing Strategy Design Pattern
class Stock_Investment:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def purchase_stock(self, investment, current_price):
        return self.strategy.purchase_stock(investment, current_price)

class Aggressive:
    def purchase_stock(self, investment, current_price):
        return investment, current_price

class Passive:
    def purchase_stock(self, investment, current_price):
        invested = investment * 0.5
        target_price = current_price * 0.9
        return invested, target_price

# For Sample Run
aggressive_strategy = Aggressive()
passive_strategy = Passive()

purchaser = Stock_Investment(aggressive_strategy)

# Purchase(aggressive strategy)
investment, price = purchaser.purchase_stock(2500, 70)
print(f"Buying €{investment} worth of stock, €{price} per share")

# Purchase again(passive strategy)
purchaser.set_strategy(passive_strategy)
investment, price = purchaser.purchase_stock(2500, 70)
print(f"Buying €{investment} worth of stock, €{price} per share")