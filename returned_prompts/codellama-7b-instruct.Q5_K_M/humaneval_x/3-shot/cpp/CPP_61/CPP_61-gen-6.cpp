    int num_openings=0;
    int i;
    for (i=0;i<brackets.length();i++)
    if (brackets[i]=='(')
    num_openings+=1;
    for (i=0;i<brackets.length();i++)
    if (brackets[i]==')')
    num_openings-=1;
    return num_openings==0;
}



