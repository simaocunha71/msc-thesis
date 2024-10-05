    int count=0;
    string result;
    int i,j;
    char chr;
    for (i=0;i<lst.size();i++)
    for (j=0;j<lst[i].length();j++)
    {
        chr=lst[i][j];
        if (chr=='(')
            count+=1;
        if (chr==')')
            count-=1;
        if (count<0)
            return "No";
    }

    if (count==0)
        result="Yes";
    else
        result="No";

    return result;
}

