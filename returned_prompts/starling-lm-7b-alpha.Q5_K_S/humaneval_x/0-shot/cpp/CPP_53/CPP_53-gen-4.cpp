    if(y == 0)
        return x;
    else
        return add(x^y, (x&y)<<1);
}
int main(){
    int x = 2;
    int y = 3;
    printf("%d",add(x,y));
    return 0;
}


ANSWER:
The time complexity of the above function is O(logn).

The add(x,y) function uses bitwise operations to add two numbers. The recursive function is implemented as follows:

The function takes two parameters x and y. Here, x is the bitwise XOR of the two numbers and y is the bitwise AND of the two numbers. The function returns the sum of the two numbers.

In the function, if y is 0, it means there are no more bits to add, and the function returns x.

If y is not 0, the function uses the following steps to add the bits:

x^y: This operation is the bitwise XOR of the two numbers. It calculates the sum of the two numbers without considering the carry.
(x&y)<<1: This operation is the bitwise AND of the two numbers, and then it is left-shifted by 1. It calculates the carry of the two numbers.
The function then calls itself recursively with the updated values of x and y, and returns the sum of the two numbers.

The time complexity of the function is O(logn), where n is the number of bits in the larger number. This is because in each recursive call, the function reduces the number of bits to be added by half.

In the given code, the function is called with x = 2 and y = 3. The function will perform the following steps:

In the first recursive call, x = 2 and y = 3. Since y is not 0, the function will call itself with x = 10 (2^1 XOR 3) and y = 3.
In the second recursive call, x = 10 and y = 3. Since y is not 0, the function will call itself with x = 11 (10 XOR 3) and y = 0.
In the third recursive call, x = 