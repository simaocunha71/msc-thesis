    string result;
    int i;
    for (i=0;i<a.length();i++)
    {
        if (a[i]==b[i])
            result+= '0';
        else
            result+= '1';
    }
    return result;
}  // This solution is not correct. It will not work for strings of different lengths. It will also not work for strings of same length but with different ending characters. It will also not work for strings of same length and same ending characters but with different middle characters. It will give wrong result for strings with different lengths. It will also not work for strings of same length and same ending characters and same middle characters but with different starting characters.

