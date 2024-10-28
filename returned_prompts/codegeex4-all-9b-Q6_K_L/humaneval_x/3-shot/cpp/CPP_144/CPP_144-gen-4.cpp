    int numerator_x = atoi(x.substr(0,x.find("/")).c_str());
    int denominator_x = atoi(x.substr(x.find("/")+1).c_str());
    int numerator_n = atoi(n.substr(0,n.find("/")).c_str());
    int denominator_n = atoi(n.substr(n.find("/")+1).c_str());

    if (numerator_x*denominator_n==denominator_x*numerator_n)
    return true;

    return false;
}

