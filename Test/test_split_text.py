import pytest  
from typing import List  
  
def split_text(text: str, max_tokens: int = 1500) -> List[str]:  
    chunks = []  
    current_chunk = []  
    current_length = 0  
    for line in text.split('\n'):  
        line_length = len(line.split())  
        if current_length + line_length > max_tokens:  
            chunks.append('\n'.join(current_chunk))  
            current_chunk = [line]  
            current_length = line_length  
        else:  
            current_chunk.append(line)  
            current_length += line_length  
    if current_chunk:  
        chunks.append('\n'.join(current_chunk))  
    return chunks  
  
def test_split_text():  
    text = ("This is a sample text. " * 1000).strip()  
    max_tokens = 1500  
      
    chunks = split_text(text, max_tokens)  
      
    # Check that the chunks are not empty  
    assert len(chunks) > 0  
      
    for chunk in chunks[:-1]:  
        # Check that each chunk has at most max_tokens words  
        assert len(chunk.split()) <= max_tokens  
  
    # Check that the combined length of all chunks is the same as the original text  
    combined_text = '\n'.join(chunks)  
    assert len(combined_text.split()) == len(text.split())  
  
def test_split_text_with_small_max_tokens():  
    text = "This is a test.\n" * 10  
    max_tokens = 3  
      
    chunks = split_text(text, max_tokens)  
      
    # Check that the chunks are not empty  
    assert len(chunks) > 0  
      
    for chunk in chunks[:-1]:  
        # Check that each chunk has at most max_tokens words  
        assert len(chunk.split()) <= max_tokens  
  
    # Check that the combined length of all chunks is the same as the original text  
    combined_text = '\n'.join(chunks)  
    assert len(combined_text.split()) == len(text.split())  
  
if __name__ == "__main__":  
    pytest.main()  
