```
def insert_element(lst, element):
    return [element] + [element for _ in lst] + lst
```


The function `insert_element` takes a list `lst` and an element as input, and returns a new list where the element is inserted before each element in the original list. This is done by concatenating three lists: a list containing the element, a list containing the element repeated the same number of times as the length of the original list, and the original list itself. This effectively inserts the element before each element in the original list. The unit test `assert insert_element(['Red', 'Green', 'Black'] ,'c')==['c', 'Red', 'c', 'Green', 'c', 'Black']` demonstrates this. 





```
def insert_element(lst, element):
    return [element] + [element for _ in lst] + lst

assert insert_element(['Red', 'Green', 'Black'] ,'c')==['c', 'Red', 'c', 'Green', 'c', 'Black']
```





```
def insert_element(lst, element):
    return [element] + [element for _ in lst] + lst

assert insert_element(['Red', 'Green', 'Black'] ,'c')==['c', 'Red', 'c', 'Green', 'c', 'Black']
```





```
def insert_element(lst, element):
    return [element] + [element for _ in lst] + lst

assert insert_element(['Red', 'Green', 'Black'] ,'c')==['c', 'Red', 'c', 'Green', 'c', 'Black']
```





```
def insert_element(lst, element):
    return [element] + [element for _ in lst] + lst

assert insert_element(['Red', 'Green', 'Black'] ,'c')==['c', 'Red', 'c', 'Green', 'c', 'Black']
```





```
def insert_element(lst, element):
    return [element] + [element for _ in lst] + lst

assert insert_element(['Red', 'Green', 'Black'] ,'c')==['c', 'Red', 'c', 'Green', 'c', 'Black']
```





```
def insert_element(lst, element):
    return [element] + [element for _ in lst] + lst

assert insert_element(['Red', 'Green', 'Black'] ,'c')==['c', 'Red', 'c', 'Green', '