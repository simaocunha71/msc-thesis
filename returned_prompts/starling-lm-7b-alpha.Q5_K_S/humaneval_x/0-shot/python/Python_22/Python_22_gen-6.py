

def filter_integers(values: List[Any]) -> List[int]:
    integers = []
    for value in values:
        if isinstance(value, int):
            integers.append(value)
    return integers


# Other solutions:
# from typing import List, Any, Union
#
#
# def filter_integers(values: List[Union[int, Any]]) -> List[int]:
#     """ Filter given list of any python values only for integers
#     >>> filter_integers(['a', 3.14, 5])
#     [5]
#     >>> filter_integers([1, 2, 3, 'abc', {}, []])
#     [1, 2, 3]
#     """
#     return [x for x in values if isinstance(x, int)]

# from typing import List, Any, Union
#
#
# def filter_integers(values: List[Union[int, Any]]) -> List[int]:
#     """ Filter given list of any python values only for integers
#     >>> filter_integers(['a', 3.14, 5])
#     [5]
#     >>> filter_integers([1, 2, 3, 'abc', {}, []])
#     [1, 2, 3]
#     """
#     return [x for x in values if isinstance(x, (int,))]

# from typing import List, Any, Union
#
#
# def filter_integers(values: List[Union[int, Any]]) -> List[int]:
#     """ Filter given list of any python values only for integers
#     >>> filter_integers(['a', 3.14, 5])
#     [5]
#     >>> filter_integers([1, 2, 3, 'abc', {}, []])
#     [1, 2, 3]
#     """
#     return [value for value in values if isinstance(value, (int,))]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]