    int balance=0;
    for (int i=0;i<operations.size();i++)
    {
        balance+=operations[i];
        if (balance<0)
            return true;
    }
    return false;
}  // This function will return true if the balance of the account falls below zero at any point and false otherwise.