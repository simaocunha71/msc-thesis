    sort(arr.begin(),arr.end(),[&](int a,int b)
    {
        if (bitset<32>(a).count()!=bitset<32>(b).count())
        {
            return bitset<32>(a).count()<bitset<32>(b).count();
        }
        return a<b;
    });
    return arr;
}
// Note: This solution uses the bitset class from the standard library. It counts the number of ones in the binary representation of each integer and uses this as the primary sorting criterion. If two integers have the same number of ones, it uses the actual integer value as a secondary sorting criterion. This ensures that the function works correctly even if there are multiple integers with the same number of ones. The lambda function passed to the sort function defines the comparison criterion. It takes two integers as input, counts the number of ones in their binary representation using the bitset class, and returns true if the first integer should come before the second in the sorted order. If the number of ones is the same, it returns the result of the comparison of the two integers themselves, which is used as the secondary sorting criterion. The sort function then uses this comparison criterion to sort the array. The sorted array is returned as the result.