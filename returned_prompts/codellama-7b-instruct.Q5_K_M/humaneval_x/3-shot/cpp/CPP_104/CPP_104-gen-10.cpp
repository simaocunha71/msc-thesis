    vector<int> result;
    vector<int> unique;
    int i,j;
    for (i=0;i<x.size();i++)
    {
        int temp=x[i];
        while (temp>0)
        {
            if (temp%10%2==0)
            break;
            else if (temp%10==0)
            continue;
            else if (temp%10==9)
            break;
            else
            temp/=10;
        }
        if (temp==0)
        {
            result.push_back(x[i]);
        }
    }
    sort(result.begin(), result.end());
    return result;
}


