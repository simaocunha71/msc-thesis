    int sum = 0;
    int i;
    for (i=0;i<lst.size();i++)
    {
        sum += ceil(lst[i])*ceil(lst[i]);
    }
    return sum;
}  // This function will return the sum of squares of the elements in the vector, each element rounded up to the nearest integer.