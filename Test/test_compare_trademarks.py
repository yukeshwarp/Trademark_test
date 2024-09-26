import pytest  
from unittest.mock import patch, MagicMock  
from openai import AzureOpenAI
# Import the function to be tested  
from main_app import compare_trademarks2  

@patch('openai.AzureOpenAI')  
def test_compare_trademarks2(mock_azure_openai):  
    # Mocking the AzureOpenAI client  
    mock_client = MagicMock()  
    mock_response = MagicMock()  
    mock_response.choices = [  
        MagicMock(message=MagicMock(content="Reasoning for Conflict: Test reasoning.\n- Conflict Grade: Name-Match"))  
    ]  
    mock_client.chat.completions.create.return_value = mock_response  
    mock_azure_openai.return_value = mock_client  

    existing_trademark = {  
        'trademark_name': 'SCOOPT\'D',  
        'status': 'Registered',  
        'owner': 'Example Owner',  
        'international_class_number': [30],  
        'serial_number': '123456',  
        'registration_number': '7891011',  
        'design_phrase': 'Example Design Phrase'  
    }  
    proposed_name = 'SCOOP-A-PALOOZA'  
    proposed_class = '30'  
    proposed_goods_services = 'Ice cream'  

    expected_output = {  
        'Trademark name': 'SCOOPT\'D',  
        'Trademark status': 'Registered',  
        'Trademark owner': 'Example Owner',  
        'Trademark class Number': [30],  
        'Trademark serial number': '123456',  
        'Trademark registration number': '7891011',  
        'Trademark design phrase': 'Example Design Phrase',  
        'conflict_grade': 'Name-Match',  
        'reasoning': 'Test reasoning.\n- Conflict Grade: Name-Match'  
    }  

    actual_output = compare_trademarks2(existing_trademark, proposed_name, proposed_class, proposed_goods_services)  
    print(actual_output)
    print(expected_output)
    assert actual_output == expected_output  

if __name__ == "__main__":  
    pytest.main()  
