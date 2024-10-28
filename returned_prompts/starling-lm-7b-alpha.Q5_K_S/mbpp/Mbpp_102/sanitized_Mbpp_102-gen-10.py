def snake_to_camel(snake):
    return "".join(word.title() for word in snake.split("_"))