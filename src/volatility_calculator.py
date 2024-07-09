import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime
import json
import os

def calculate_volatility(ticker, start_date, end_date, frequency='weekly'):
    start_date = datetime.strptime(start_date, '%m/%d/%Y').strftime('%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%m/%d/%Y').strftime('%Y-%m-%d')
    data = yf.download(ticker, start=start_date, end=end_date, interval='1d')

    if data.empty:
        raise ValueError(f"No data found for {ticker} from {start_date} to {end_date}")

    adj_close = data['Adj Close']

    if frequency == 'daily':
        prices = adj_close
        annual_factor = np.sqrt(252)
    elif frequency == 'weekly':
        prices = adj_close.resample('W-FRI').last()
        annual_factor = np.sqrt(52)
    elif frequency == 'monthly':
        prices = adj_close.resample('M').last()
        annual_factor = np.sqrt(12)
    else:
        raise ValueError("Invalid frequency. Use 'daily', 'weekly', or 'monthly'.")

    log_returns = np.log(prices / prices.shift(1)).dropna()
    volatility = log_returns.std() * annual_factor
    return round(volatility * 100, 2)

def load_config(config_path):
    with open(config_path, 'r') as file:
        config = json.load(file)
    return config

if __name__ == "__main__":
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.json')
    config = load_config(config_path)

    tickers = config['tickers']
    frequencies = config['frequencies']
    start_dates = config['start_dates']
    end_dates = config['end_dates']

    columns = ['Ticker'] + [f"{start} to {end}" for start, end in zip(start_dates, end_dates)]
    results_df = pd.DataFrame(columns=columns)

    for ticker in tickers:
        row = [ticker]
        for frequency, start_date, end_date in zip(frequencies, start_dates, end_dates):
            try:
                volatility = calculate_volatility(ticker, start_date, end_date, frequency)
                row.append(volatility)
            except Exception as e:
                print(f"Error for {ticker} from {start_date} to {end_date}: {e}")
                row.append(None)
        row_df = pd.DataFrame([row], columns=columns)
        results_df = pd.concat([results_df, row_df], ignore_index=True)

    output_dir = os.path.join(os.path.dirname(__file__), '..', 'output')
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, 'volatility_results.csv')
    results_df.to_csv(output_file, index=False)

    print(f"Results saved to {output_file}")
