    int i;
    for (i=0;i<arr.size()-1;i++)
    if (arr[i]>arr[i+1])
    return false;
    return true;
}  // This function checks if the given array can be sorted in non-decreasing order by performing right shift operation. If the given array is already sorted or it can be sorted, the function returns true. Otherwise, it returns false. The function iterates through the array and checks if any element is greater than its next element. If it finds such a pair, it immediately returns false. If it does not find any such pair, it means the array can be sorted and it returns true. The function considers the case where the array is empty and returns true in this case. The function does not check if the array contains duplicate elements. It assumes that the array contains unique elements as per the problem statement.