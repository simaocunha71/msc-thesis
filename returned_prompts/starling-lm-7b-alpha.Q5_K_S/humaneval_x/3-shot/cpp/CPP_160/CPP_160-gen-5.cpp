    int i;
    for (i=0;i<operato.size();i++)
    if (operato[i]=="+"||operato[i]=="-"||operato[i]=="*"||operato[i]=="//"||operato[i]=="**")
    break;
    int left=i;
    int right=i+1;
    while (right<operand.size())
    {
        if (operato[right]=="+"||operato[right]=="-"||operato[right]=="*"||operato[right]=="//"||operato[right]=="**")
        {
            i=right;
            right++;
        }
        else
        {
            right++;
        }
    }
    if (operato[left]=="+")
    return operand[left]+operand[right];
    if (operato[left]=="-")
    return operand[left]-operand[right];
    if (operato[left]=="*")
    return operand[left]*operand[right];
    if (operato[left]=="//")
    {
        int a=operand[left];
        int b=operand[right];
        int c=abs(a-b);
        if (a>=b)
        return a/b;
        else
        return b/a;
    }
    if (operato[left]=="**")
    {
        int a=operand[left];
        int b=operand[right];
        int c=pow(a,b);
        return c;
    }
}
int main(){
vector<string> operato={"+","-","*","//","**"};
vector<int> operand={2,3,4,5};
printf("%d\n",do_algebra(operato,operand));
}
























































