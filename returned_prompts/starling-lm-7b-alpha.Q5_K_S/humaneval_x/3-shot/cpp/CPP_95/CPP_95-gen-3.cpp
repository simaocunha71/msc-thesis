    for (auto it:dict)
    {
        if (it.first[0]>='a' && it.first[0]<='z')
        {
            if (it.second[0]>='A' && it.second[0]<='Z')
                return false;
        }
        if (it.first[0]>='A' && it.first[0]<='Z')
        {
            if (it.second[0]>='a' && it.second[0]<='z')
                return false;
        }
    }
    return true;
}


