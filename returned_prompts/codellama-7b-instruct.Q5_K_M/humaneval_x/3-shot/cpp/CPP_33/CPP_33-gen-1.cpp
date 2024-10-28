    vector<int> l_prime;
    for (int i=0;i<l.size();i++)
    {
        if (i%3==0)
        sort(l.begin()+i,l.begin()+i+3);
        l_prime.push_back(l[i]);
    }
    return l_prime;
}


