    vector<int> collatz_odd;
    collatz_odd.push_back(n);
    while (collatz_odd[collatz_odd.size()-1]!=1)
    {
        if (collatz_odd[collatz_odd.size()-1]%2==1)
        collatz_odd.push_back(3*collatz_odd[collatz_odd.size()-1]+1);
        else
        collatz_odd.push_back(collatz_odd[collatz_odd.size()-1]/2);
    }
    sort(collatz_odd.begin(), collatz_odd.end());
    return collatz_odd;
}



