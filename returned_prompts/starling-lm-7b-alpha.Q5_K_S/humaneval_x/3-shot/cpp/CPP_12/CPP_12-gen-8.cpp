    int i;
    string longest_str="";
    for (i=0;i<strings.size();i++)
    {
        if (longest_str.length()<strings[i].length())
        {
            longest_str=strings[i];
        }
    }
    return longest_str;
}


