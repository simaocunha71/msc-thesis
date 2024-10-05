    int balance=0;
    for (int i=0;i<operations.size();i++)
    {
        balance+=operations[i];
        if (balance<0)
            return true;
    }
    return false;
}
// This function is not correct. It should return true as soon as the balance goes below zero.
// The corrected function would be:
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
