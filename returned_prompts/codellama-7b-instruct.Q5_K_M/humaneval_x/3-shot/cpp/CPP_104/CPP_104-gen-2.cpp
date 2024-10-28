    vector<int> y;
    int i,j;
    for (i=0;i<x.size();i++)
    {
        int num=x[i];
        int temp=num;
        for (j=0;j<10;j++)
        {
            if (temp%10==0)
            break;
            else if (temp%10%2==0)
            {
            y.push_back(num);
            break;
            }
            temp/=10;
        }
    }
    sort(y.begin(),y.end());
    return y;
}


