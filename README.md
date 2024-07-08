
# Stock Options Volatility Calculator

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

\`\`\`bash
git clone https://github.com/yourusername/Stock-Options-Volatility-Calculator.git
cd Stock-Options-Volatility-Calculator
\`\`\`

### Option 2: Download the Repository

1. Go to the repository's page on GitHub: [Stock-Options-Volatility-Calculator](https://github.com/yourusername/Stock-Options-Volatility-Calculator).
2. Click the green \`Code\` button.
3. Select \`Download ZIP\`.
4. Extract the ZIP file to your desired location.
5. Navigate to the extracted folder.

### Create and Activate a Virtual Environment

It's a good practice to use a virtual environment to manage dependencies. You can create and activate a virtual environment with the following commands:

For Windows:

\`\`\`bash
python -m venv env
env\Scripts\activate
\`\`\`

For macOS and Linux:

\`\`\`bash
python3 -m venv env
source env/bin/activate
\`\`\`

### Install Dependencies

Install the required dependencies using the provided \`requirements.txt\` file:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

## Configuration

### JSON Configuration File

Edit the \`config/config.json\` file to specify the tickers, frequencies, start dates, and end dates. Here is an example of what the file looks like:

\`\`\`json
{
  "tickers": [
    "BKKT", "FRGE", "VIRT", "HOOD", "COIN", "TW", "MKTX",
    "AMG", "APO", "ARES", "BX", "OWL", "BPT.L", "CG",
    "EQT.ST", "HLNE", "KKR", "EMG.L", "PGHN.SW", "PHLL.L",
    "SCU", "STEP", "TPG"
  ],
  "frequencies": [
    "weekly", "weekly", "weekly", "weekly", "weekly", "weekly", "daily",
    "weekly", "weekly", "weekly", "weekly", "weekly", "weekly", "weekly"
  ],
  "start_dates": [
    "3/31/2015", "6/30/2015", "9/30/2015", "12/31/2015", "3/31/2016",
    "6/30/2016", "6/30/2023", "9/30/2016", "12/31/2016", "3/31/2017",
    "4/1/2017", "4/1/2018", "4/1/2019"
  ],
  "end_dates": [
    "3/31/2022", "6/30/2022", "9/30/2022", "12/31/2022", "3/31/2023",
    "6/30/2023", "9/30/2023", "9/30/2023", "12/31/2023", "3/31/2024",
    "4/1/2024", "4/1/2024", "4/1/2024"
  ]
}
\`\`\`

## Running the Script

Run the script to calculate volatilities:

\`\`\`bash
python src/volatility_calculator.py
\`\`\`

The results will be saved in the \`output\` directory as \`volatility_results_wide_format.csv\`.

## Project Structure

\`\`\`
Stock-Options-Volatility-Calculator/
├── README.md
├── LICENSE
├── requirements.txt
├── config/
│   └── config.json
├── src/
│   └── volatility_calculator.py
├── data/
└── output/
\`\`\`

## License

This project is licensed under the MIT License. See the \`LICENSE\` file for details.

## Contributing

1. Fork the repository.
2. Create a new branch (\`git checkout -b feature-branch\`).
3. Make your changes.
4. Commit your changes (\`git commit -m 'Add some feature'\`).
5. Push to the branch (\`git push origin feature-branch\`).
6. Create a new Pull Request.

## Troubleshooting

If you encounter any issues, ensure that all dependencies are correctly installed and that your Python version is compatible. If problems persist, feel free to open an issue in the repository.

## Contact

For further questions, please contact [your email].
