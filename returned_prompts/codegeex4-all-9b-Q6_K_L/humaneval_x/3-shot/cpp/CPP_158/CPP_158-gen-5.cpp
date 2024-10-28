    int i;
    int j;
    int max=0;
    string max_string="";
    for (i=0;i<words.size();i++)
    {
        string current_string=words[i];
        sort(current_string.begin(),current_string.end());
        if (count(current_string.begin(),current_string.end(),current_string[0])>max)
        {
            max_string=current_string;
            max=count(current_string.begin(),current_string.end(),current_string[0]);
        }
    }
    return max_string;
}

