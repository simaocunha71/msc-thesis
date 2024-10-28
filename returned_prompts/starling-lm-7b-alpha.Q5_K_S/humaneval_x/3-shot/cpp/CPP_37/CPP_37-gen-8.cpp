    vector<float> l_prime;
    int i;
    for (i=0;i<l.size();i++)
    {
        if (i%2==0)
        {
            l_prime.push_back(l[i]);
        }
        else
        {
            l_prime.push_back(l[i]);
        }
    }
    sort(l_prime.begin(),l_prime.end());
    return l_prime;
}


