    int i;
    int counter=0;
    int counter2=0;
    int counter3=0;
    for (i=0;i<file_name.length();i++)
    {
        if (file_name[i]>=48 && file_name[i]<=57)
        {
            counter+=1;
        }
        if (file_name[i]>=65 && file_name[i]<=90)
        {
            counter3+=1;
        }
        if (file_name[i]>=97 && file_name[i]<=122)
        {
            counter3+=1;
        }
    }
    for (i=0;i<file_name.length();i++)
    {
        if (file_name[i]=='.')
        {
            counter2+=1;
        }
    }
    if (counter2==1 && counter3==1 && counter<=3)
    {
        return "Yes";
    }
    return "No";
}

