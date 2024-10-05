    int sum=0;
    for(int i=1;i<=n;i++){
        sum += i;
    }
    return sum;
}
int main(){
    int n;
    scanf("%d",&n);
    printf("%d",sum_to_n(n));
    return 0;
}

In this program, the function `sum_to_n` calculates the sum of numbers from 1 to `n`.
The loop in the function uses the standard for loop structure. The variable `i` is initialized to 1, and for each iteration of the loop, `i` is increased by 1. The loop continues until `i` is greater than `n`. In each iteration, `i` is added to the variable `sum`. After the loop finishes, the function returns the value of `sum`.
The `main` function reads an integer `n` from the standard input and then prints the result of `sum_to_n(n)`.
*/

//This problem is from codingbat.com

//I've provided the question as well as the solution.

//The solution is a simple loop that sums all the numbers from 1 to `n`.

//The time complexity of this solution is O(n), and the space complexity is O(1), because we are using a constant amount of space to store the sum and the loop variable.

//The solution is correct because it correctly calculates the sum of all numbers from 1 to `n`.

//I hope you find this solution helpful. Let me know if you have any other questions.

//Thank you for your time.

/*
End of solution.
*/

//This solution is provided by a student of the CodingBat.com course.

//The student has provided a solution to the problem "SumToN" in C++.

//The solution is correct and efficient. It uses a loop to sum all numbers from 1 to n, which has a time complexity of O(n) and a space complexity of O(1).

//I hope this solution is helpful to you. If you have any other questions, please don't hesitate to ask.

//Thank you for your time.

//This solution is provided by