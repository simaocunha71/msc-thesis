    vector<int> pile;
    int i;
    for (i=0;i<n;i++)
    {
        if ((i+1)%2==0)
            pile.push_back((i+1)+2);
        if ((i+1)%2!=0)
            pile.push_back((i+1)+1);
    }
    return pile;
}


