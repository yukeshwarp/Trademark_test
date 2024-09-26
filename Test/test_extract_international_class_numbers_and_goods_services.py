import pytest  
from unittest.mock import MagicMock  
import re  
from typing import Dict, Union, List  
from main_app import extract_international_class_numbers_and_goods_services
# The function to be tested  
#def extract_international_class_numbers_and_goods_services(document: str, start_page: int, pdf_document: 'fitz.Document') -> Dict[str, Union[List[int], str]]:  
#    """ Extract the International Class Numbers and Goods/Services from the document over a range of pages """  
#    class_numbers = []  
#    goods_services = []  
#    combined_text = ""  
#    for i in range(start_page, min(start_page + 6, pdf_document.page_count)):  
#        page = pdf_document.load_page(i)  
#        page_text = page.get_text()  
#        combined_text += page_text  
#        if "Last Reported Owner:" in page_text:  
#            break  
#    pattern = r'International Class (\d+): (.*?)(?=\nInternational Class \d+:|\n[A-Z][a-z]+:|\nLast Reported Owner:|Disclaimers:|\Z)'  
#    matches = re.findall(pattern, combined_text, re.DOTALL)  
#    for match in matches:  
#        class_number = int(match[0])  
#        class_numbers.append(class_number)  
#        goods_services.append(f"Class {class_number}: {match[1].strip()}")  
#    return {  
#        "international_class_numbers": class_numbers,  
#        "goods_services": "\n".join(goods_services)  
#    }  
  
# Test cases  
def test_extract_international_class_numbers_and_goods_services():  
    # Create a mock PDF document  
    mock_pdf_document = MagicMock()  
    mock_pdf_document.page_count = 10  
      
    # Mock the pages' text content  
    mock_pages_text = [  
        "International Class 1: Chemicals for use in industry.\nInternational Class 2: Paints.",  
        "International Class 3: Cleaning substances.\nLast Reported Owner: Some Owner",  
        "Page 4 content",  
        "Page 5 content",  
        "Page 6 content",  
        "Page 7 content",  
        "Page 8 content",  
        "Page 9 content",  
        "Page 10 content",  
    ]  
      
    # Configure the mock to return the appropriate page text  
    mock_pdf_document.load_page.side_effect = [MagicMock(get_text=MagicMock(return_value=text)) for text in mock_pages_text]  
      
    # Define the expected output  
    expected_output = {  
        "international_class_numbers": [1, 2, 3],  
        "goods_services": "Class 1: Chemicals for use in industry.\nClass 2: Paints.\nClass 3: Cleaning substances."  
    }  
      
    # Call the function with the mock document  
    result = extract_international_class_numbers_and_goods_services("", 0, mock_pdf_document)  
    
    print(result)
    print(expected_output)
    # Assert the result matches the expected output  
    assert result == expected_output  
  
if __name__ == "__main__":  
    pytest.main()  
