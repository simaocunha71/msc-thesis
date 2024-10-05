    if (a.type()==b.type())
    {
        if (a==b) return "None";
        else if (a<b) return b;
        else return a;
    }
    else 
    {
        float a1=float(boost::any_cast<float>(a));
        float b1=float(boost::any_cast<float>(b));
        if (a1<b1) return b;
        else return a;
    }
}

