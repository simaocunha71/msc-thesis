    int i,j;
    for (i=lst.size()-1;i>=0;i--)
    {
        int current_number=lst[i];
        int current_frequency=0;
        for (j=0;j<lst.size();j++)
        if (lst[j]==current_number)
        current_frequency+=1;

        if (current_frequency>=current_number)
        return current_number;
    }
    return -1;
}



