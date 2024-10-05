    int i,j;
    for(i=0;i<operato.size();i++)
    {
        if(operato[i]=="+")
        {
            j=i+1;
            int sum=operand[j];
            while(j<operand.size()-1&&operato[j+1]=="+")
            {
                sum+=operand[j+2];
                j+=2;
            }
            operand.erase(operand.begin()+j+1,operand.end());
            operand[j]=sum;
        }
        else if(operato[i]=="-")
        {
            j=i+1;
            int sub=operand[j];
            while(j<operand.size()-1&&operato[j+1]=="-")
            {
                sub-=operand[j+2];
                j+=2;
            }
            operand.erase(operand.begin()+j+1,operand.end());
            operand[j]=sub;
        }
        else if(operato[i]=="*")
        {
            j=i+1;
            int mul=operand[j];
            while(j<operand.size()-1&&operato[j+1]=="*")
            {
                mul*=operand[j+2];
                j+=2;
            }
            operand.erase(operand.begin()+j+1,operand.end());
            operand[j]=mul;
        }
        else if(operato[i]=="//")
        {
            j=i+1;
            int div=operand[j];
            while(j<operand.size()-1&&operato[j+1]=="//")
            {
                div/=operand[j+2];
                j+=2;
            }
            operand.erase(operand.begin()+j+1,operand.end());
            operand[j]=div;
        }
        else if(operato[i]=="**")
        {
            j=i+1;
            int pow=operand[j];
            while(j<operand.size()-1&&operato[j+1]=="**")
            {
                pow=pow*int(pow(operand[j+2],operand[j+1]));
                j+=2;
            }
            operand.erase(operand.begin()+j+1,operand.end());
            operand[j]=pow;
        }
    }
    return operand[0];
}  // Note that the function do_algebra does not handle the case when the operator vector contains more than one of the same operator in a row. In that case, the function will not work correctly. It will also not work correctly if the operator vector contains more than one operator of the same type in a row. For example, if the