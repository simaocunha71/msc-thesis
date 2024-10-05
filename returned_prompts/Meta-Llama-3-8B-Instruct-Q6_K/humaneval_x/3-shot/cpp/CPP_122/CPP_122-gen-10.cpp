    int sum=0;
    int i;
    for(i=0;i<k;i++)
    {
        if(log10(arr[i])<2)
        sum+=arr[i];
    }
    return sum;
}
// Alternative solution
int add_elements(vector<int> arr,int k){
    int sum=0;
    for(int i=0;i<k;i++)
    {
        if(log10(arr[i])<2)
        sum+=arr[i];
    }
    return sum;
}

