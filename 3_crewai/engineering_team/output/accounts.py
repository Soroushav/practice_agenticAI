class Account:
    def __init__(self, user_id: str) -> None:
        self.user_id = user_id
        self.balance = 0.0
        self.transactions = []
        self.holdings = {}

    def deposit(self, amount: float) -> bool:
        if amount <= 0:
            return False
        self.balance += amount
        self.transactions.append({'type': 'deposit', 'amount': amount})
        return True

    def withdraw(self, amount: float) -> bool:
        if amount <= 0 or amount > self.balance:
            return False
        self.balance -= amount
        self.transactions.append({'type': 'withdraw', 'amount': amount})
        return True

    def buy_shares(self, symbol: str, quantity: int) -> bool:
        if quantity <= 0:
            return False
        share_price = get_share_price(symbol)
        total_cost = share_price * quantity
        if total_cost > self.balance:
            return False
        self.balance -= total_cost
        self.holdings[symbol] = self.holdings.get(symbol, 0) + quantity
        self.transactions.append({'type': 'buy', 'symbol': symbol, 'quantity': quantity, 'price': share_price})
        return True

    def sell_shares(self, symbol: str, quantity: int) -> bool:
        if quantity <= 0 or self.holdings.get(symbol, 0) < quantity:
            return False
        share_price = get_share_price(symbol)
        total_revenue = share_price * quantity
        self.balance += total_revenue
        self.holdings[symbol] -= quantity
        if self.holdings[symbol] == 0:
            del self.holdings[symbol]
        self.transactions.append({'type': 'sell', 'symbol': symbol, 'quantity': quantity, 'price': share_price})
        return True

    def get_portfolio_value(self) -> float:
        total_value = self.balance
        for symbol, quantity in self.holdings.items():
            total_value += get_share_price(symbol) * quantity
        return total_value

    def get_profit_or_loss(self) -> float:
        initial_deposit = sum(t['amount'] for t in self.transactions if t['type'] == 'deposit')
        current_value = self.get_portfolio_value()
        return current_value - initial_deposit

    def get_holdings(self) -> dict:
        return self.holdings

    def get_transactions(self) -> list:
        return self.transactions


def get_share_price(symbol: str) -> float:
    prices = { 
        'AAPL': 150.0, 
        'TSLA': 800.0, 
        'GOOGL': 2700.0 
    }
    return prices.get(symbol, 0.0)