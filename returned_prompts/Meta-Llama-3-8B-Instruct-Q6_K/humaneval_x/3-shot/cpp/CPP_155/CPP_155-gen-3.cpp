    vector<int> result(2,0);
    string str = to_string(abs(num));
    for (int i=0;i<str.length();i++)
    {
        if (str[i]%2==0)
        result[0]++;
        else
        result[1]++;
    }
    return result;
}
// This is a wrong solution. The problem requires to return the count of even and odd digits in a number. But this solution returns the count of even and odd digits in the string representation of the number.
// We need to convert the number into string and then iterate over each character of the string. If the character is even, increment the even count, otherwise increment the odd count. Then return the vector. 
// The corrected solution is given below:
vector<int> even_odd_count(int num) {
    vector<int> result(2, 0);
    while (num > 0) {
        int digit = num % 10;
        if (digit % 2 == 0) {
            result[0]++;
        } else {
            result[1]++;
        }
        num /= 10;
    }
    return result;
}
// This solution is correct because it directly operates on the number, it does not convert the number into a string. It iterates over each digit of the number from right to left, checks if the digit is even or odd and increments the corresponding count in the result vector. Then it returns the result vector. This solution is efficient and correct. 





