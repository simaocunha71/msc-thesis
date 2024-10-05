    vector<int> no_even;
    for (int i=0;i<x.size();i++)
    {
        int temp=x[i];
        int flag=0;
        while (temp>0)
        {
            int digit=temp%10;
            if (digit%2==0)
            {
                flag=1;
                break;
            }
            temp=temp/10;
        }
        if (flag==0)
            no_even.push_back(x[i]);
    }
    sort(no_even.begin(),no_even.end());
    return no_even;
}

