    int balance=0;
    int operation;
    int i;
    for (i=0;i<operations.size();i++)
    {
        operation=operations[i];
        balance+=operation;
        if (balance<0)
        return true;
    }
    return false;
}




