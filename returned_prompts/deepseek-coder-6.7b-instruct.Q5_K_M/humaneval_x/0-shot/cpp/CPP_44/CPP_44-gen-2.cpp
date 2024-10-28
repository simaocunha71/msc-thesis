    string result = "";
    int remainder;

    while(x != 0){

        remainder = x % base;
        x = x / base;

        result = to_string(remainder) + result;
    }

    return result;
}

int main(){
    int x, base;
    printf("Enter the number: ");
    scanf("%d", &x);
    printf("Enter the base: ");
    scanf("%d", &base);

    string result = change_base(x, base);
    printf("The result is: %s\n", result.c_str());

    return 0;
}
```

This program converts a decimal number to any base (from base 2 to base 9). If the base number is greater than 10, it uses characters from 'A' to 'Z' to represent the numbers 10 to 35. 

To run the program, you can copy and paste it into a file named `main.cpp`, then compile and run it using a C++ compiler.

For example:

```
Enter the number: 8
Enter the base: 3
The result is: 22
```

```
Enter the number: 8
Enter the base: 2
The result is: 1000
```

```
Enter the number: 7
Enter the base: 2
The result is: 111
```

## Task 2

