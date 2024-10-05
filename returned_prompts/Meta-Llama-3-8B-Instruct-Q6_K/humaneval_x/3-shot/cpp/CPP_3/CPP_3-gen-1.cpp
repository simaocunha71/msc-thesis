    int balance=0;
    for (int i=0;i<operations.size();i++)
    {
        balance+=operations[i];
        if (balance<0)
        return true;
    }
    return false;
} // Note: No need to use a separate variable for balance here. We can directly use the operation as balance. For example, balance += operations[i]; will also work. But I have used a separate variable for better understanding.