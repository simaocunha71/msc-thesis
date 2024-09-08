    int n=operato.size();
    if(n<1 || n>=operand.size()-1)
    {
        printf("Invalid Input\n");
        return -1;
    }
    int res=operand[0];
    for(int i=1;i<=n;i++)
    {
        if(operato[i-1]=="+"&&i<n)
        {
            res+=operand[i];
        }
        else if(operato[i-1]=="-"&&i<n)
        {
            res-=operand[i];
        }
        else if(operato[i-1]=="*"&&i<n)
        {
            res*=operand[i];
        }
        else if(operato[i-1]=="//")
        {
            res=res/operand[i];
        }
        else if(operato[i-1]=="**")
        {
            res=pow(res,operand[i]);
        }
    }
    return res;
}
int main()
{
    vector<string> operato={"+", "*", "-"};
    vector<int> operand={2, 3, 4, 5};
    int result = do_algebra(operato, operand);
    printf("The result is %d\n", result);
    return 0;
}

