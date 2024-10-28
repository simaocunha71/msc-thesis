def text_match_two_three(text: str) -> bool:
    return re.match(r"a.*bb{2,3}$", text) is not None