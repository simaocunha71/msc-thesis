    int i;
    int number_of_digits=0;
    int number_of_dots=0;
    int index_of_last_dot;
    string extension;
    for (i=0;i<file_name.length();i++)
    {
        if (file_name[i]>='0' && file_name[i]<='9')
        number_of_digits++;
        if (file_name[i]=='.')
        {
            number_of_dots++;
            index_of_last_dot=i;
        }
    }
    if (number_of_dots!=1 || number_of_digits>3)
    return "No";
    if (index_of_last_dot==0)
    return "No";
    extension=file_name.substr(index_of_last_dot+1);
    if (extension!="txt" && extension!="exe" && extension!="dll")
    return "No";
    return "Yes";
}



