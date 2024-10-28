    for(int i=0;i<arr.size();i++)
    {
        for(int j=0;j<arr.size()-1;j++)
        {
            if(arr[j]==-1)
            {
                int temp=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=temp;
            }
            else if(countOnes(arr[j])>countOnes(arr[j+1])||(countOnes(arr[j])==countOnes(arr[j+1])&&arr[j]>arr[j+1]))
            {
                int temp=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=temp;
            }
        }
    }
    return arr;
}

int countOnes(int n)
{
    int count=0;
    while(n!=0)
    {
        if(n%2==1)
        {
            count++;
        }
        n=n/2;
    }
    return count;
}

int main()
{
    int arr[]={-2,-3,-4,-5,-6};
    int size=sizeof(arr)/sizeof(arr[0]);
    vector<int> v(arr,arr+size);
    for(int i=0;i<size;i++)
    {
        printf("%d ",v[i]);
    }
    printf("\n");
    vector<int> res=sort_array(v);
    for(int i=0;i<size;i++)
    {
        printf("%d ",res[i]);
    }
    printf("\n");
    return 0;
}



*/





















































































