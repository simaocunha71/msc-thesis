    sort(arr.begin(), arr.end(), [](int a, int b)
    {
        if (count(b, b+1, '1') == count(a, a+1, '1'))
            return a < b;
        return count(b, b+1, '1') < count(a, a+1, '1');
    });
    return arr;
}  //using lambda function for sorting and count function from string library for counting number of 1's in binary representation


