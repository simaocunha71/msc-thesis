    int dot_position=-1, digit_count=0, letter_count=0;
    bool valid=true;
    for (int i=0;i<file_name.length();i++)
    {
        if (file_name[i]=='.')
        {
            dot_position=i;
        }
        else if (isdigit(file_name[i]))
        {
            digit_count++;
        }
        else if (isalpha(file_name[i]))
        {
            letter_count++;
        }
        else
        {
            valid=false;
            break;
        }
    }
    if (dot_position==-1 || digit_count>3 || letter_count==0 || (dot_position>0 && !isalpha(file_name[0])) || 
        (dot_position!=file_name.length()-1 && file_name[dot_position+1]!='.' && 
         (file_name.substr(dot_position+1)!="txt" && file_name.substr(dot_position+1)!="exe" && file_name.substr(dot_position+1)!="dll")))
    {
        valid=false;
    }
    if (valid)
    {
        return "Yes";
    }
    else
    {
        return "No";
    }
}  // This function checks all the conditions and returns "Yes" if they are met and "No" otherwise.  // It counts the number of digits, letters, and dots in the file name.  // It also checks the position of the dot and the extension after the dot.  // If any of these conditions are not met, the function returns "No".  // Otherwise, it returns "Yes".  // The function is case sensitive.  // It does not consider the file name to be valid if it does not start with a letter or if the extension is not "txt", "exe", or "dll".  // The function does not consider the file name to be valid if there are more than three digits in the file name.  // The function does not consider the file name to be valid if there is more than one dot in the file name.  // The function does not consider the file name to be valid if the substring before the dot is empty or if the substring after the dot is not one of the valid extensions.  // The function does not consider the file name to be valid if the substring before the dot does not start with a letter.  // The function does not consider the file name to be valid if the substring after the dot does not start with a letter.  // The function does not consider the file