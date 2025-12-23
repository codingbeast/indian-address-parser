"""indian_address_parser/parser.py"""

from .schema import SCHEMA

def parse(address: str) -> dict:
    """
    Parse an Indian address into structured fields.
    """
    result = SCHEMA.copy()
    result["raw"] = address  # optional, can remove later
    return result
