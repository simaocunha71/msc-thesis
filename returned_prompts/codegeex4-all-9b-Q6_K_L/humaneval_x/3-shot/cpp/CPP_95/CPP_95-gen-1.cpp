    bool isupper=true;
    bool islower=true;
    for (auto const& x : dict)
    {
    if (isupper==true)
        if (x.first[0]<=122 && x.first[0]>=65)
            isupper=true;
        else
            isupper=false;
    if (islower==true)
        if (x.first[0]<=90 && x.first[0]>=65)
            islower=false;
        else
            islower=true;
    }
    if (isupper==true || islower==true)
        return true;
    else
        return false;
}