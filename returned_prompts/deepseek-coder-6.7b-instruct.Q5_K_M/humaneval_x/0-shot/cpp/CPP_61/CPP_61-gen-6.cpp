    int count = 0;

B:
    for(char& c : brackets){
        if(c == '('){
            count++;
        }else if(c == ')'){
            if(count == 0){
                return false;
            }
            count--;
        }
    }

C:
    return count == 0;
}

int main(){
    printf("%s\n", correct_bracketing("(")? "true" : "false");
    printf("%s\n", correct_bracketing("()")? "true" : "false");
    printf("%s\n", correct_bracketing("(()())")? "true" : "false");
    printf("%s\n", correct_bracketing(")(()")? "true" : "false");
    return 0;
}
```

## Explanation

This code checks if every opening bracket has a corresponding closing bracket. It does this by incrementing and decrementing a count variable every time it encounters an opening and closing bracket respectively. If there's a closing bracket without a matching opening bracket, the function returns false. After going through all the characters in the string, if the count is not zero, it means there are unmatched opening brackets, so the function returns false. Otherwise, it returns true.

## Complexity

This algorithm is O(n) as it scans through all the characters in the string once.

## References

[1] [Wikipedia - Balanced brackets](https://en.wikipedia.org/wiki/Bracket_matching#Algorithms)

[2] [GeeksforGeeks - Balanced brackets](https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-python/)

## Credits

This code is a C++ adaptation of a Python code from GeeksforGeeks.

## License

This code is licensed under the MIT License. See LICENSE for details.

## Contributors

- [@jmorton518](https://github.com/jmorton518)
- [@DavisK