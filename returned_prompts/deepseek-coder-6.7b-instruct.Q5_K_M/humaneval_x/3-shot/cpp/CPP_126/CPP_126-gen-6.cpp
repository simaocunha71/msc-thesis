    for (int i = 1; i < lst.size(); ++i)
    {
        if (lst[i-1] >= lst[i])
        {
            return false;
        }
    }
    return true;
}


