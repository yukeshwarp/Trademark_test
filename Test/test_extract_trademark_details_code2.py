import pytest  
from typing import Dict, Union, List  
import re  

# Assuming this is the function to be tested  
def extract_trademark_details_code2(page_text: str) -> Dict[str, Union[str, List[int]]]:  
    details = {}  
  
    trademark_name_match = re.search(r"\d+\s*/\s*\d+\s*\n\s*\n\s*([A-Za-z0-9'&!,\-. ]+)\s*\n", page_text)  
    if trademark_name_match:  
        details["trademark_name"] = trademark_name_match.group(1).strip()  
    else:  
        trademark_name_match = re.search(r"(?<=\n)([A-Za-z0-9'&!,\-. ]+)(?=\n)", page_text)  
        details["trademark_name"] = trademark_name_match.group(1).strip() if trademark_name_match else ""  
  
    status_match = re.search(r'Status\s*(?:\n|:\s*)([A-Za-z]+)', page_text, re.IGNORECASE)  
    details["status"] = status_match.group(1).strip() if status_match else ""  
  
    owner_match = re.search(r'Holder\s*(?:\n|:\s*)(.*)', page_text, re.IGNORECASE)  
    if owner_match:  
        details["owner"] = owner_match.group(1).strip()  
    else:  
        owner_match = re.search(r'Owner\s*(?:\n|:\s*)(.*)', page_text, re.IGNORECASE)  
        details["owner"] = owner_match.group(1).strip() if owner_match else ""  
      
    nice_classes_match = re.search(r'Nice Classes\s*[\s:]*\n((?:\d+(?:,\s*\d+)*)\b)', page_text, re.IGNORECASE)  
    if nice_classes_match:  
        nice_classes_text = nice_classes_match.group(1)  
        nice_classes = [int(cls.strip()) for cls in nice_classes_text.split(",")]  
        details["international_class_number"] = nice_classes  
    else:  
        details["international_class_number"] = []  
      
    serial_number_match = re.search(r'Application#\s*(.*?)(?=\s|$)', page_text, re.IGNORECASE)  
    details["serial_number"] = serial_number_match.group(1).strip() if serial_number_match else ""  
  
    goods_services_match = re.search(r'Goods & Services\s*(.*?)(?=\s*G&S translation|$)', page_text, re.IGNORECASE | re.DOTALL)  
    details["goods_services"] = goods_services_match.group(1).strip() if goods_services_match else ""  
  
    registration_number_match = re.search(r'Registration#\s*(.*?)(?=\s|$)', page_text, re.IGNORECASE)  
    details["registration_number"] = registration_number_match.group(1).strip() if registration_number_match else ""  
  
    design_phrase = re.search(r'Description\s*(.*?)(?=\s*Applicant|Owner|Holder|$)', page_text, re.IGNORECASE | re.DOTALL)  
    details["design_phrase"] = design_phrase.group(1).strip() if design_phrase else "No Design phrase presented in document"  
  
    return details  

# Test cases  
def test_extract_trademark_details_code2():  
    sample_text = """  
    1234 / 5678  
    Example Trademark Name  
    Status: Registered  
    Holder: Example Holder Name  
    Nice Classes: 35, 42  
    Application#: 12345678  
    Goods & Services: Some goods and services here.  
    Registration#: 987654321  
    Description: This is a sample design phrase.  
    """  
    
    expected_output = {  
        'trademark_name': 'Example Trademark Name',  
        'status': 'Registered',  
        'owner': 'Example Holder Name',  
        'international_class_number': [35, 42],  
        'serial_number': '12345678',  
        'goods_services': 'Some goods and services here.',  
        'registration_number': '987654321',  
        'design_phrase': 'This is a sample design phrase.'  
    }  
    
    actual_output = extract_trademark_details_code2(sample_text)
    
    # Print the actual output for debugging
    print("Actual Output:", actual_output)
    
    assert actual_output == expected_output  

if __name__ == "__main__":  
    pytest.main()  
