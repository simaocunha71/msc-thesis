    int len_b=b.length();
    for (int i=0;i<a.length();i++)
    {
        string temp=a.substr(i);
        if (temp.length()>=len_b)
        {
            if (temp.substr(0,len_b)==b)
                return true;
        }
    }
    return false;
}   // This function is not working properly, please check your code
// This function is not working properly, please check your code


