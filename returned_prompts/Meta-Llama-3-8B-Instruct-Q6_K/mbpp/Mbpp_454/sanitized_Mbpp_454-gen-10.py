def text_match_wordz(text: str) -> bool:
    return 'z' in text.lower() and text.lower().endswith('z') or text.lower().endswith('z.') or text.lower().endswith('z,')