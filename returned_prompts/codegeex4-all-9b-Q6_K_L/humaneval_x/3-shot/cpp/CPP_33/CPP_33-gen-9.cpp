    vector<int> l_prime;
    vector<int> div_three;
    int i;
    for (i=0;i<l.size();i++)
    {
        if (i%3==0)
        div_three.push_back(l[i]);
        else
        l_prime.push_back(l[i]);
    }
    sort(div_three.begin(),div_three.end());
    int j;
    for (j=0;j<div_three.size();j++)
    l_prime.insert(l_prime.begin()+j*3, div_three[j]);

    return l_prime;
}

