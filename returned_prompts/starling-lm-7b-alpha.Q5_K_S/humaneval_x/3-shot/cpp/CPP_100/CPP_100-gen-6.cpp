    vector<int> all_pile;
    int level=n;
    int i;
    for (i=0;i<n;i++)
    {
        all_pile.push_back(level);
        if (level%2==0){
        level+=1;
        }
        else
        {
            level+=2;
        }
    }
    return all_pile;
}


