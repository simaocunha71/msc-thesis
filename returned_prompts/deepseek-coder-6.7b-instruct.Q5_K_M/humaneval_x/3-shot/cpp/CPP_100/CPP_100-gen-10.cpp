    vector<int> pile(n);
    pile[0]=n;
    for(int i=1;i<n;i++)
    {
        if(pile[i-1]%2==0)
        pile[i]=pile[i-1]+2;
        else
        pile[i]=pile[i-1]+2;
    }
    return pile;
}


