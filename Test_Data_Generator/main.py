import openai
import csv
import re

# Set your OpenAI API key
openai.api_key = "API_KEY"

# Function to generate test data using OpenAI (updated for chat model)
def generate_test_data(data_type, constraints, num_samples=10):
    """
    Generates test data using OpenAI's API based on the data type and constraints.
    """
    prompt = f"""
    Generate {num_samples} examples of {data_type}.
    Constraints: {constraints}.
    Provide the output as a list of items.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # or another chat model
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": prompt}],
            max_tokens=250,
            n=1,
            stop=None
        )
        # Parse the response text and split into lines
        data = response['choices'][0]['message']['content'].strip().split("\n")
        return [item.strip() for item in data if item.strip()]
    except Exception as e:
        print(f"Error generating test data: {e}")
        return []

# Function to validate data using a regex pattern
def validate_data(data, pattern):
    """
    Validates generated data based on a provided regex pattern.
    """
    validated_data = [item for item in data if re.match(pattern, item)]
    return validated_data

# Function to save data to a CSV file
def save_to_csv(data, filename="test_data.csv"):
    """
    Saves the generated and validated data to a CSV file.
    """
    try:
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Generated Data"])
            writer.writerows([[item] for item in data])
        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"Error saving data to CSV: {e}")

# Main function to interact with the user
def main():
    print("\n=== Welcome to the Test Data Generator ===\n")
    
    # Collect user inputs
    data_type = input("Enter the type of data to generate (e.g., email addresses, phone numbers): ").strip()
    constraints = input("Enter constraints for the data (e.g., 'must contain @', '10-digit format'): ").strip()
    num_samples = int(input("Enter the number of samples to generate: ").strip())
    pattern = input("Enter a regex pattern for validation (optional, press Enter to skip): ").strip()
    
    # Generate data
    print("\nGenerating data...")
    generated_data = generate_test_data(data_type, constraints, num_samples)
    
    # Validate data if regex pattern is provided
    if pattern:
        print("Validating data...")
        validated_data = validate_data(generated_data, pattern)
        print(f"Validated {len(validated_data)} out of {len(generated_data)} items.")
    else:
        validated_data = generated_data

    # Display the generated data
    print("\nGenerated Data:")
    for item in validated_data:
        print(f"- {item}")
    
    # Save data to a CSV file
    save_choice = input("\nWould you like to save the data to a CSV file? (yes/no): ").strip().lower()
    if save_choice == "yes":
        filename = input("Enter the filename (default: test_data.csv): ").strip() or "test_data.csv"
        save_to_csv(validated_data, filename)

if __name__ == "__main__":
    main()