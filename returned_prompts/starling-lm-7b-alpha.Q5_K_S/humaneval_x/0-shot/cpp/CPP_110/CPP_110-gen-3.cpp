    int len1=lst1.size();
    int len2=lst2.size();
    if(len1!=len2) return "NO";
    int count=0;
    for(int i=0;i<len1;i++)
    {
        if(lst1[i]%2!=0)
        {
            for(int j=0;j<len2;j++)
            {
                if(lst2[j]%2==0)
                {
                    count++;
                    lst1[i]=lst2[j];
                    lst2[j]=lst1[i];
                    if(count==len1) return "YES";
                    goto A;
                }
            }
            return "NO";
        }
    }
    return "YES";
}
int main()
{
    vector<int> lst1={1,2,3,4};
    vector<int> lst2={1,2,3,4};
    printf("%s",exchange(lst1,lst2).c_str());
    return 0;
}




















































































































































































































































