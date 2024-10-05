    string result;
    for(int i=0;i<str.length();i++)
    {
        if(islower(str[i]))
        {
            result += toupper(str[i]);
        }
        else
        {
            result += tolower(str[i]);
        }
    }
    return result;
}
```
The above questions are related to C++ and the provided code is the solution to these questions. The first question checks if there are any two numbers in a given vector that are closer than a given threshold. The second question separates a string containing nested parentheses into separate strings. The third question truncates a floating point number into its integer and decimal parts, and the fourth question flips the case of a given string from lowercase to uppercase and vice versa. The code uses various C++ standard library functions and operators to solve these problems.