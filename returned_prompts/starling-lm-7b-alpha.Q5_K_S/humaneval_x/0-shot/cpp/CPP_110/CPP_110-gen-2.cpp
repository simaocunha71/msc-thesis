    int i,j,k;
    int count=0;
    for(i=0;i<lst1.size();i++)
    {
        if(lst1[i]%2!=0)
        {
            count++;
        }
    }
    if(count==0)
    {
        return "YES";
    }
    for(i=0;i<lst2.size();i++)
    {
        if(lst2[i]%2!=0)
        {
            for(j=0;j<lst1.size();j++)
            {
                if(lst1[j]%2==0)
                {
                    k=lst2[i];
                    lst2[i]=lst1[j];
                    lst1[j]=k;
                    goto A;
                }
            }
        }
    }
    return "NO";
}

int main()
{
    vector<int> lst1,lst2;
    int n;
    scanf("%d",&n);
    for(int i=0;i<n;i++)
    {
        int temp;
        scanf("%d",&temp);
        lst1.push_back(temp);
    }
    for(int i=0;i<n;i++)
    {
        int temp;
        scanf("%d",&temp);
        lst2.push_back(temp);
    }
    printf("%s\n",exchange(lst1,lst2).c_str());
    return 0;
}


*/






























































































































