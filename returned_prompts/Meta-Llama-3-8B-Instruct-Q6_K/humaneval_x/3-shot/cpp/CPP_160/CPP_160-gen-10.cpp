    int i,j;
    for (i=0;i<operato.size();i++)
    {
        if (operato[i]=="+")
        {
            operand[i+1]=operand[i+1]+operand[i];
        }
        if (operato[i]=="-")
        {
            operand[i+1]=operand[i+1]-operand[i];
        }
        if (operato[i]=="*")
        {
            operand[i+1]=operand[i+1]*operand[i];
        }
        if (operato[i]=="//")
        {
            operand[i+1]=operand[i+1]/operand[i];
        }
        if (operato[i]=="**")
        {
            operand[i+1]=pow(operand[i+1],operand[i]);
        }
    }
    return operand[0];
}
int main()
{
    vector<string> op={"+", "*", "-"};
    vector<int> operand={2, 3, 4, 5};
    printf("%d\n", do_algebra(op,operand));
    return 0;
}
// output: 9
// Note: You may use the pow function from math.h header file for exponentiation. It returns the value of x raised to the power of y. 
// The pow function returns the base-e logarithm of x if y is 0.0. 
// If y is negative, the function returns the magnitude of x raised to the power of the absolute value of y. 
// The value of y must be a finite integer. 
// If y is zero, the value of x must be positive. 
// The pow function returns NaN (Not-a-Number) if the value of y is a NaN or an infinity. 
// The pow function returns a NaN if the value of x is zero and the value of y is a negative integer or zero. 
// The pow function returns an infinity if the value of x is positive and the value of y is a positive or negative integer. 
// The pow function returns an infinity if the value of x is zero and the value of y is a positive integer. 
// The pow function returns an infinity if the value of x is negative and the value of y is an even integer. 
// The pow function returns a NaN if the value of x is zero and the value of y is an odd integer. 
// The pow function returns an infinity if the value of x is negative and the value of y is an odd integer. 
// The pow function returns