    if (a == round(a) && b == round(b) && c == round(c)) {
        if (a == b + c || a == c + b || b == a + c || b == c + a || c == a + b || c == b + a) {
            return true;
        }
    }
    return false;
}

int main()
{
    printf("%d\n", any_int(5,2,7));
    printf("%d\n", any_int(3,2,2));
    printf("%d\n", any_int(3,-2,1));
    printf("%d\n", any_int(3.6,-2.2,2));
    return 0;
}
*/



**Explanation:**

The problem is asking to create a function that takes three numbers as input and returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers. Otherwise, it returns false.

The given solution uses the `round` function from the `math.h` library to check if the numbers are integers. This function returns the nearest integer to the given number. If the given number is already an integer, `round` will return the same number.

The function `any_int` first checks if all the input numbers are integers by comparing them with their rounded values. If they are integers, it then checks if one of the numbers is equal to the sum of the other two. If it finds such a case, it returns true. Otherwise, it returns false.

The `main` function tests the `any_int` function with different inputs and prints the results.