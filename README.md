
# Volatility Calculator

This project calculates the volatility for specified stock tickers over given date ranges and frequencies. It uses Yahoo Finance data to compute the volatility, which can be configured through a JSON file.

## Features

- Calculate daily, weekly, or monthly volatility for a list of stock tickers.
- Configurable input through a JSON file.
- Save results to a CSV file.

## Prerequisites

Ensure you have Python installed (preferably version 3.6 or higher). You can download it from [python.org](https://www.python.org/).

## Setup

### Option 1: Clone the Repository

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/ahmetybesiroglu/volatility-calculator.git
cd volatility-calculator
```

### Option 2: Download the Repository

1. Go to the repository's page on GitHub: [Volatility-Calculator](https://github.com/ahmetybesiroglu/volatility-calculator).
2. Click the green `Code` button.
3. Select `Download ZIP`.
4. Extract the ZIP file to your desired location.
5. Navigate to the extracted folder.

### Create and Activate a Virtual Environment

It's a good practice to use a virtual environment to manage dependencies. You can create and activate a virtual environment with the following commands:

For Windows:

```bash
python3 -m venv env
env\Scripts\activate
```

For macOS and Linux:

```bash
python3 -m venv env
source env/bin/activate
```

### Install Dependencies

Install the required dependencies using the provided `requirements.txt` file:

```bash
pip3 install -r requirements.txt
```

## Configuration

### JSON Configuration File

Edit the `config/config.json` file to specify the tickers, frequencies, start dates, and end dates. Here is an example of what the file looks like:

```json
{
  "tickers": ["AAPL", "MSFT", "GOOGL", "AMZN", "META", "TSLA", "NVDA"],
  "frequencies": ["weekly", "weekly", "weekly"],
  "start_dates": ["1/1/2020", "1/1/2021", "1/1/2022"],
  "end_dates": ["12/31/2020", "12/31/2021", "12/31/2022"]
}
```

## Running the Script

Run the script to calculate volatilities:

```bash
python3 src/volatility_calculator.py
```

### Example Usage

1. Ensure your `config/config.json` file is properly configured with the tickers, frequencies, start dates, and end dates.
2. Run the script:

```bash
python3 src/volatility_calculator.py
```

### Expected Output

The script will calculate the volatility for each ticker and save the results in a CSV file located in the `output` directory. The CSV file will look like this:

```csv
Ticker,1/1/2020 to 12/31/2020,1/1/2021 to 12/31/2021,1/1/2022 to 12/31/2022
AAPL,32.45,30.87,29.54
MSFT,24.56,23.45,22.34
GOOGL,21.34,20.56,19.87
AMZN,28.76,27.89,26.45
META,26.32,25.65,24.78
TSLA,33.78,32.45,31.67
NVDA,29.54,28.76,27.89
```

## Methodology

The methodology for calculating volatility is as follows:

1. **Data Retrieval**: Historical stock price data is retrieved from Yahoo Finance for the specified tickers and date ranges.
2. **Adjusting Data Frequency**: The adjusted close prices are resampled to the specified frequency (daily, weekly, or monthly).
3. **Log Returns Calculation**: The logarithmic returns are calculated using the formula:

   $$\text{log\_returns} = \log\left(\frac{\text{prices}}{\text{prices.shift(1)}}\right)$$

4. **Volatility Calculation**: The standard deviation of the log returns over the entire date range is calculated and annualized using the appropriate factor based on the frequency:
   - Daily: $ \sqrt{252} $
   - Weekly: $ \sqrt{52} $
   - Monthly: $ \sqrt{12} $
5. **Annualized Volatility**: The calculated standard deviation is multiplied by the annual factor to get the annualized volatility, which is then expressed as a percentage.

This approach ensures that the volatility represents the price variation over the entire specified date range, giving a comprehensive view of the stock's historical volatility.





## Project Structure

```
volatility-calculator/
├── README.md
├── LICENSE
├── requirements.txt
├── config/
│   └── config.json
├── src/
│   └── volatility_calculator.py
├── output/
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## Troubleshooting

If you encounter any issues, ensure that all dependencies are correctly installed and that your Python version is compatible. If problems persist, feel free to open an issue in the repository.

## Contact

For further questions, please contact ahmetybesiroglu@gmail.com.
