    int i,j;
    int max_length=0;
    int current_length;
    string max_string;
    for (i=0;i<strings.size();i++)
    {
        current_length=strings[i].length();
        if (current_length>max_length)
        {
            max_length=current_length;
            max_string=strings[i];
        }
    }
    return max_string;
}

