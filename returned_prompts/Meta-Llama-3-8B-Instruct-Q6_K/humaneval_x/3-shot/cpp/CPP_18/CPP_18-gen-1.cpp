    int count=0;
    int i=0;
    while(i<=str.length()-substring.length())
    {
        if(str.substr(i,substring.length())==substring)
            count++;
        i++;
    }
    return count;
}  // 1. substr() function is used to find the substring of the given string.
   // 2. while loop is used to traverse the string and find the occurrence of the substring.
   // 3. If the substring is found, then the count is incremented by 1.
   // 4. Finally, the count is returned as the result.
}  // This is a simple and efficient solution for the problem. It has a time complexity of O(n*m), where n is the length of the string and m is the length of the substring.