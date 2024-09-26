import pytest  
from typing import List  
  
def parse_international_class_numbers(class_numbers: str) -> List[int]:  
    numbers = class_numbers.split(',')  
    return [int(num.strip()) for num in numbers if num.strip().isdigit()]  
  
def test_parse_international_class_numbers():  
    # Test with a typical input  
    input_data = "1, 2, 3, 4, 5"  
    expected_output = [1, 2, 3, 4, 5]  
    assert parse_international_class_numbers(input_data) == expected_output  
  
    # Test with extra spaces  
    input_data = "  10, 20 , 30 , 40, 50  "  
    expected_output = [10, 20, 30, 40, 50]  
    assert parse_international_class_numbers(input_data) == expected_output  
  
    # Test with non-numeric values  
    input_data = "1, a, 2, b, 3"  
    expected_output = [1, 2, 3]  
    assert parse_international_class_numbers(input_data) == expected_output  
  
    # Test with empty string  
    input_data = ""  
    expected_output = []  
    assert parse_international_class_numbers(input_data) == expected_output  
  
    # Test with a string that has only non-numeric values  
    input_data = "a, b, c"  
    expected_output = []  
    assert parse_international_class_numbers(input_data) == expected_output  
  
    # Test with mixed valid and invalid numeric strings  
    input_data = "1, -2, 3, 4.5, 5"  
    expected_output = [1, 3, 5]  
    assert parse_international_class_numbers(input_data) == expected_output  
  
if __name__ == "__main__":  
    pytest.main()  
