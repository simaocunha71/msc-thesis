    int i;
    double result=operand[0];
    for (i=1;i<operand.size();i++)
    {
        if (operato[i-1]=="+" )
        {
            result+=operand[i];
        }
        else if (operato[i-1]=="-" )
        {
            result-=operand[i];
        }
        else if (operato[i-1]=="*" )
        {
            result*=operand[i];
        }
        else if (operato[i-1]=="//")
        {
            result=double(result)/double(operand[i]);
        }
        else if (operato[i-1]=="**")
        {
            result=pow(double(result),double(operand[i]));
        }
    }
    return (int)result;
}
int main()
{
    vector<string> operato = {"+", "*", "-"};
    vector<int> operand = {2, 3, 4, 5};
    cout << do_algebra(operato, operand) << endl;
    return 0;
}
*/



