    string result = "";
    for (int i=0; i<a.length(); i++)
    {
        result += ((a[i]-'0')^(b[i]-'0')) + '0';
    }
    return result;
}


