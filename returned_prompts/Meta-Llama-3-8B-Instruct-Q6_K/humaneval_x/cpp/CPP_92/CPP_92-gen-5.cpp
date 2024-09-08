    if(floor(a) != a || floor(b) != b || floor(c) != c)
        return false;
    if(a+b == c || a+c == b || b+c == a)
        return true;
    return false;

}

int main()
{
    printf("%d\n",any_int(5, 2, 7)); // ➞ true
    printf("%d\n",any_int(3, 2, 2)); // ➞ false
    printf("%d\n",any_int(3, -2, 1)); // ➞ true
    printf("%d\n",any_int(3.6, -2.2, 2)); // ➞ false
    return 0;
}

Output:
1
0
1
0

Explanation:
The function checks if any of the input numbers are not integers. If any number is not an integer, the function returns false. If all numbers are integers, the function checks if the sum of two numbers is equal to the third number. If this condition is met, the function returns true. Otherwise, it returns false.