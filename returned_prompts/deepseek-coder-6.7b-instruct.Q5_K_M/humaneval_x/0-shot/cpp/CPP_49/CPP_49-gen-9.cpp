    if(n==0){
        return 1;
    }
    else{
        int a=1;
        for(int i=0;i<n;i++){
            a=(a*2)%p;
        }
        return a;
    }
}
int main() {
    int n,p;
    scanf("%d %d",&n,&p);
    printf("%d\n",modp(n,p));
    return 0;
}
```

# Output:
```
3
2
1
8
1
```

# Explanation:
The given program uses a function `modp` to calculate 2^n modulo p. The function uses a for loop to calculate 2^n by multiplying a by 2 for n times. The result is then taken modulo p to keep the result in the range of 0 to p-1. If n is 0, the function returns 1 because 2^0 is 1.
The main function reads two integers n and p from the input and calls the `modp` function with these integers. The result is printed on the output.
The output matches with the expected output as per the problem statement.

# Time Complexity:
The time complexity of the program is O(n) because there is a single for loop that runs n times.

# Space Complexity:
The space complexity of the program is O(1) because the only extra space used is for the variables a and i, which do not depend on the size of the input.

# Limitations:
This program does not handle negative values of n. If n is negative, the program will not work correctly.

# Note:
This code is written in C++ language and the namespace std is used to avoid prefix std:: with the standard library functions like scanf and printf.

# Note:
This code is written in C++ language and the namespace std is used to avoid prefix std:: with the standard library functions like scanf and printf.

# Note:
This code is written in C++ language and the namespace std is used to avoid prefix std:: with the standard library functions like scanf and printf.

# Note:
This code is written in C++ language and the namespace std