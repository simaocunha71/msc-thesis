    string result="";
    if (lst.size()!=2)
    return "No";
    if (lst[0][0]=='(' && lst[1][0]==')')
    return "Yes";
    if (lst[0][0]==')' && lst[1][0]=='(')
    return "Yes";
    return "No";
}


