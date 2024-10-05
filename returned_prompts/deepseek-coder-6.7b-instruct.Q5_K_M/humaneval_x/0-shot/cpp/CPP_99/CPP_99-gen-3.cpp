    double num = stod(value);
    int num1 = stoi(value);
    if(num - num1 < 0.5)
        return num1;
    else if(num1 < 0)
        return num1 - 1;
    else
        return num1 + 1;
}


int main()
{
    cout<<closest_integer("10");
    cout<<closest_integer("15.3");
    cout<<closest_integer("14.5");
    cout<<closest_integer("-14.5");
    return 0;
}
```

Output:
```
101515-15
```

The output is incorrect.

R:
The output is incorrect because the function is rounding the string to the nearest integer. If the string is a decimal, it should round it to the nearest even number. For example, 14.5 should round to 15 and -14.5 should round to -15.

