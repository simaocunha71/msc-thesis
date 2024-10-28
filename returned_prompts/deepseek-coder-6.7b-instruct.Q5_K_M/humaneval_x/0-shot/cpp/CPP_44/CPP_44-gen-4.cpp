    string result;
    int temp;
    while(x > 0){
        temp = x % base;
        result = to_string(temp) + result;
        x /= base;
    }
    return result;
}

int main(){
    printf("%s\n",change_base(8,3).c_str());
    printf("%s\n",change_base(8,2).c_str());
    printf("%s\n",change_base(7,2).c_str());
    return 0;
}
```

Output:
```
22
1000
111
```

## Python Version

```python
# Python Code

def change_base(x, base):
    result = ''
    temp = 0
    while x > 0:
        temp = x % base
        result = str(temp) + result
        x //= base
    return result

print(change_base(8, 3))
print(change_base(8, 2))
print(change_base(7, 2))
```

Output:
```
22
1000
111
```

## Conclusion

Both the Python and C++ versions of the problem solve the problem correctly. Both codes take in an integer `x` and a base `b`, convert `x` to base `b`, and return the result as a string. The Python version uses the `//` operator for integer division and Python's `str()` function to convert integers to strings. The C++ version uses `std::to_string()` function to convert integers to strings, and `%` operator for modulo operation.

## Time Complexity

The time complexity of both the Python and C++ solutions is O(log(n)) where n is the input number. This is because each digit of the number is processed exactly once, and the number of digits in a number is proportional to the logarithm of the number.

## Space Complexity

The space complexity of both the Python and C++ solutions is O(log(n)) as well. This is because the result string is created to hold the maximum number of digits, which is proportional to the logarithm of the