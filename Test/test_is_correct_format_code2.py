import pytest  
from main_app import is_correct_format_code2  # Replace 'your_module' with the actual module name where your function is defined.  
  
def test_is_correct_format_code2():  
    # Test case: All required fields are present  
    page_text = "Register\nNice Classes\nGoods & Services"  
    assert is_correct_format_code2(page_text) == True  
  
    # Test case: Missing one required field  
    page_text = "Register\nNice Classes\nSome other info"  
    assert is_correct_format_code2(page_text) == False  
  
    # Test case: Missing all required fields  
    page_text = "Some other info"  
    assert is_correct_format_code2(page_text) == False  
  
    # Test case: Empty string  
    page_text = ""  
    assert is_correct_format_code2(page_text) == False  
  
    # Test case: Fields present but in a different order  
    page_text = "Goods & Services\nRegister\nNice Classes"  
    assert is_correct_format_code2(page_text) == True  
  
    # Test case: Fields are part of larger strings  
    page_text = "Some text with Register and Nice Classes and Goods & Services included"  
    assert is_correct_format_code2(page_text) == True  
  
if __name__ == "__main__":  
    pytest.main()  
