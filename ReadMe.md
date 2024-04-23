
# Browser Cookie Analyzer

## Overview
The Browser Cookie Analyzer is a Python script that analyzes and reports on browser cookies from popular web browsers such as Chrome and Brave. It extracts cookie data from the browser's database file and exports it to an Excel file for easy analysis.

## Features
- Supports multiple browsers, including Chrome and Brave.
- Analyzes cookies from both regular and incognito/private browsing sessions.
- Extracts cookie data such as name, value, host, path, expiration date, and whether it's secure.
- Exports the analyzed cookie data to an Excel file for further analysis.

## Installation
1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/shreyas0201/cookie-analyzer.git
    ```

2. Install the required Python packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Run the script `script.py`:

    ```bash
    python script.py
    ```

2. Follow the prompts to enter the names of the browsers and profiles you want to analyze cookies for.

3. The script will generate Excel files named `Report_Browser_Profile.xlsx` containing the analyzed cookie data.

## Example
python script.py
Starting browser cookie analysis tool...
Enter the names of the browsers separated by commas (e.g., Brave, Chrome): Chrome, Brave
Cookie data for Chrome (Default) exported to 'Report_Chrome_Default.xlsx'
Cookie data for Brave (Default) exported to 'Report_Brave_Default.xlsx'


## Contributing
Contributions are welcome! If you'd like to contribute to this project, please fork the repository, make your changes, and submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).
