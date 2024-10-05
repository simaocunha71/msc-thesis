    string result;
    for (int i=0;i<=n;i++)
    {
        if (result.size()>0)
            result += " ";
        result += to_string(i);
    }
    return result;
}