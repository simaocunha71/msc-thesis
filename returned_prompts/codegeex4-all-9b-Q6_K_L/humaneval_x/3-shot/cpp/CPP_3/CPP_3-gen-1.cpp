    int sum=0;
    int i;
    for (i=0;i<operations.size();i++)
    {
        sum+=operations[i];
        if (sum<0)
        {
            return true;
        }
    }

    return false;
}

