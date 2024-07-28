import yfinance as yf
import pandas as pd

def track_portfolio(stocks):
    # Create an empty DataFrame to store portfolio data
    portfolio_data = pd.DataFrame(columns=['Stock', 'Shares', 'Price', 'Total Value'])

    # Iterate through each stock in the portfolio
    for stock, shares in stocks.items():
        # Fetch stock data
        ticker = yf.Ticker(stock)
        current_price = ticker.history(period='1d')['Close'][0]
        
        # Calculate total value of each stock
        total_value = current_price * shares
        
        # Append data to DataFrame
        portfolio_data = portfolio_data.append({
            'Stock': stock,
            'Shares': shares,
            'Price': current_price,
            'Total Value': total_value
        }, ignore_index=True)
    
    # Print portfolio data
    print("Current Portfolio:")
    print(portfolio_data)
    
    # Calculate total portfolio value
    total_portfolio_value = portfolio_data['Total Value'].sum()
    print(f"\nTotal Portfolio Value: ${total_portfolio_value:.2f}")

if __name__ == "__main__":
    # Example usage with a dictionary of stocks and shares
    my_stocks = {
        'AAPL': 10,   # Apple Inc.
        'MSFT': 5,    # Microsoft Corporation
        'GOOGL': 3,   # Alphabet Inc. (Google)
        'TSLA': 2     # Tesla, Inc.
    }
    
    track_portfolio(my_stocks)
