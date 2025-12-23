"""indian_address_parser/features.py"""

def extract_features(tokens: list[str], i: int) -> list[str]:
    """extract features"""
    t = tokens[i]
    feats = [
        f"w={t}",
        f"l={t.lower()}",
        f"is_digit={t.isdigit()}",
        f"is_upper={t.isupper()}",
        f"has_digit={any(c.isdigit() for c in t)}",
        f"prefix2={t[:2]}",
        f"suffix2={t[-2:]}",
    ]

    if i > 0:
        prev = tokens[i - 1]
        feats.append(f"prev_w={prev.lower()}")
    else:
        feats.append("BOS")

    if i < len(tokens) - 1:
        nxt = tokens[i + 1]
        feats.append(f"next_w={nxt.lower()}")
    else:
        feats.append("EOS")

    return feats
