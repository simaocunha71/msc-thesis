def snake_to_camel(snake_string):
    camel_string = ""
    for i in range(len(snake_string)):
        if i == 0:
            camel_string += snake_string[i].upper()
        elif snake_string[i] == "_":
            camel_string += snake_string[i+1].upper()
        else:
            camel_string += snake_string[i]
    return camel_string
snake_string = "ruby_on_rails"
camel_string = snake_to_camel(snake_string)