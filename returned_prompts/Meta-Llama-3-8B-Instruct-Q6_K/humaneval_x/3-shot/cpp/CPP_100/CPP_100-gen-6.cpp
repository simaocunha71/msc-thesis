    vector<int> pile;
    pile.push_back(n);
    int stones=0;
    for (int i=1;i<n;i++)
    {
        if (i%2==0)
        stones+=2;
        else stones+=1;
        pile.push_back(stones);
    }
    return pile;
}  // This solution has a time complexity of O(n), where n is the number of levels in the pile.  // The space complexity is O(n), as we are storing the number of stones in each level in a vector.  // In terms of efficiency, this solution can be improved by reducing the number of operations.  // We can achieve this by using a simple formula to calculate the number of stones in each level, rather than iterating through the levels.  // This can reduce the time complexity to O(1).  // However, this would require a more complex solution that involves mathematical calculations.  // In this case, the given solution is simple and efficient.