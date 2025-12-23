"""indian_address_parser/parser.py"""
from .schema import SCHEMA
from .tokenizer import tokenize

def parse(address: str) -> dict:
    """
    Parse an Indian address into structured fields.
    """
    result = SCHEMA.copy()
    if not address:
        return result
    tokens = tokenize(address) # TODO: implement this
    print(tokens)
    # ML will come later
    return result
