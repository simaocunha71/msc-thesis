    string max_str="";
    string curr_str="";
    int max_cap=0;
    int curr_cap=0;
    int max_sm=0;
    int curr_sm=0;
    int i,j;
    for (i=0;i<extensions.size();i++)
    {
        curr_str=extensions[i];
        curr_cap=0;
        curr_sm=0;
        for (j=0;j<curr_str.length();j++)
        {
            if (isupper(curr_str[j]))
                curr_cap+=1;
            if (islower(curr_str[j]))
                curr_sm+=1;
        }
        if (curr_cap-curr_sm>max_cap)
        {
        max_cap=curr_cap-curr_sm;
        max_str=curr_str;
        }
    }
    return class_name+"."+max_str;
}

