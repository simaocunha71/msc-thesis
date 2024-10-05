    int res = operand[0];
    for(int i=0; i<operato.size(); i++)
    {
        if(operato[i] == "+")
            res += operand[i+1];
        else if(operato[i] == "-")
            res -= operand[i+1];
        else if(operato[i] == "*")
            res *= operand[i+1];
        else if(operato[i] == "//")
            res /= operand[i+1];
        else if(operato[i] == "**")
            res = pow(res, operand[i+1]);
    }
    return res;
}
int main(){
    vector<string> operato = {"+", "*", "-"};
    vector<int> operand = {2, 3, 4, 5};
    printf("%d", do_algebra(operato, operand));
    return 0;
}
*/
// Solution:
// The solution is to iterate through the given operator array and apply the corresponding operation on the operand array.
// The operation to be performed is determined by the operator. If the operator is "+", then add the next operand to the result. 
// If the operator is "-", then subtract the next operand from the result. If the operator is "*", then multiply the result by the next operand. 
// If the operator is "//", then divide the result by the next operand. If the operator is "**", then raise the result to the power of the next operand.
// The result is updated at each step and returned at the end.
// This solution has a time complexity of O(n), where n is the length of the operator array.

// The main function is used to test the do_algebra function. It creates two vectors, one for operators and one for operands, and calls the do_algebra function with these vectors.
// The result is printed to the console.
// The main function does not return a value.

// The do_algebra function takes two vectors as arguments. The first vector is a vector of strings that represent the operators. 
// The second vector is a