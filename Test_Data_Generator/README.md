
Test Data Generator

The Test Data Generator is a Python-based tool that uses OpenAI’s GPT model to generate synthetic data based on user-defined constraints. It can generate various types of data (e.g., email addresses, phone numbers, etc.), validate it using regex patterns, and save it to a CSV file for further use.

---

Features

- Generate Test Data: Generates synthetic data based on specified data type and constraints.
- Data Validation: Optionally validates the generated data using regular expressions (regex).
- Save to CSV: Saves the valid data to a CSV file for easy access and reuse.

---

Requirements

- Python 3.x
- OpenAI Python library

Install the required library with:

pip install openai

---

Setup

1. Get Your OpenAI API Key:

   You need an OpenAI API key to interact with the GPT model. You can get your API key from the OpenAI platform (https://platform.openai.com).

2. Configure Your API Key:

   In the Python script main.py, replace the placeholder your_openai_api_key with your actual API key.

openai.api_key = "your_openai_api_key"

---

How to Run

1. Clone the Repository (Optional):

   If you’re using Git, clone the repository to your local machine:

   git clone https://github.com/yourusername/test-data-generator.git
   cd test-data-generator

2. Run the Script:

   Execute the script with:

   python main.py

3. Provide Input:

   You will be prompted to enter the following:
   - Data Type: The type of data you want to generate (e.g., email addresses, phone numbers).
   - Constraints: Any rules for the data (e.g., format or length).
   - Number of Samples: How many data samples you need.
   - Regex Pattern (Optional): A regex pattern to validate the generated data (optional).

4. Output:

   After entering the required information, the script will:
   - Generate the data.
   - Validate it (if you provided a regex pattern).
   - Display the generated data in the console.
   - Ask if you want to save it to a CSV file.

5. Save to CSV (Optional):

   If you choose to save the data, the script will prompt you to specify the filename (or use the default test_data.csv).

---

Example

Input Example:

- Data Type: email addresses
- Constraints: username@domain.com
- Number of Samples: 10
- Regex Pattern: ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$

Output Example:

user1@example.com
test.user2@domain.org
random.person3@company.net
...

You’ll be prompted to save the data to a CSV file, like test_data.csv.

---

License

MIT License
