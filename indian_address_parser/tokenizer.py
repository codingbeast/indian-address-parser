"""indian_address_parser/tokenizer.py"""
import regex as re

# Precompiled for speed (module load time)
_TOKEN_RE = re.compile(
    r"\p{L}+|\p{N}+|[^\s\p{L}\p{N}]",
    re.UNICODE,
)

def tokenize(text: str) -> list[str]:
    """
    Tokenize address string into stable tokens.
    Unicode-safe and fast.
    """
    if not text:
        return []
    return _TOKEN_RE.findall(text)
