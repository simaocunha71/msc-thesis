def parse_nested_parens(paren_string):
    return [
        len(list(group))
        for group in re.findall(r"\((?:[^()]|\([^()]*\))*\)", paren_string)
    ]