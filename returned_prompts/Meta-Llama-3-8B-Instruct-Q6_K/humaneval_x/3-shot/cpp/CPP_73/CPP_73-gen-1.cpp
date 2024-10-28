    int n=arr.size();
    int count=0;
    int i,j;
    for(i=0,j=n-1;i<j;)
    {
        if(arr[i]==arr[j])
        {
            i++;
            j--;
        }
        else
        {
            if(arr[i+1]==arr[j])
            {
                arr[i++]=arr[j--];
                count++;
            }
            else if(arr[i]==arr[j-1])
            {
                arr[i++]=arr[j--];
                count++;
            }
            else
            {
                i++;
                j--;
                count++;
            }
        }
    }
    return count;
}