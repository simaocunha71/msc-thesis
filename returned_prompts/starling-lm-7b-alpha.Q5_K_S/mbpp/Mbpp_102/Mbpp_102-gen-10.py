def snake_to_camel(snake):
    return "".join(word.title() for word in snake.split("_"))

# assert snake_to_camel('python_program')=='PythonProgram'

def test_snake_to_camel():
    assert snake_to_camel('python_program')=='PythonProgram'
    assert snake_to_camel('this_is_a_test')=='ThisIsATest'
    assert snake_to_camel('this_is_another_test')=='ThisIsAnotherTest'

# test_snake_to_camel()

def snake_to_camel_v2(snake):
    return ''.join(w.capitalize() for w in snake.split("_"))

# assert snake_to_camel_v2('python_program')=='PythonProgram'

def test_snake_to_camel_v2():
    assert snake_to_camel_v2('python_program')=='PythonProgram'
    assert snake_to_camel_v2('this_is_a_test')=='ThisIsATest'
    assert snake_to_camel_v2('this_is_another_test')=='ThisIsAnotherTest'

# test_snake_to_camel_v2()

def snake_to_camel_v3(snake):
    return "".join(map(lambda word: word.capitalize(), snake.split("_")))

# assert snake_to_camel_v3('python_program')=='PythonProgram'

def test_snake_to_camel_v3():
    assert snake_to_camel_v3('python_program')=='PythonProgram'
    assert snake_to_camel_v3('this_is_a_test')=='ThisIsATest'
    assert snake_to_camel_v3('this_is_another_test')=='ThisIsAnotherTest'

# test_snake_to_camel_v3()

def snake_to_camel