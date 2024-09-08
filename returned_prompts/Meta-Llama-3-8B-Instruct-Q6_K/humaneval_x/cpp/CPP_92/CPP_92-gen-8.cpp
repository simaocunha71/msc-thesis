    if(a+b==c || a+c==b || b+c==a)
    {
        if(a==round(a) && b==round(b) && c==round(c))
        {
            return true;
        }
    }
    return false;
}
int main()
{
    printf("%d\n",any_int(5,2,7)); //returns 1
    printf("%d\n",any_int(3,2,2)); //returns 0
    printf("%d\n",any_int(3,-2,1)); //returns 1
    printf("%d\n",any_int(3.6,-2.2,2)); //returns 0
    return 0;
}
/*Output:
1
0
1
0*/
*/

Explanation:
The task is to create a function that takes three numbers as input and checks if one of the numbers is equal to the sum of the other two. The function should return true if all numbers are integers and this condition is met, and false otherwise.

The function `any_int` is defined to take three floating-point numbers as input. It first checks if one of the numbers is equal to the sum of the other two using the conditions `a+b==c`, `a+c==b`, and `b+c==a`. If any of these conditions is met, it then checks if all numbers are integers by comparing them with their rounded values using the `round` function. If all numbers are integers, the function returns true; otherwise, it returns false.

In the `main` function, we test the `any_int` function with four different sets of input numbers and print the output. The output is as expected, with the function returning 1 (true) for the first, third, and fourth inputs, and 0 (false) for the second input.