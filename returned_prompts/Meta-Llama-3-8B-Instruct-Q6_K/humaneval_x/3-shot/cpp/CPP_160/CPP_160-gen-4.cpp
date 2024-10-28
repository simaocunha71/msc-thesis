    int i;
    for(i=0;i<operato.size();i++)
    {
        if(operato[i] == "+")
        {
            operand[i+1] = operand[i] + operand[i+1];
        }
        else if(operato[i] == "-")
        {
            operand[i+1] = operand[i] - operand[i+1];
        }
        else if(operato[i] == "*")
        {
            operand[i+1] = operand[i] * operand[i+1];
        }
        else if(operato[i] == "///")
        {
            operand[i+1] = operand[i] / operand[i+1];
        }
        else if(operato[i] == "**")
        {
            operand[i+1] = pow(operand[i], operand[i+1]);
        }
    }
    return operand.back();
}
int main()
{
    vector<string> op = {"+", "*", "-"};
    vector<int> opnd = {2, 3, 4, 5};
    int result = do_algebra(op, opnd);
    printf("%d\n", result);
    return 0;
}
*/



