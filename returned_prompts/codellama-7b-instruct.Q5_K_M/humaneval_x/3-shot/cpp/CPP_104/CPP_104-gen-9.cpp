    vector<int> y;
    for (int i=0;i<x.size();i++)
    {
        int a=x[i];
        while (a>0)
        {
            int b=a%10;
            if (b%2==1)
            {
                y.push_back(a);
            }
            a/=10;
        }
    }
    sort(y.begin(),y.end());
    return y;
}



