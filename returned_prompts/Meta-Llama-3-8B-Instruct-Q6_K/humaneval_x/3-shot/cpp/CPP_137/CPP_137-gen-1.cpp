    float fa,fb;
    string sa,sb;
    if (boost::any_cast<float>(a)!=boost::any_cast<float>(b)){
        fa=boost::any_cast<float>(a);
        fb=boost::any_cast<float>(b);
        if (fa>fb)
        return a;
        else
        return b;
    }
    else
    {
        sa=boost::any_cast<string>(a);
        sb=boost::any_cast<string>(b);
        if (sa==sb)
        return "None";
        else if (sa>sb)
        return a;
        else
        return b;
    }
}

