    string temp;
    int counter=0;
    int i;
    for (i=0;i<file_name.length();i++)
    {
        if (file_name[i]>=48 && file_name[i]<=57)
        counter+=1;
    }
    if (counter>3)
    return "No";
    int dot=0;
    for (i=0;i<file_name.length();i++)
    {
        if (file_name[i]=='.')
        dot+=1;
    }
    if (dot!=1)
    return "No";
    int flag=0;
    for (i=0;i<file_name.length();i++)
    {
        if (flag==1 && (file_name[i]=='.' || file_name[i]>=48 && file_name[i]<=57))
        return "No";
        if (flag==1 && (file_name[i]>=65 && file_name[i]<=90 || file_name[i]>=97 && file_name[i]<=122))
        flag=0;
        if (flag==0 && (file_name[i]>=65 && file_name[i]<=90 || file_name[i]>=97 && file_name[i]<=122))
        flag=1;
    }
    if (flag==1)
    return "No";
    temp=file_name.substr(file_name.length()-3,3);
    if (temp!="txt" && temp!="exe" && temp!="dll")
    return "No";
    return "Yes";
}<|code_prefix|>