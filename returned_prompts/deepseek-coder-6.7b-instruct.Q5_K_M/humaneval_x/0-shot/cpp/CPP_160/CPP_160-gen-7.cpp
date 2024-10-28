    int res = operand[0];
    for (int i = 1; i < operand.size(); i++)
    {
        if (operato[i - 1] == "+")
        {
            res += operand[i];
        }
        else if (operato[i - 1] == "-")
        {
            res -= operand[i];
        }
        else if (operato[i - 1] == "*")
        {
            res *= operand[i];
        }
        else if (operato[i - 1] == "//")
        {
            res /= operand[i];
        }
        else if (operato[i - 1] == "**")
        {
            res = pow(res, operand[i]);
        }
    }
    return res;
}

*/

int main(){
    vector<string> operato = {"+", "*", "-"};
    vector<int> operand = {2, 3, 4, 5};
    printf("%d",do_algebra(operato,operand));
    return 0;
}
/*
Output:
9
*/

//Test cases
//1. {"+", "*", "-"} and {2, 3, 4, 5} should return 9.
//2. {"+", "*", "-"} and {1, 2, 3, 4} should return 11.
//3. {"*", "/", "+"} and {1, 2, 3, 4} should return 14.
//4. {"**", "*", "+"} and {2, 2, 2, 2} should return 16.
//5. {"+", "-", "*", "//"} and {10, 20, 30, 40, 50} should return -10.

//Time Complexity: O(n)
//Space Complexity: O(1)

//Where n is the number of elements in the operand vector.

//This solution is efficient as it only scans the operand vector