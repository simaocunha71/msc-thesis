    int i;
    int palindromic_sum=0;
    int current_sum=0;
    int min_changes=0;
    int max_value=0;
    for (i=0;i<arr.size();i++)
    {
        current_sum+=arr[i];
        if (current_sum>palindromic_sum)
        {
            palindromic_sum=current_sum;
            min_changes=i+1;
        }
        if (arr[i]>max_value)
            max_value=arr[i];
    }
    current_sum=0;
    for (i=arr.size()-1;i>=0;i--)
    {
        current_sum+=arr[i];
        if (current_sum>palindromic_sum)
        {
            palindromic_sum=current_sum;
            min_changes=arr.size()-1-i;
        }
        if (arr[i]>max_value)
            max_value=arr[i];
    }
    return min_changes;
}


