    int i;
    int letter_count=0;
    int number_count=0;
    for (i=0;i<file_name.length();i++)
    {
        if (file_name[i]>='a' && file_name[i]<='z')
        letter_count+=1;
        if (file_name[i]>='A' && file_name[i]<='Z')
        letter_count+=1;
        if (file_name[i]>='0' && file_name[i]<='9')
        number_count+=1;
    }
    if (letter_count==0 || number_count>3 || file_name.find(".")==string::npos)
    return "No";
    if (file_name[file_name.length()-1]=='.')
    return "No";

    string file_type=file_name.substr(file_name.length()-3);
    if (file_type=="txt" || file_type=="dll" || file_type=="exe")
    return "Yes";
    return "No";
}




