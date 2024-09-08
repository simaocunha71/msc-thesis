    int arr_len=arr.size();
    int arr_len_1=arr_len-1;
    int i,j,k;
    int temp;
    for(i=0;i<arr_len_1;i++)
    {
        for(j=0;j<arr_len_1-i;j++)
        {
            int n=arr[j];
            int count=0;
            int n_len=0;
            while(n>0)
            {
                if(n%2==1)
                {
                    count++;
                }
                n=n/2;
                n_len++;
            }
            int n_2=arr[j+1];
            int count_2=0;
            int n_len_2=0;
            while(n_2>0)
            {
                if(n_2%2==1)
                {
                    count_2++;
                }
                n_2=n_2/2;
                n_len_2++;
            }
            if(count<count_2)
            {
                temp=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=temp;
            }
            else if(count==count_2)
            {
                if(arr[j]>arr[j+1])
                {
                    temp=arr[j];
                    arr[j]=arr[j+1];
                    arr[j+1]=temp;
                }
            }
        }
    }
    return arr;
}

B:
    int arr_len=arr.size();
    int arr_len_1=arr_len-1;
    int i,j,k;
    int temp;
    for(i=0;i<arr_len_1;i++)
    {
        for(j=0;j<arr_len_1-i;j++)
        {
            int n=arr[j];
            int count=0;
            int n_len=0;
            while(n>0)
            {
                if(n%2==1)
                {
                    count++;
                }
                n=n/2;
                n_len++;
            }
            int n_2=arr[j+1];
            int count_2=0;
            int n_len_2=0;
            while(n_2>0)
            {
                if(n_2%2==1)
                {
                    count_2++;
                }
                n_2=n_2/2;
                n_len_2++;
            }
            if(count>count_2)
            {
                temp=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=temp;
            }
