    string one=lst[0];
    string two=lst[1];

    if (one.length()==0 || two.length()==0)
    return "No";

    string both=one+two;
    int i,j;
    int level=0;
    for (i=0;i<both.length();i++)
    if (both[i]=='(')
    level+=1;
    else
    level-=1;

    if (level==0)
    return "Yes";
    else
    return "No";
}

