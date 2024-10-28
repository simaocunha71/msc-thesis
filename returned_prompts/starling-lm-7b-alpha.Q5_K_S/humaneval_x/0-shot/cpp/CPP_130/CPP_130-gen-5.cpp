    vector<int> arr;
    arr.push_back(3);
    if(n==0)
        return arr;
    else if(n==1)
    {
        arr.push_back(1);
        return arr;
    }
    else if(n==2)
    {
        arr.push_back(2);
        return arr;
    }
    else
    {
        int i=3;
        while(i<=n)
        {
            if(i%2==0)
            {
                arr.push_back(1+(i/2));
                i++;
            }
            else
            {
                arr.push_back(arr[arr.size()-1]+arr[arr.size()-2]+arr[arr.size()-3]);
                i++;
            }
        }
    }
    return arr;
}
int main()
{
    int n;
    scanf("%d",&n);
    for(int i=0;i<n+1;i++)
    {
        printf("%d ",tri(i).at(i));
    }
    return 0;
}








































































































































































































































