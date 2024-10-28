    float a_num=boost::any_cast<float>(a);
    float b_num=boost::any_cast<float>(b);
    if (a_num==b_num)
    return "None";
    if (a_num>b_num)
    return a;
    else
    return b;
}

