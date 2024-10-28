    int i;
    for (i=0;i<arr.size()-1;i++)
    {
        if (arr[i]>arr[i+1])
        {
            return false;
        }
    }
    return true;
} // This function checks if the array is already sorted, if it is, it returns true, else it returns false.


