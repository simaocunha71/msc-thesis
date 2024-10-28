def text_match_two_three(text: str) -> bool:
    return re.search(r'a{1}b{2,3}',text) is not None

