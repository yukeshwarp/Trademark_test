import pytest  
import re  
from main_app import extract_registration_number  # Replace 'main_app' with the actual module name where your function is defined.  
  
def test_extract_registration_number():  
    # Test case: Registration number is present  
    document = """  
    Chronology:  
    Some other information  
    Registration Number: 123456  
    """  
    assert extract_registration_number(document) == "123456"  
  
    # Test case: Registration number with commas  
    document = """  
    Chronology:  
    Some other information  
    Registration Number: 1,234,567  
    """  
    assert extract_registration_number(document) == "1,234,567"  
  
    # Test case: No registration number  
    document = """  
    Chronology:  
    Some other information  
    Registration Details: None  
    """  
    assert extract_registration_number(document) == "No registration number presented in document"  
  
    # Test case: Registration number in different section  
    document = """  
    Different Section:  
    Some other information  
    Registration Number: 123456  
    """  
    assert extract_registration_number(document) == "No registration number presented in document"  
  
    # Test case: Empty document  
    document = ""  
    assert extract_registration_number(document) == "No registration number presented in document"  
  
    # Test case: Registration number with additional text  
    document = """  
    Chronology:  
    Some other information  
    Registration Number: 123456. Additional text here.  
    """  
    assert extract_registration_number(document) == "123456"  
  
    # Test case: Multiple registration numbers (should return the first one)  
    document = """  
    Chronology:  
    Some other information  
    Registration Number: 123456  
    Other information  
    Registration Number: 654321  
    """  
    assert extract_registration_number(document) == "123456"  
  
if __name__ == "__main__":  
    pytest.main()  
