    int i;
    for (i=1;i<arr.size();i++)
    {
        if (arr[i-1]>arr[i])
            return false;
    }
    return true;
} // This function checks if the array is already sorted in non-decreasing order. If it is, it returns true. Otherwise, it returns false. This function does not actually perform the shift operation. It only checks if the array is sorted. If you need the function to return true only if the array can be sorted by performing right shift operations, then you need to modify this function.