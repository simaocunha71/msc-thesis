    int i;
    float upper=0.0,lower=0.0;
    for  (i=0;i<ext.size();i++)
    {
        if  (isupper(ext[i]))
            upper+=1;
        if  (islower(ext[i]))
            lower+=1;
    }
    return upper-lower;
}


