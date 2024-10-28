    vector<int> l_prime;
    vector<int> l_third;
    for (int i=0;i<l.size();i++)
    {
        if (i%3==0)
        {
            l_third.push_back(l[i]);
        }
        else
        {
            l_prime.push_back(l[i]);
        }
    }
    sort(l_third.begin(),l_third.end());
    for (int i=0;i<l.size();i++)
    {
        if (i%3==0)
        {
            l_prime[i]=l_third[i/3];
        }
    }
    return l_prime;
}

