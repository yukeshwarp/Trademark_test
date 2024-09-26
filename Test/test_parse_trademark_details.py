import pytest  
from unittest.mock import patch, MagicMock  
from typing import List, Dict, Union  
  
# Import the function to be tested  
from main_app import parse_trademark_details  
  
# Helper functions to mock  
def mock_is_correct_format_code1(text):  
    return True  
  
def mock_preprocess_text(text):  
    return text  
  
def mock_extract_trademark_details_code1(text):  
    return {  
        "trademark_name": "Example Trademark",  
        "owner": "Example Owner",  
        "status": "Active",  
        "serial_number": "123456",  
        "international_class_numbers": [1, 2, 3],  
        "goods_services": "Example Goods/Services"  
    }  
  
def mock_extract_international_class_numbers_and_goods_services(text, page_num, pdf_document):  
    return {  
        "international_class_numbers": [1, 2, 3],  
        "goods_services": "Example Goods/Services"  
    }  
  
def mock_extract_registration_number(text):  
    return "7891011"  
  
def mock_extract_design_phrase(text, page_num, pdf_document):  
    return "Example Design Phrase"  
  
class MockPDFPage:  
    def __init__(self, text):  
        self.text = text  
      
    def get_text(self):  
        return self.text  
  
class MockPDFDocument:  
    def __init__(self, pages):  
        self.pages = pages  
        self.page_count = len(pages)  
      
    def load_page(self, page_num):  
        return self.pages[page_num]  
      
    def __enter__(self):  
        return self  
      
    def __exit__(self, exc_type, exc_val, exc_tb):  
        pass  
  
# Mock data  
mock_pdf_pages = [  
    MockPDFPage("Page 1 text"),  
    MockPDFPage("Page 2 text"),  
]  
  
mock_pdf_document = MockPDFDocument(mock_pdf_pages)  
  
# Test function  
@patch('main_app.fitz.open', return_value=mock_pdf_document)  
@patch('main_app.is_correct_format_code1', mock_is_correct_format_code1)  
@patch('main_app.preprocess_text', mock_preprocess_text)  
@patch('main_app.extract_trademark_details_code1', mock_extract_trademark_details_code1)  
@patch('main_app.extract_international_class_numbers_and_goods_services', mock_extract_international_class_numbers_and_goods_services)  
@patch('main_app.extract_registration_number', mock_extract_registration_number)  
@patch('main_app.extract_design_phrase', mock_extract_design_phrase)  
def test_parse_trademark_details(mock_open):  
    expected_output = [  
        {  
            "trademark_name": "Example Trademark",  
            "owner": "Example Owner",  
            "status": "Active",  
            "serial_number": "123456",  
            "international_class_number": [1, 2, 3],  
            "goods_services": "Example Goods/Services",  
            "page_number": 1,  
            "registration_number": "7891011",  
            "design_phrase": "Example Design Phrase",  
        },  
        {  
            "trademark_name": "Example Trademark",  
            "owner": "Example Owner",  
            "status": "Active",  
            "serial_number": "123456",  
            "international_class_number": [1, 2, 3],  
            "goods_services": "Example Goods/Services",  
            "page_number": 2,  
            "registration_number": "7891011",  
            "design_phrase": "Example Design Phrase",  
        }  
    ]  
      
    actual_output = parse_trademark_details("dummy_path")  
      
    assert actual_output == expected_output  
  
if __name__ == "__main__":  
    pytest.main()  
