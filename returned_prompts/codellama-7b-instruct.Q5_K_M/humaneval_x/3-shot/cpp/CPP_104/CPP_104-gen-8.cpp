    vector<int> res;
    for (int i=0;i<x.size();i++)
    {
        int temp=x[i];
        while (temp>0)
        {
            if (temp%10%2==0)
            {
                res.push_back(x[i]);
                break;
            }
            else
            temp/=10;
        }
    }
    sort(res.begin(), res.end());
    return res;
}



