    int count=0;
    bool has_dot=false;
    bool has_valid_extension=false;
    int i;
    for (i=0;i<file_name.length();i++)
    {
        if (isdigit(file_name[i]))
        {
            count++;
            if (count>3)
            return "No";
        }
        if (file_name[i]=='.')
        {
            has_dot=true;
        }
        if (has_dot)
        {
            if (file_name[i]=='t'&&file_name[i+1]=='x'&&file_name[i+2]=='.')
            {
                has_valid_extension=true;
                i+=2;
            }
            else if (file_name[i]=='e'&&file_name[i+1]=='x'&&file_name[i+2]=='e'&&file_name[i+3]=='.')
            {
                has_valid_extension=true;
                i+=3;
            }
            else if (file_name[i]=='d'&&file_name[i+1]=='l'&&file_name[i+2]=='l'&&file_name[i+3]=='.')
            {
                has_valid_extension=true;
                i+=3;
            }
        }
    }
    if (count>3 || !has_dot || !has_valid_extension || file_name[0]<'a'|| file_name[0]>'z'|| file_name[0]<'A'|| file_name[0]>'Z')
    return "No";
    return "Yes";
}
