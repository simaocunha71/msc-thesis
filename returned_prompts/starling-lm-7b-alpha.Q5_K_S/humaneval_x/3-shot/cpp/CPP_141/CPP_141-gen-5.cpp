    int i;
    int c_digits=0;
    int c_chars=0;
    bool letter_found=false;
    bool valid_file_extension_found=false;
    for (i=0;i<file_name.length();i++)
    {
        if (file_name[i]=='.')
        {
            if (c_digits>3)
            {
                return "No";
            }
            if (c_chars!=1)
            {
                return "No";
            }
            if (!letter_found)
            {
                return "No";
            }
            if (!(file_name[i+1]=='t'||file_name[i+1]=='x'||file_name[i+1]=='d'||file_name[i+1]=='l'||file_name[i+1]=='e'))
            {
                return "No";
            }
            valid_file_extension_found=true;
            c_chars=0;
            c_digits=0;
            letter_found=false;
        }
        else if (file_name[i]>='0'&&file_name[i]<='9')
        {
            c_digits++;
        }
        else if (file_name[i]>='a'&&file_name[i]<='z')
        {
            letter_found=true;
        }
        else if (file_name[i]>='A'&&file_name[i]<='Z')
        {
            letter_found=true;
        }
        else
        {
            return "No";
        }
        c_chars++;
    }
    if (c_digits>3)
    {
        return "No";
    }
    if (c_chars!=1)
    {
        return "No";
    }
    if (!letter_found)
    {
        return "No";
    }
    if (!valid_file_extension_found)
    {
        return "No";
    }
    return "Yes";
}



