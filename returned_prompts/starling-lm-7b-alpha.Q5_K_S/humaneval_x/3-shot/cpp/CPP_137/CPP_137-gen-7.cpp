    if (a.type()==boost::type_id<int>())
    if (b.type()==boost::type_id<int>())
    {
    if (a.template get<int>()>b.template get<int>())
    return a;
    else
    return b;
    }
    else if (b.type()==boost::type_id<int>())
    return b;
    else if (a.type()==boost::type_id<float>())
    if (b.type()==boost::type_id<float>())
    {
    if (a.template get<float>()>b.template get<float>())
    return a;
    else
    return b;
    }
    else if (b.type()==boost::type_id<float>())
    return b;
    else if (a.type()==boost::type_id<string>())
    if (b.type()==boost::type_id<string>())
    {
    if (a.template get<string>().size()>b.template get<string>().size())
    return a;
    else if (a.template get<string>().size()<b.template get<string>().size())
    return b;
    else if (a.template get<string>()>b.template get<string>())
    return a;
    else if (a.template get<string>()<b.template get<string>())
    return b;
    else
    return "None";
    }
    else if (b.type()==boost::type_id<string>())
    return b;
    else if (a.type()==boost::type_id<string>())
    return a;
    else
    return "None";
    }
























































































