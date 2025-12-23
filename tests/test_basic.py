"""tests/test_basic.py"""
from indian_address_parser.tokenizer import tokenize

def test_tokenizer_basic():
    """token tests"""
    text = "H No 12, Sector-5, Noida 201301"
    tokens = tokenize(text)

    assert "Noida" in tokens
    assert "201301" in tokens
    assert "-" in tokens
