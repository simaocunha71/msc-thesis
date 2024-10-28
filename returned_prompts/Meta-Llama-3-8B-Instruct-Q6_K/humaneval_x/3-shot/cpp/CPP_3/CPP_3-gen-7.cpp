    int balance=0;
    for (int i=0;i<operations.size();i++)
    {
        balance+=operations[i];
        if (balance<0)
        return true;
    }
    return false;
}
//or
bool below_zero(vector<int> operations){
    int balance=0;
    for (int operation : operations)
    {
        balance+=operation;
        if (balance<0)
        return true;
    }
    return false;
}
//or
bool below_zero(vector<int> operations){
    int balance=0;
    for (int i=0;i<operations.size();i++)
    {
        balance+=operations[i];
        if (balance<0)
        return true;
    }
    return false;
} 

