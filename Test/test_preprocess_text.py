import re  
import pytest  
from main_app import preprocess_text  # Replace 'your_module' with the name of your Python file  
  
def test_preprocess_text():  
    # Test case: single space  
    assert preprocess_text("This  is   a    test.") == "This is a test."  
      
    # Test case: different dashes  
    assert preprocess_text("This–is—a test.") == "This-is-a test."  
  
    # Test case: leading and trailing spaces  
    assert preprocess_text("  This is a test.  ") == "This is a test."  
  
    # Test case: combination of spaces and dashes  
    assert preprocess_text("  This– is— a    test.  ") == "This- is- a test."  
  
    # Test case: no change needed  
    assert preprocess_text("This is a test.") == "This is a test."  
      
    # Edge case: empty string  
    assert preprocess_text("") == ""  
  
    # Edge case: string with only spaces  
    assert preprocess_text("     ") == ""  
  
if __name__ == "__main__":  
    pytest.main()  
