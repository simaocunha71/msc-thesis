    int n=arr.size();
    int l,r;
    int i;
    int cnt=0;
    for (i=0;i<n/2;i++)
    {
        l=i;
        r=n-i-1;
        while (l<r)
        {
            if (arr[l]!=arr[r])
            {
                cnt++;
                break;
            }
            l++;
            r--;
        }
    }
    return cnt;
}