    double A=boost::get<double>(a);
    double B=boost::get<double>(b);
    string A_str=boost::get<string>(a);
    string B_str=boost::get<string>(b);
    if (A==B)
    return boost::any("None");
    if (A>B)
    return boost::any(A);
    return boost::any(B);
}



