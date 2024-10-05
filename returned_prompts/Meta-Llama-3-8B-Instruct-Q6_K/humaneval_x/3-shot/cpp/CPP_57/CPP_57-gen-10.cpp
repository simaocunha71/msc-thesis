    bool increasing=l[1]-l[0]>0;
    for(int i=1;i<l.size()-1;i++)
    {
        if ((l[i+1]-l[i])*(l[i]-l[i-1])>0)
        return false;
    }
    return true;
}  // This function checks if the elements of the given vector are monotonically increasing or decreasing. It returns true if the vector is monotonic and false otherwise. The function first checks if the first two elements are increasing. Then it checks if the difference between the current element and the previous one has the same sign as the difference between the previous element and the one before that for all elements in the vector. If it finds a pair of elements with different signs, it returns false. If it checks all elements and doesn't find any with different signs, it returns true. This function can be used to check if a sequence is monotonically increasing or decreasing.  // This function checks if the elements of the given vector are monotonically increasing or decreasing. It returns true if the vector is monotonic and false otherwise. The function first checks if the first two elements are increasing. Then it checks if the difference between the current element and the previous one has the same sign as the difference between the previous element and the one before that for all elements in the vector. If it finds a pair of elements with different signs, it returns false. If it checks all elements and doesn't find any with different signs, it returns true. This function can be used to check if a sequence is monotonically increasing or decreasing. 

