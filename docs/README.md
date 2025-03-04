# aptiq_interview
This repo will address the following exercise with step by step instructions. 

# Problem Statement
Please generate a python project that will conduct webscraping to collect information from the
humor category of https://books.toscrape.com/
We recommend using a recent version of python as well as a parsing library such as beautiful
soup.

Additionally capture the following:
  1. Scrape all books in the Humor category:
      - Follow pagination if there are multiple pages.
      - For each book, collect:
        - UPC (from the product page)
        - Title
        - Price
        - Image URL
  2. Output the collected data as a list of objects in a JSON file, with one entry per book.
      - The output will be stored in a provided directory
  4. Document all steps so another developer can:
      - Install required libraries (e.g., beautifulsoup4, requests).
      - Run the script to reproduce the same results.

# Instructions on how to execute package (suggested)
  1. Ensure Python is installed on the operating system
  2. Clone the GitHub repository - gh repo clone steiner-de/aptiq_interview
  3. Open the terminal or command prompt and navigate to the local directory containing the cloned repository
  4. Execute the setup_and_run.bat or setup_and_run.sh file (use .bat for Windows and .bash for unix/MacOS
    a. To execute the setup_and_run.sh file execute the following:
      `./setup_and_run.sh`
  5. The output file will be generated in the working directory  
# Alternative Execution
  1. Ensure Python is installed on the operating system
  2. Clone the GitHub repository - gh repo clone steiner-de/aptiq_interview
  3. Open the terminal/command prompt and navigate to the repository location
  4. In the terminal/command prompt execute the following command 'pip install -r requirements.txt'
  5. From the terminal/command prompt execute the following command
    a. Option 1: Execute from the terminal (Unix/MacOS)
        - python3 /src/main.py
    b. Option 2: Execute from the command line (windows)
        - python3 src/main.py
    c. Option 3: In the IDE run the /src/main.py file
  6. Output json file will be located in the current working directory.