from accounts import Account
import gradio as gr

# Initialize account for demonstration
account = Account(user_id="test_user")

def create_account():
    global account
    account = Account(user_id="new_user")
    return "Account created successfully"

def deposit(amount):
    if account.deposit(float(amount)):
        return f"Deposited: ${amount}. Updated Balance: ${account.balance}"
    else:
        return "Deposit failed. Amount must be greater than 0."

def withdraw(amount):
    if account.withdraw(float(amount)):
        return f"Withdrew: ${amount}. Updated Balance: ${account.balance}"
    else:
        return "Withdrawal failed. Check the amount and balance."

def buy_shares(symbol, quantity):
    if account.buy_shares(symbol, int(quantity)):
        return f"Bought {quantity} shares of {symbol}. Updated Balance: ${account.balance}"
    else:
        return "Purchase failed. Check balance or quantity."

def sell_shares(symbol, quantity):
    if account.sell_shares(symbol, int(quantity)):
        return f"Sold {quantity} shares of {symbol}. Updated Balance: ${account.balance}"
    else:
        return "Sale failed. Check holdings or quantity."

def get_portfolio_value():
    return f"Total Portfolio Value: ${account.get_portfolio_value()}"

def get_profit_or_loss():
    return f"Profit/Loss: ${account.get_profit_or_loss()}"

def get_holdings():
    return f"Holdings: {account.get_holdings()}"

def get_transactions():
    return f"Transactions: {account.get_transactions()}"

with gr.Blocks() as app:
    gr.Markdown("# Trading Simulation Platform")
    
    with gr.Tab("Account Management"):
        create_button = gr.Button("Create Account")
        create_account_status = gr.Textbox()
        create_button.click(create_account, outputs=create_account_status)
        
        deposit_amount = gr.Number(label="Deposit Amount")
        deposit_button = gr.Button("Deposit")
        deposit_status = gr.Textbox()
        deposit_button.click(deposit, inputs=deposit_amount, outputs=deposit_status)
        
        withdraw_amount = gr.Number(label="Withdraw Amount")
        withdraw_button = gr.Button("Withdraw")
        withdraw_status = gr.Textbox()
        withdraw_button.click(withdraw, inputs=withdraw_amount, outputs=withdraw_status)
    
    with gr.Tab("Trading"):
        buy_symbol = gr.Textbox(label="Symbol")
        buy_quantity = gr.Number(label="Quantity")
        buy_button = gr.Button("Buy Shares")
        buy_status = gr.Textbox()
        buy_button.click(buy_shares, inputs=[buy_symbol, buy_quantity], outputs=buy_status)
        
        sell_symbol = gr.Textbox(label="Symbol")
        sell_quantity = gr.Number(label="Quantity")
        sell_button = gr.Button("Sell Shares")
        sell_status = gr.Textbox()
        sell_button.click(sell_shares, inputs=[sell_symbol, sell_quantity], outputs=sell_status)
        
    with gr.Tab("Reports"):
        value_button = gr.Button("Get Portfolio Value")
        value_status = gr.Textbox()
        value_button.click(get_portfolio_value, outputs=value_status)
        
        profit_button = gr.Button("Get Profit/Loss")
        profit_status = gr.Textbox()
        profit_button.click(get_profit_or_loss, outputs=profit_status)
        
        holdings_button = gr.Button("Get Holdings")
        holdings_status = gr.Textbox()
        holdings_button.click(get_holdings, outputs=holdings_status)
        
        transactions_button = gr.Button("Get Transactions")
        transactions_status = gr.Textbox()
        transactions_button.click(get_transactions, outputs=transactions_status)

if __name__ == "__main__":
    app.launch()