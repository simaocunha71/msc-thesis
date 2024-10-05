    long long sum=0;
    for (float num : lst)
    {
        if (num>0 && int(num)==num)
        {
            sum+=pow(num,2);
        }
    }
    return sum;
} // This function will return 0 for an empty input vector. If you want to return a specific value for an empty input vector, you can add a check at the beginning of the function. For example, if you want to return 0 for an empty vector and -1 for a vector with at least one element, you can add the following check: if (lst.empty()) return -1; before the loop.