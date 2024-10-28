    int left=0, right=arr.size()-1, changes=0;
    while (left<right)
    {
        if (arr[left]!=arr[right])
        {
            changes++;
            int left_value=arr[left];
            for (int i=left+1;i<right;i++)
            {
                if (arr[i]==arr[right])
                {
                    arr[i]=left_value;
                    break;
                }
            }
        }
        left++;
        right--;
    }
    return changes;
}
