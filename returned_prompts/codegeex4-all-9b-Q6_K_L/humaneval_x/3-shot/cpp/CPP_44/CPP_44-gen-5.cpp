    string new_x="";
    string bases="0123456789";
    while (x>0)
    {
        new_x=bases[x%base]+new_x;
        x/=base;
    }
    return new_x;
}

