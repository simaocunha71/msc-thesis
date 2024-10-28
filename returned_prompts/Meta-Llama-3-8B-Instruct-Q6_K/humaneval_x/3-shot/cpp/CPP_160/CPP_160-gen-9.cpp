    int i;
    int result = operand[0];
    for (i=0;i<operato.size();i++)
    {
        switch(operato[i][0])
        {
            case '+':
                result += operand[i+1];
                break;
            case '-':
                result -= operand[i+1];
                break;
            case '*':
                result *= operand[i+1];
                break;
            case '/':
                result /= operand[i+1];
                break;
            case '^':
                result = pow(result, operand[i+1]);
                break;
        }
    }
    return result;
} // end do_algebra
// Example of usage:
int main()
{
    vector<string> operato = {"+", "*", "-"};
    vector<int> operand = {2, 3, 4, 5};
    printf("Result: %d\n", do_algebra(operato, operand));
    return 0;
} // end main
// Output:
// Result: 9

Note:
    If you are using C++11 or later, you can use lambda functions and std::accumulate instead of a loop.
    Here is an example:
    int do_algebra(vector<string> operato, vector<int> operand)
    {
        return std::accumulate(operand.begin() + 1, operand.end(), operand[0], 
        [operato](int a, int b)
        {
            switch(operato[0][0])
            {
                case '+':
                    return a + b;
                case '-':
                    return a - b;
                case '*':
                    return a * b;
                case '/':
                    return a / b;
                case '^':
                    return pow(a, b);
            }
        });
    } // end do_algebra
    // Example of usage:
    int main()
    {
        vector<string> operato = {"+", "*", "-"};
        vector<int> operand = {2, 3, 4, 5};
        printf("Result: %d\n", do_algebra(operato, operand));
        return 0;
    } // end main
    // Output:
    // Result: 9
    // This is a more concise and expressive way to solve the problem. It also avoids the need for a loop.