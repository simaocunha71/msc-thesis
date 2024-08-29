def snake_to_camel(s):
    words = s.split('_')
    return ''.join(word.capitalize() for word in words)

print(snake_to_camel('python_program'))



