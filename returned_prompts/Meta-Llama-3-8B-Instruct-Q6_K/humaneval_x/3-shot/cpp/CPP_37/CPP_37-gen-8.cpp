    vector<float> l_prime;
    for (int i=0;i<l.size();i++)
    {
        if (i%2==0)
        {
            l_prime.push_back(i%2==0?*min_element(l.begin(),l.end()):l[i]);
        }
        else
        {
            l_prime.push_back(l[i]);
        }
    }
    return l_prime;
} 