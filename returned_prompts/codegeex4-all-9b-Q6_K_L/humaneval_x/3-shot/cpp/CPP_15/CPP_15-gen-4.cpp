    string result="";
    for (int i=0;i<=n;i++)
    {
        result=result+to_string(i);
        if (i<n)
        result=result+" ";
    }
    return result;
}

