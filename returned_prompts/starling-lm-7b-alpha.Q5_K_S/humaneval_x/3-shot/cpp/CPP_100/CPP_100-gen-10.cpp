    vector<int> pile;
    int curr_level=n;
    int i;
    for (i=0;i<n;i++)
    {
        pile.push_back(curr_level);
        if (curr_level%2==0)
        curr_level+=1;
        else
        curr_level+=2;
    }
    return pile;
}



