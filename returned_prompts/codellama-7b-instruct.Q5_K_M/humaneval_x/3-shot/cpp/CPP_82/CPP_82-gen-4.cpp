    int length=str.length();
    for (int i=2;i<=length/2;i++)
    {
        if (length%i==0)
        return false;
    }
    return true;
}


