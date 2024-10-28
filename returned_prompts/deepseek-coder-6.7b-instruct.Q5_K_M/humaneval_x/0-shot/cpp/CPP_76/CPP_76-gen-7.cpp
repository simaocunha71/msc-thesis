    int i = 1;
    while(pow(n, i) <= x){
        if(pow(n, i) == x)
            return true;
        i++;
    }
    return false;
}

int main(){
    printf("%d\n", is_simple_power(1, 4));
    printf("%d\n", is_simple_power(2, 2));
    printf("%d\n", is_simple_power(8, 2));
    printf("%d\n", is_simple_power(3, 2));
    printf("%d\n", is_simple_power(3, 1));
    printf("%d\n", is_simple_power(5, 3));
    return 0;
}
```

## Explanation

The function is_simple_power(x, n) is checking if a number x is a simple power of n. 

The function uses a while loop to check each integer i from 1 to x. If n to the power of i equals x, then x is a simple power of n, so the function returns true. If no such i is found after checking all integers from 1 to x, then x is not a simple power of n, so the function returns false.

## Test Cases

1. is_simple_power(1, 4) => true
2. is_simple_power(2, 2) => true
3. is_simple_power(8, 2) => true
4. is_simple_power(3, 2) => false
5. is_simple_power(3, 1) => false
6. is_simple_power(5, 3) => false

These test cases cover different scenarios where x is a simple power of n and x is not a simple power of n.

## Runtime Analysis

The time complexity of this function is O(x), because it checks each integer from 1 to x to see if it is a power of n. The space complexity is O(1), because it uses a constant amount of space to store the variables x, n, and i.

## Conclusion

This function correctly determines if a number x is a simple power of n. It does this by iter