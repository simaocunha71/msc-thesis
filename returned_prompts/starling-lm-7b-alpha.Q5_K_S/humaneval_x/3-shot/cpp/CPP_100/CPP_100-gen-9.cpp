    vector<int> pile;
    int i,current_level=n;
    if (n%2==0)
    {
        for (i=0;i<n;i++)
        {
            pile.push_back(current_level);
            current_level+=2;
        }
    }
    else
    {
        for (i=0;i<n;i++)
        {
            pile.push_back(current_level);
            current_level+=1;
        }
    }
    return pile;
}


