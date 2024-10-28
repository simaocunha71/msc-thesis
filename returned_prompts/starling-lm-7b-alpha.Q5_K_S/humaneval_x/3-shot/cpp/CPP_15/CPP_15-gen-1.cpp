    string result;
    int i;
    for (i=0;i<=n;i++)
    {
        result+=to_string(i);
        if (i<n) result+=" ";
    }

    return result;
}


