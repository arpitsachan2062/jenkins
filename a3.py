import requests
from fpdf import FPDF

# Define the base URL for the API
base_url = "https://9b59-2401-4900-8845-31ce-e58b-56cd-3386-628e.ngrok-free.app/services/json/v1"

# List of review IDs to pass
review_ids = [52, 12, 1]  # Add more review IDs as needed

# Function to create a PDF from the response content
def create_pdf(response_data, review_id):
    pdf = FPDF()
    pdf.add_page()
    
    pdf.set_font("Arial", size=12)
    
    # Add a title or header to the PDF
    pdf.cell(200, 10, txt=f"Review Versions for Review ID: {review_id}", ln=True, align="C")
    pdf.ln(10)  # Add some space after the title
    
    # Assuming response_data contains structured information such as a dictionary or list
    if isinstance(response_data, dict):
        # Loop over the dictionary to format each section clearly
        for key, value in response_data.items():
            pdf.ln(5)  # Adding line break for better readability
            
            # Bold the section header
            pdf.set_font("Arial", style='B', size=12)
            pdf.cell(200, 10, txt=f"{key}:", ln=True)
            
            # Regular font for the content
            pdf.set_font("Arial", size=12)
            
            # If value is a list or dictionary, make it a string
            if isinstance(value, (list, dict)):
                value = str(value)
            
            # Add the content with proper line breaks
            pdf.multi_cell(0, 10, value)
    
    else:
        # If the response is not a dictionary, just print it as plain text
        pdf.multi_cell(0, 10, str(response_data))
    
    # Save the PDF to a file
    output_filename = f"review_{review_id}_versions.pdf"
    pdf.output(output_filename)
    print(f"PDF for review ID {review_id} has been saved as {output_filename}.")

# Make API requests for each review ID
for review_id in review_ids:
    print(f"Getting review versions for review ID: {review_id}")
    
    response = requests.post(base_url, json=[
        {"command": "Examples.checkLoggedIn"},
        {"command": "SessionService.authenticate", 
         "args": {"login": "arpit.sachan", "ticket": "a52a5848abc217105b114d643e131cd4"}},
        {"command": "ReviewService.getVersions", 
         "args": {"reviewId": review_id}
        }
    ])
    
    # Check if the request was successful
    if response.status_code == 200:
        # Create a PDF for the response data
        create_pdf(response.json(), review_id)
    else:
        print(f"Error retrieving data for review ID {review_id}.")
    
    print("-" * 50)  # Separator line for clarity
