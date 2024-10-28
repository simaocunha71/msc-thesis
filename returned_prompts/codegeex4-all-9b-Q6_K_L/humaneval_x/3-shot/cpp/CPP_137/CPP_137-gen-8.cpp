    float fa,fb;
    string sa,sb;
    boost::any ans;
    if (a.type()==typeid(float))
    fa=boost::any_cast<float>(a);
    if (a.type()==typeid(string))
    {
        sa=boost::any_cast<string>(a);
        replace(sa.begin(),sa.end(),',','.');
        fa=atof(sa.c_str());
    }

    if (b.type()==typeid(float))
    fb=boost::any_cast<float>(b);
    if (b.type()==typeid(string))
    {
        sb=boost::any_cast<string>(b);
        replace(sb.begin(),sb.end(),',','.');
        fb=atof(sb.c_str());
    }

    if (fa==fb) ans="None";
    if (fa>fb) ans=fa;
    if (fb>fa) ans=fb;

    return ans;
}

