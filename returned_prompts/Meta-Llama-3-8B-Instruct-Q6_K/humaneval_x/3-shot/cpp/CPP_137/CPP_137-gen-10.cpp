    if (boost::any_cast<int>(a)==boost::any_cast<int>(b))
    return "None";
    if (boost::any_cast<int>(a)>boost::any_cast<int>(b))
    return a;
    if (boost::any_cast<int>(a)<boost::any_cast<int>(b))
    return b;
    if (boost::any_cast<float>(a)>boost::any_cast<float>(b))
    return a;
    if (boost::any_cast<float>(a)<boost::any_cast<float>(b))
    return b;
    if (boost::any_cast<string>(a)>boost::any_cast<string>(b))
    return a;
    if (boost::any_cast<string>(a)<boost::any_cast<string>(b))
    return b;
    return "None";
}