    vector<float> l_prime;
    int i;
    for (i=0;i<l.size();i++)
    {
        if (i%2==0)
        {
            sort(&l[i]/2,&l[i]/2+l/2);
            for (int j=i/2;j<i/2+l/2;j++)
            {
                l_prime.push_back(l[j]);
            }
        }
        else
        {
            l_prime.push_back(l[i]);
        }
    }
    return l_prime;
} 