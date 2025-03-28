import requests

# Define the base URL for the API
base_url = "https://67fa-2405-201-6804-9151-cc49-2824-66d1-9f40.ngrok-free.app/services/json/v1"

# List of review IDs to pass
review_ids = [52, 12, 1]  # Add more review IDs as needed

# Function to print the response content
def print_response_data(response_data, review_id):
    print(f"Review Versions for Review ID: {review_id}")
    print("=" * 50)
    
    # Assuming response_data contains structured information such as a dictionary or list
    if isinstance(response_data, dict):
        # Loop over the dictionary to format each section clearly
        for key, value in response_data.items():
            print(f"\n{key}:")
            
            # If value is a list or dictionary, make it a string
            if isinstance(value, (list, dict)):
                value = str(value)
            
            # Print the content with proper formatting
            print(value)
    
    else:
        # If the response is not a dictionary, just print it as plain text
        print(str(response_data))
    
    print("-" * 50)  # Separator line for clarity

# Make API requests for each review ID
for review_id in review_ids:
    print(f"Getting review versions for review ID: {review_id}")
    
    response = requests.post(base_url, json=[
        {"command": "Examples.checkLoggedIn"},
        {"command": "SessionService.authenticate", 
         "args": {"login": "arpit.sachan", "ticket": "4832766ad217363cb25a586536a6c4f1"}},
        {"command": "ReviewService.getVersions", 
         "args": {"reviewId": review_id}
        }
    ])
    
    # Check if the request was successful
    if response.status_code == 200:
        # Print the response data
        print_response_data(response.json(), review_id)
    else:
        print(f"Error retrieving data for review ID {review_id}.")
    
    print("=" * 50)  # Separator line for clarity
