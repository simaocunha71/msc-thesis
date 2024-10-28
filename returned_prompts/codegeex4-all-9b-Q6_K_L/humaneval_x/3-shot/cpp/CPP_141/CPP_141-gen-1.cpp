    int i=0;
    int dot_count=0;
    int digit_count=0;
    char chr;
    if (file_name.length()>0)
    {
        if (file_name[0]>='A' && file_name[0]<='Z' || file_name[0]>='a' && file_name[0]<='z')
        {
            for (i=0;i<file_name.length();i++)
            {
                chr=file_name[i];
                if (chr=='.')
                {
                    dot_count+=1;
                    if (dot_count>1)
                    {
                        return "No";
                    }
                }
                else if (chr>='0' && chr<='9')
                {
                    digit_count+=1;
                    if (digit_count>3)
                    {
                        return "No";
                    }
                }
            }
            if (dot_count==1)
            {
                if (file_name[file_name.length()-1]=='t' && file_name[file_name.length()-2]=='x' && file_name[file_name.length()-3]=='.')
                {
                    return "Yes";
                }
                if (file_name[file_name.length()-1]=='e' && file_name[file_name.length()-2]=='x' && file_name[file_name.length()-3]=='.')
                {
                    return "Yes";
                }
                if (file_name[file_name.length()-1]=='l' && file_name[file_name.length()-2]=='l' && file_name[file_name.length()-3]=='.')
                {
                    return "Yes";
                }
                else
                {
                    return "No";
                }
            }
            else
            {
                return "No";
            }
        }
        else
        {
            return "No";
        }
    }
    else
    {
        return "No";
    }
} 

