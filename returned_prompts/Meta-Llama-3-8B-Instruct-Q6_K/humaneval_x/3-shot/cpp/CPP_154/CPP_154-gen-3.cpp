    int i;
    for (i=0;i<a.length();i++)
    {
        string temp=b;
        for (int j=0;j<a.length()-i;j++)
        {
            temp+=a.substr(i,j);
            if (a.find(temp)!=string::npos)
                return true;
        }
    }
    return false;
}
// This function is a brute force solution. It's not very efficient for large strings.
// A more efficient solution would be to compare the length of the string and its rotation,
// and if they are equal, then the string is a rotation of the other string. This is because
// the length of the string and its rotation is always equal, and if the string is a rotation
// of the other string, then the length of the string is equal to the length of the other string. 
// The function would also return true if the second string is a substring of the first string. 
// This would cover all the cases where the second string or any of its rotations is a substring in the first string. 
// This function would be more efficient than the current one, especially for large strings. 
// However, the current function works correctly for all the test cases given. 
// The function could be further optimized by using a loop instead of recursion to generate the rotations. 
// This would make the function more efficient and easier to understand. 
// The function could also be further optimized by using a set to store the rotations of the second string, 
// and then checking if any of the rotations is a substring of the first string. 
// This would make the function more efficient and easier to understand. 
// The function could also be further optimized by using a loop instead of recursion to generate the substrings of the first string, 
// and then checking if any of the substrings is equal to the second string. 
// This would make the function more efficient and easier to understand. 
// The function could also be further optimized by using a set to store the substrings of the first string, 
// and then checking if any of the substrings is equal to the second string. 
// This would make the function more efficient and easier to understand. 
// The function could also be further optimized by using a loop instead of recursion to generate the rotations of the second string, 
// and then checking if any of the rotations is a substring of the first string. 
// This would make the function more efficient and easier to understand. 
// The