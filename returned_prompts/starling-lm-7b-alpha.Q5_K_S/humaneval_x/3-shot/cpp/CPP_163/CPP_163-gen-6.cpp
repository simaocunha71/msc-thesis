    vector<int> result;
    for (int i=a;i<=b;i++)
    {
        int temp=i;
        while (temp>0)
        {
            if (temp%2==0)
            {
                result.push_back(temp%10);
            }
            temp/=10;
        }
    }
    return result;
}




