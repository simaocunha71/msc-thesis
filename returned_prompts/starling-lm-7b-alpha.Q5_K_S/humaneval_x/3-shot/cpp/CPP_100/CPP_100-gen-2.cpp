    vector<int> pile;
    int i;
    for (i=0;i<n;i++)
    {
        int num=i+1;
        if (i%2==0)
        {
            pile.push_back(num);
        }
        else
        {
            pile.push_back(num+1);
        }
    }
    return pile;
}


