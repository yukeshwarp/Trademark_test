import pytest
import fitz  # PyMuPDF
import re  # Import the regular expression module
from typing import Dict, List, Union

# The function to be tested
def extract_design_phrase(document: str, start_page: int, pdf_document: fitz.Document) -> Dict[str, Union[List[int], str]]:
    """ Extract the design phrase from the document. """
    
    combined_texts = ""
    
    # Loop through the pages, stopping if we find "Filing Correspondent:"
    for i in range(start_page, min(start_page + 8, pdf_document.page_count)):
        page = pdf_document.load_page(i)
        page_text = page.get_text()
        combined_texts += page_text
        
        # Stop if the target phrase is found
        if "Filing Correspondent:" in page_text:
            break

    # Regex pattern to extract the design phrase
    pattern = r'Design Phrase:\s*(.*?)(?=Other U\.S\. Registrations:|Filing Correspondent:|Group:|USPTO Page:|$)'
    match = re.search(pattern, combined_texts, re.DOTALL) 
    
    if match:
        design_phrase = match.group(1).strip()
        # Remove any newline characters within the design phrase
        design_phrase = ' '.join(design_phrase.split())
        return {"design_phrase": design_phrase}  # Returning as a dictionary
    
    return {"design_phrase": "No Design phrase presented in document"}  # Consistent return type

# Create a helper function to generate a mock PDF document
def create_mock_pdf(pages_content):
    pdf_document = fitz.open()  # Create a new PDF document
    for content in pages_content:
        page = pdf_document.new_page()  # Add a new page
        page.insert_text((50, 50), content)  # Insert text into the page
    return pdf_document

# Test function
def test_extract_design_phrase():
    # Mock PDF content
    pages_content = [
        "This is a test document.\nDesign Phrase: Sample Design Phrase Here.\nOther U.S. Registrations:",
        "This page should not be needed.",
        "Filing Correspondent: John Doe",
        "Another page without the design phrase."
    ]

    # Create a mock PDF document with the above content
    mock_pdf = create_mock_pdf(pages_content)

    # Call the function to test
    result = extract_design_phrase("Dummy string for regex", 0, mock_pdf)

    # Expected result
    expected_result = {"design_phrase": "Sample Design Phrase Here."}

    # Assert the result matches the expected output
    assert result == expected_result

    # Cleanup
    mock_pdf.close()

# Running the test
test_extract_design_phrase()
