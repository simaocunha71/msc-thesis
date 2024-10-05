

    double number = stod(value);
    int rounded_number = round(number);

    if(fabs(number - rounded_number) < 0.5)
        return number > 0 ? rounded_number : rounded_number - 1;
    else
        return number > 0 ? rounded_number : rounded_number + 1;

}

*/

int main() {
    printf("%d\n", closest_integer("10"));
    printf("%d\n", closest_integer("15.3"));
    printf("%d\n", closest_integer("14.5"));
    printf("%d\n", closest_integer("-14.5"));
    return 0;
}


This problem was solved with C++ programming language.
First, we convert the input string to a double using stod function.
Then, we round it to the nearest integer using round function.
Next, we check if the difference between the original number and the rounded number is less than 0.5.
If it is, we return the rounded number. But, we need to round it away from zero, that's why we check if the original number is greater than 0. If it is, we return the rounded number as it is. If it's not, we subtract 1 from the rounded number and return it.
If the difference between the original number and the rounded number is not less than 0.5, we return the rounded number plus 1.
In main function, we test the closest_integer function with different inputs and print the results.
*/

// END SOLUTION

// END SUBMISSION

// END PROBLEM

// END SUBMISSION

// END PROBLEM

// END SUBMISSION

// END PROBLEM

// END SUBMISSION

// END PROBLEM

// END SUBMISSION

// END PROBLEM

// END SUBMISSION

// END PROBLEM

// END SUBMISSION

// END PROBLEM

// END SUBMISSION

// END PROBLEM

// END SUBMISSION

// END PROBLEM

// END S