
def odd_values_string(input_str: str) -> str:
    output_str = ''
    for i, c in enumerate(input_str):
        if i % 2 == 0:
            output_str += c
    return output_str


