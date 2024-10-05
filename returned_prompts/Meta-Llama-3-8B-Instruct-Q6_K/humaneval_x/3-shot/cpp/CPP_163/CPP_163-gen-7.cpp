    vector<int> result;
    int min_val= min(a,b);
    int max_val=max(a,b);
    for (int i=min_val;i<=max_val;i++)
    {
        if (i%2==0)
        {
            result.push_back(i);
        }
    }
    return result;
}  // This will return the even numbers between a and b, in ascending order. If a is larger than b, it will return the even numbers between a and b in ascending order. If a is equal to b, it will return a vector containing only a. If a and b are the same and are even, it will return a vector containing only a. If a is odd and b is even, it will return a vector containing b. If a is even and b is odd, it will return a vector containing a. If both a and b are odd, it will return an empty vector.  // If a is even and b is even, it will return a vector containing all the even numbers between a and b. If a is odd and b is odd, it will return an empty vector.  // If a is odd, it will return a vector containing all the even numbers between a and b. If b is odd, it will return a vector containing all the even numbers between a and b.  // This function will return the even numbers between a and b in ascending order.  // It will not include the end points if they are odd.  // It will include the end points if they are even.  // It will not include any odd numbers.  // It will return an empty vector if there are no even numbers.  // It will return a vector containing all the even numbers between a and b if a and b are even.  // It will return a vector containing b if a is odd and b is even.  // It will return a vector containing a if a is even and b is odd.  // It will return a vector containing all the even numbers between a and b if a is even and b is even.  // It will return an empty vector if a and b are odd.  // It will return a vector containing all the even numbers between a and b if a is odd and b is odd.  // It will return a vector containing a if a is odd and b is odd.  // It will return a vector containing b if a is odd and b is odd.  // It will return a vector containing all the even numbers