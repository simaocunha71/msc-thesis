    string result = "";
    while(x > 0){
        result = to_string(x%base) + result;
        x /= base;
    }
    return result;
}

int main(){
    printf("%s\n", change_base(8, 3).c_str());
    printf("%s\n", change_base(8, 2).c_str());
    printf("%s\n", change_base(7, 2).c_str());
    return 0;
}
```

Here is the explanation of the code:
In the `change_base` function, we repeatedly divide `x` by `base` and add the remainder to the beginning of our result string. We do this until `x` is 0. The `to_string` function is used to convert the integer remainder to a string.
The `main` function is used to test the `change_base` function.

This code will print:
```
22
1000
111
```
which are the base-3 and base-2 representations of the input number 8 and 7.
*/

// @lc code=end

// @lc code=start
/*
\*
