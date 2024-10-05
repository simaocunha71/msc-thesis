    int i,j;
    vector<string>::iterator it;
    vector<int>::iterator itt;
    int result=operand[0];
    for (i=0;i<operato.size();i++)
    {
        it=find(operato.begin(), operato.end(), operato[i]);
        itt=find(operand.begin(), operand.end(), *it);
        if (operato[i]=="+" || operato[i]=="-")
        {
        if (operato[i]=="+")
            result+=*itt;
        if (operato[i]=="-")
            result-=*itt;
        }
        if (operato[i]=="*")
            result*=*itt;
        if (operato[i]=="//")
            result/=*itt;
        if (operato[i]=="**")
        {
        if (*itt==0)
            result=0;
        else if (*itt==1)
            result=result;
        else
        result=pow(result, *itt);
        }
    }
    return result;
}



