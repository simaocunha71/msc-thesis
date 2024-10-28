    int smallest_even=100000000;
    int smallest_index=0;
    int i;
    for (i=0;i<arr.size();i++)
    {
        if (arr[i]%2==0 && arr[i]<smallest_even)
        {
            smallest_even=arr[i];
            smallest_index=i;
        }
    }
    vector<int> out={smallest_even, smallest_index};
    return out;
}


