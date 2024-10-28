    vector<float> l_prime;
    for (int i=0;i<l.size();i++)
    {
        if (i%2==0)
        {
            sort(l.begin()+i,l.begin()+i+1);
            l_prime.push_back(l[i]);
        }
        else
        {
            l_prime.push_back(l[i]);
        }
    }
    return l_prime;
}