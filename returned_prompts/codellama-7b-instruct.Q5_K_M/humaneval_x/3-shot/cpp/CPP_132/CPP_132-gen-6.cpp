    int stack[str.size()];
    int top=-1;
    for (int i=0;i<str.size();i++)
    {
        if (str[i]=='[')
        {
            top+=1;
            stack[top]=i;
        }
        if (str[i]==']')
        {
            if (top==-1)
            return false;
            if (str[stack[top]]=='[')
            {
                top-=1;
                continue;
            }
            else
            {
                int index_start=stack[top];
                int index_end=i+1;
                if (index_end-index_start>2)
                {
                    return true;
                }
            }
        }
    }
    return false;
}


