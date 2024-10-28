    vector<int> all_int;
    int i,j;
    for (i=0;i<x.size();i++)
    {
        j=x[i];
        while (j>0)
        {
            if ((j%10)%2==0)
            break;
            else
            j=j/10;
        }
        if (j==0)
        all_int.push_back(x[i]);
    }
    sort(all_int.begin(),all_int.end());
    return all_int;
}

