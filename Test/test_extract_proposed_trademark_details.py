import pytest  
from unittest.mock import patch, MagicMock  
import re  
from main_app import extract_proposed_trademark_details2  

# Helper function to preprocess text  
def preprocess_text(text):  
    # Assuming preprocess_text just returns the text as is for simplicity  
    return text  

@patch('main_app.fitz.open')  
@patch('main_app.preprocess_text', side_effect=preprocess_text)  
def test_extract_proposed_trademark_details2(mock_preprocess_text, mock_fitz_open):  
    # Mocking the PDF document and its first page's text  
    mock_page = MagicMock()  
    mock_page.get_text.return_value = """Name: Example Trademark  
Nice Classes: 9, 42  
Goods & Services: Software development and design."""  
      
    mock_pdf_document = MagicMock()  
    mock_pdf_document.page_count = 1  
    mock_pdf_document.load_page.return_value = mock_page  
      
    mock_fitz_open.return_value.__enter__.return_value = mock_pdf_document  

    expected_output = {  
        "proposed_trademark_name": "Example Trademark",  
        "proposed_nice_classes_number": "9, 42",  
        "proposed_goods_services": "Software development and design."  
    }  

    actual_output = extract_proposed_trademark_details2("dummy_path")  
      
    assert actual_output == expected_output  

if __name__ == "__main__":  
    pytest.main()  
