    int i;
    int count=0;
    for (i=0;i<str.length();i++)
    if (str[i]==substring[0])
    {
        int j=0;
        int k=0;
        while (str[i+k]==substring[j] && (i+k<str.length()) && (j<substring.length()))
        {
            j++;
            k++;
        }
        if (j==substring.length())
        count++;
    }
    return count;
}

