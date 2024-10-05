    bool valid=true;
    int count=0;
    int i;
    for (i=0;i<file_name.length();i++)
    {
        if (file_name[i]>='0' && file_name[i]<='9')
        {
            count++;
        }
        else if (file_name[i]=='.')
        {
            if (count>3 || i==file_name.length()-1)
                valid=false;
            else
            {
                string extension=file_name.substr(i+1);
                if (extension!="txt" && extension!="exe" && extension!="dll")
                    valid=false;
            }
        }
        else if (i==0 && (!isalpha(file_name[i])))
            valid=false;
    }
    if (valid)
        return "Yes";
    else
        return "No";
}  // note: this function does not check if the file name is valid according to the file system rules (like the length of the file name, the length of the path, etc.). It only checks if the file name is valid according to the given rules.