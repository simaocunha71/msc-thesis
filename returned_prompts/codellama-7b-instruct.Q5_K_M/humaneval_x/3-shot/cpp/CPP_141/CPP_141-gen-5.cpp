    int dot_count=0;
    int digit_count=0;
    int i;
    for (i=0;i<file_name.length();i++)
    {
        if (file_name[i]=='.')
        dot_count+=1;
        if (file__name[i]>='0'&&file_name[i]<='9')
        digit_count+=1;
    }
    if (dot_count==1&&digit_count<=3)
    {
        int j;
        for (j=0;j<file_name.length();j++)
        {
            if (file_name[j]=='.'&&file_name[j+1]=='t'&&file_name[j+2]=='x'&&file_name[j+3]=='t')
            return "Yes";
            else if (file_name[j]=='.'&&file_name[j+1]=='e'&&file_name[j+2]=='x'&&file_name[j+3]=='e')
            return "Yes";
            else if (file_name[j]=='.'&&file_name[j+1]=='d'&&file_name[j+2]=='l'&&file_name[j+3]=='l')
            return "Yes";
        }
    }
    return "No";
}


