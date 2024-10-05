    vector<int> temp=lst2;
    int i,j;
    for (i=0;i<lst1.size();i++)
    {
        for (j=0;j<temp.size();j++)
        {
            if (lst1[i]%2==0 && temp[j]%2!=0)
            {
                int temp2=temp[j];
                temp[j]=lst1[i];
                lst1[i]=temp2;
                break;
            }
        }
    }
    for (i=0;i<lst1.size();i++)
    {
        if (lst1[i]%2!=0)
        return "NO";
    }
    return "YES";
}
//test
int main()
{
    vector<int> v1={1, 2, 3, 4};
    vector<int> v2={1, 2, 3, 4};
    cout<<exchange(v1,v2)<<endl;
    return 0;
}
//test end


