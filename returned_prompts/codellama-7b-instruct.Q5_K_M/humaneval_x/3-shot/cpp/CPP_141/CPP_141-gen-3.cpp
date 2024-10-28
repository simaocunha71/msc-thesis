    int i,j;
    int num_count=0;
    int dot_count=0;
    int letter_count=0;
    int end_count=0;
    for (i=0;i<file_name.length();i++)
    {
        if (file_name[i]>='0'&&file_name[i]<='9')
        num_count+=1;
        if (file_name[i]=='.')
        dot_count+=1;
        if (file_name[i]>='a'&&file_name[i]<='z'||file_name[i]>='A'&&file_name[i]<='Z')
        letter_count+=1;
        if (file_name.length()-i==3)
        end_count+=1;
    }
    if (num_count<=3&&dot_count==1&&letter_count==1&&end_count==0)
    return "Yes";
    else
    return "No";
}



