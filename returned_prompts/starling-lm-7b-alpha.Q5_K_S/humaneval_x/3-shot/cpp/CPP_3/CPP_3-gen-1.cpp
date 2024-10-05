    int balance=0;
    int i;
    for (i=0;i<operations.size();i++)
    {
        balance+=operations[i];
        if (balance<0)
        return true;
    }
    return false;
}


