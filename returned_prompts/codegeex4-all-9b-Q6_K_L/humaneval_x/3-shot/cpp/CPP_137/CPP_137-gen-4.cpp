    float x,y;
    x=boost::any_cast<float>(a);
    y=boost::any_cast<float>(b);
    if (x==y)
    {
        boost::any ans;
        ans="None";
        return ans;
    }
    else if (x>y)
    {
        return a;
    }
    else
    {
        return b;
    }
}