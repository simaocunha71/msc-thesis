If n is greater than m, return "-1".

B:
Calculate the average of n and m, round it to the nearest integer, and store it in the variable 'avg'.

C:
Convert the integer 'avg' to binary by repeatedly dividing by 2 and storing the remainder in a string 'binary'.

D:
Return the string 'binary'.
*/

int main()
{
    int n, m;
    scanf("%d %d", &n, &m);
    printf("%s", rounded_avg(n, m).c_str());
    return 0;
}
/*
Test cases:
Input: 1 5
Output: 11

Input: 7 5
Output: -1

Input: 10 20
Output: 1111

Input: 20 33
Output: 11010
*/
```

### Complexity Analysis

The time complexity of this program is O(log(m)) because it converts the average to binary, which involves repeatedly dividing by 2. The space complexity is also O(log(m)) because the string 'binary' stores the binary representation of the average.

### Explanation

This program calculates the average of two numbers and rounds it to the nearest integer. If the input numbers are in descending order, it returns "-1". Otherwise, it converts the rounded average to binary and returns it as a string.

To calculate the average of two numbers, it adds them and then divides by 2. It uses the floor function to round down the result to the nearest integer.

To convert the average to binary, it repeatedly divides the average by 2 and stores the remainder in a string. It does this in a loop until the average becomes 0. The