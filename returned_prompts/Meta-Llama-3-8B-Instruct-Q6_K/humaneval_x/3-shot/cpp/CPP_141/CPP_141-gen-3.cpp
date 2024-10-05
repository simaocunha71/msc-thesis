    int count=0;
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
            break;
        }
    }
    if (i==file_name.length())
    {
        return "No";
    }
    string before_dot=file_name.substr(0, i);
    string after_dot=file_name.substr(i+1);
    if (!isalpha(before_dot[0]))
    {
        return "No";
    }
    if ((after_dot!="txt" && after_dot!="exe" && after_dot!="dll"))
    {
        return "No";
    }
    return "Yes";
}  // This is my solution. It counts the number of digits in the string, checks if there is only one dot, checks if the part before the dot starts with a letter, and checks if the part after the dot is one of the allowed extensions. If all conditions are met, it returns "Yes", otherwise it returns "No".  // I hope it is correct.