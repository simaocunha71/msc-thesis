
def snake_to_camel(snake: str) -> str:
    result = snake[0].upper() + snake[1:]
    for i in range(1,len(snake)):
        if snake[i] == '_':
            result += snake[i+1].upper()
    return result


