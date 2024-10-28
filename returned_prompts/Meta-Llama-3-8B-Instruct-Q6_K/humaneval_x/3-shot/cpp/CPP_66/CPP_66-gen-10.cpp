    int sum=0;
    for(int i=0;i<s.length();i++)
    {
        if (isupper(s[i]))
        {
            sum+=int(s[i]);
        }
    }
    return sum;
}  // This code is not working correctly. It seems like it's treating uppercase letters as digits. We need to treat uppercase letters as ASCII codes. Also, it's not handling lowercase letters. We need to convert both lowercase and uppercase letters to uppercase before summing their ASCII values.


