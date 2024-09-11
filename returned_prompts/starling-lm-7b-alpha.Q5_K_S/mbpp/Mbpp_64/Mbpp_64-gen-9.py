def subject_marks(lst):
    return sorted(lst, key = lambda x: x[1])

# Test
def test_subject_marks():
    assert subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])==[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
    print("All Tests Passed")

test_subject_marks()


# Time complexity: O(nlogn)
# Space complexity: O(1)
# Here we used the built-in function sorted() to sort the list of tuples.
# We passed lambda function as the key to the sorted() function to sort the tuples based on the second element of the tuple.
# The time complexity of the sorted() function is O(nlogn) and the space complexity is O(1).

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```