import os
import requests

def fetch_conferences(url, headers):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        if response.text.strip():  # Check if response is not empty
            return response.text  # Return response text directly
        else:
            print("Response is empty.")
            return None
    except requests.exceptions.RequestException as e:
        print("Failed to fetch page:", e)
        return None

def save_to_txt(data, filename):
    with open(filename, 'w') as file:
        file.write(data)
    # Print the absolute path of the saved file
    print("File saved to:", os.path.abspath(filename))

def main():
    url = 'https://conferenceineurope.net/topic-list/information-technology'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.999 Safari/537.36'
    }  # Set a valid User-Agent
    conferences_data = fetch_conferences(url, headers)
    
    if conferences_data:
        # Save data to a text file
        save_to_txt(conferences_data, 'conferences.txt')
        print("Conferences data saved to conferences.txt")
    else:
        print("No conferences found.")

if __name__ == "__main__":
    main()
