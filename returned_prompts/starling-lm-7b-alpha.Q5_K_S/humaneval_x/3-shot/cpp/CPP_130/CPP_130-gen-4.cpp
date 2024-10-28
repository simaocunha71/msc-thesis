    vector<int> res;
    vector<int> res_aux;
    res.push_back(3);
    res_aux.push_back(3);
    int i;
    for (i=2;i<=n;i++)
    {
        if (i%2==0)
        {
            res.push_back(1+(i/2));
        }
        if (i%2!=0)
        {
            res.push_back(res_aux[i-1]+res_aux[i-2]+res_aux[i+1]);
        }
    }
    return res;
}


