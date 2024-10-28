def snake_to_camel(snake_str):
    # Split the string by underscores
    split_str = snake_str.split('_')
    # Convert the first letter of each word to uppercase
    camel_str = split_str[0].upper()
    for i in range(1, len(split_str)):
        camel_str += split_str[i].capitalize()
    return camel_str