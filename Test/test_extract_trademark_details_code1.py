import pytest  
from unittest.mock import patch, MagicMock  
from main_app import extract_trademark_details_code1  # Replace 'main_app' with the actual module name where your function is defined.  
  
def test_extract_trademark_details_code1():  
    document_chunk = """Trademark Document Example  
    ---------------------------  
    Trademark name: ExampleTrademark  
    Status: Active  
    Serial number: 123456789  
    International class number: 25  
    Goods/Services: Clothing, footwear, headgear  
    Owner: ExampleOwner  
    ---------------------------  
    """  
      
    expected_result = {  
        "trademark_name": "ExampleTrademark",  
        "status": "Active",  
        "serial_number": "123456789",  
        "international_class_number": "25",  
        "goods_services": "Clothing, footwear, headgear",  
        "owner": "ExampleOwner"  
    }  
      
    # Mock the AzureOpenAI client and its response  
    with patch('openai.AzureOpenAI') as MockAzureOpenAI:  # Correctly patching the AzureOpenAI from the openai module  
        mock_client = MockAzureOpenAI.return_value  
        mock_response = MagicMock()  
        mock_response.choices = [MagicMock()]  
        mock_response.choices[0].message.content = """  
        trademark_name: ExampleTrademark  
        status: Active  
        serial_number: 123456789  
        international_class_number: 25  
        goods_services: Clothing, footwear, headgear  
        owner: ExampleOwner  
        """  
        mock_client.chat.completions.create.return_value = mock_response  
          
        result = extract_trademark_details_code1(document_chunk)  
          
        assert result == expected_result  
  
if __name__ == "__main__":  
    pytest.main()  

