    int changes=0;
    int left=0;
    int right=arr.size()-1;
    while (left<right){
        if (arr[left]!=arr[right]){
            changes++;
            left++;
            right--;
        }
        else
        {
            left++;
            right--;
        }
    }
    return changes;
}

