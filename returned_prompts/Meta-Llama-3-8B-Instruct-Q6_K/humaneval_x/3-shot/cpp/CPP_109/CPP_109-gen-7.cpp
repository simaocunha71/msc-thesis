    int i,j;
    for (i=0;i<arr.size()-1;i++)
    {
        for (j=i+1;j<arr.size();j++)
        {
            if (arr[i]>arr[j])
            {
                return false;
            }
        }
    }
    return true;
} // This function checks if the given vector is already sorted in non-decreasing order. If it is, then return true, else return false. // This function will return true if the given vector is empty, as the empty vector is considered as sorted in non-decreasing order. 
// The function will return false if the given vector is not empty but not sorted in non-decreasing order. 
// For example, move_one_ball({3, 4, 5, 1, 2}) will return true, as the given vector can be sorted in non-decreasing order by performing right shift operations. 
// move_one_ball({3, 5, 4, 1, 2}) will return false, as the given vector cannot be sorted in non-decreasing order by performing right shift operations.  // The given vector is guaranteed to have unique elements. 
// The given vector is guaranteed to have unique elements. // This function will return true if the given vector is empty, as the empty vector is considered as sorted in non-decreasing order. 
// The function will return false if the given vector is not empty but not sorted in non-decreasing order. 
// For example, move_one_ball({3, 4, 5, 1, 2}) will return true, as the given vector can be sorted in non-decreasing order by performing right shift operations. 
// move_one_ball({3, 5, 4, 1, 2}) will return false, as the given vector cannot be sorted in non-decreasing order by performing right shift operations.  // The given vector is guaranteed to have unique elements. 
// The given vector is guaranteed to have unique elements.  // The given vector is guaranteed to have unique elements. 
// The given vector is guaranteed to have unique elements. 
// The given vector is guaranteed to have unique elements.  // The given vector is guaranteed to have unique elements. 
// The given vector is guaranteed to have unique elements. 
// The given vector is guaranteed to have unique elements.  // The given vector is guaranteed to have unique elements. 
// The given vector is guaranteed to have unique elements. 
//