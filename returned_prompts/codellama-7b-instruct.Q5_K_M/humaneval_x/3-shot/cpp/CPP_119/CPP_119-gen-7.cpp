    int i;
    int balance=0;
    for (i=0;i<lst[0].length();i++)
    if (lst[0][i]=='(')
    balance+=1;
    else
    balance-=1;
    if (balance==0)
    return "Yes";
    balance=0;
    for (i=0;i<lst[1].length();i++)
    if (lst[1][i]=='(')
    balance+=1;
    else
    balance-=1;
    if (balance==0)
    return "Yes";
    return "No";
}


