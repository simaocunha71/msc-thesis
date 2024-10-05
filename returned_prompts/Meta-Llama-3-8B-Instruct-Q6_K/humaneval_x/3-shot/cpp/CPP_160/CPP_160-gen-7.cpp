    int i;
    int j;
    int k;
    int temp;
    int res=operand[0];
    for (i=0;i<operato.size();i++)
    {
        if (operato[i]=="+")
        {
            res=res+operand[i+1];
        }
        else if (operato[i]=="-")
        {
            res=res-operand[i+1];
        }
        else if (operato[i]=="*")
        {
            res=res*operand[i+1];
        }
        else if (operato[i]=="//")
        {
            res=res/operand[i+1];
        }
        else if (operato[i]=="**")
        {
            res=pow(res, operand[i+1]);
        }
    }
    return res;
}
int main()
{
    vector<string> operato = {"+", "*", "-"};
    vector<int> operand = {2, 3, 4, 5};
    int result = do_algebra(operato, operand);
    printf("%d", result);
    return 0;
} 
*/



