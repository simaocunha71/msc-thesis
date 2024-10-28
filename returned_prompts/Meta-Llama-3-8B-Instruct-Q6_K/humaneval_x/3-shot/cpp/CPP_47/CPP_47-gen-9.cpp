    sort(l.begin(),l.end());
    int n=l.size();
    if (n%2==0)
    return (l[n/2-1]+l[n/2])/2;
    else
    return l[n/2];
} // This function returns the median of the given vector of floats. It first sorts the vector, then checks if the size of the vector is even or odd. If the size is even, it returns the average of the two middle elements; otherwise, it returns the middle element.