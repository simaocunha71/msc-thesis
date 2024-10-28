    int i;
    int count_of_digits=0;
    int count_of_dots=0;
    bool first_part_valid=false;
    bool second_part_valid=false;
    for (i=0;i<file_name.length();i++)
    {
        if (file_name[i]>='0' && file_name[i]<='9')
        count_of_digits+=1;
        if (file_name[i]=='.')
        count_of_dots+=1;
        if (file_name[i]>='a' && file_name[i]<='z' || file_name[i]>='A' && file_name[i]<='Z')
        first_part_valid=true;
        if (file_name[i]=='t' || file_name[i]=='e' || file_name[i]=='x' || file_name[i]=='e' || file_name[i]=='l' || file_name[i]=='l' || file_name[i]=='d' || file_name[i]=='l' || file_name[i]=='l')
        second_part_valid=true;
    }
    if (count_of_digits>3)
    return "No";
    if (count_of_dots>1)
    return "No";
    if (first_part_valid==false)
    return "No";
    if (second_part_valid==false)
    return "No";
    return "Yes";
}


