    for(int i=0;i<lst.size();i++)
    {
        if(lst[i]==0)
            continue;
        if(lst[i]==1)
            continue;
        if(lst[i]%2==0)
            continue;
        for(int j=2;j<=sqrt(lst[i]);j++)
        {
            if(lst[i]%j==0)
                continue A;
        }
        int sum=0,a=lst[i];
        while(a!=0)
        {
            sum+=a%10;
            a/=10;
        }
        return sum;
    }
    return 0;
}

int main()
{
    vector<int> lst={0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3};
    printf("%d\n",skjkasdkd(lst));
}

*/





























































































































































































































































