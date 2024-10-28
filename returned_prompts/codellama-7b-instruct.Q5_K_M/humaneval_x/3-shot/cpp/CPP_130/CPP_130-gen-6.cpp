    vector<int> ans;
    int current;
    int previous;
    int previous_previous;
    int i;
    ans.push_back(1);
    ans.push_back(3);
    current=2;
    previous=1;
    previous_previous=3;
    for (i=0;i<n-2;i++)
    {
        if (i%2==0)
        current=previous_previous+previous+current;
        else 
        current=previous+previous_previous+current;
        ans.push_back(current);
        previous_previous=previous;
        previous=current;
    }
    return ans;
}


