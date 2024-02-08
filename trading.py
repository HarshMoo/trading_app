import yfinance as yf

def get_data(ticker_symbol,thing):
    try:
        ticker = yf.Ticker(ticker_symbol)
        
        current_price = ticker.history(period='1d')[thing][0]
        
        return current_price
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None
    
def get_price(ticker_symbol):

    return get_data(ticker_symbol,"Close")

def get_volume(ticker_symbol):

    return get_data(ticker_symbol,"Volume")
    
def get_dividend_yield(ticker_symbol):
    try:
        ticker = yf.Ticker(ticker_symbol)
        
        dividend_per_share = ticker.dividends.iloc[-1] 

        current_price = ticker.history(period='1d')['Close'][0]
        
        dividend_yield_ratio = (dividend_per_share / current_price) * 100  # Multiply by 100 to convert to percentage
        
        return dividend_yield_ratio
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None