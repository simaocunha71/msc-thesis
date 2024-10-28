    int i;
    for (i=0;i<a.length();i++)
    {
        string temp=a.substr(i,a.length());
        if (temp.find(b)!=string::npos)
        {
            return true;
        }
    }
    return false;
}  // Time complexity O(n*m) where n is the length of a and m is the length of b.  // Space complexity O(n) for storing substrings of a.