    float float_a = boost::any_cast<float>(a);
    float float_b = boost::any_cast<float>(b);

    if (float_a > float_b)
        return a;
    else if (float_a < float_b)
        return b;
    else
        return "None";
}
// alternative solution using boost::any_cast
boost::any compare_one(boost::any a,boost::any b){
    if (boost::any_cast<float>(a) > boost::any_cast<float>(b))
        return a;
    else if (boost::any_cast<float>(a) < boost::any_cast<float>(b))
        return b;
    else
        return "None";
}
// alternative solution using boost::lexical_cast
boost::any compare_one(boost::any a,boost::any b){
    string str_a = boost::lexical_cast<string>(a);
    string str_b = boost::lexical_cast<string>(b);

    float float_a = stof(str_a);
    float float_b = stof(str_b);

    if (float_a > float_b)
        return a;
    else if (float_a < float_b)
        return b;
    else
        return "None";
}
// alternative solution using boost::any_cast and string functions
boost::any compare_one(boost::any a,boost::any b){
    float float_a = boost::any_cast<float>(a);
    float float_b = boost::any_cast<float>(b);

    if (float_a > float_b)
        return a;
    else if (float_a < float_b)
        return b;
    else{
        string str_a = boost::any_cast<string>(a);
        string str_b = boost::any_cast<string>(b);

        if (str_a.length() > str_b.length())
            return a;
        else if (str_a.length() < str_b.length())
            return b;
        else
            return "None";
    }
}
// alternative solution using boost::any_cast and std::max_element
boost::any compare_one(boost::any a,boost::any b){
    float float_a = boost::any_cast<float>(a);
    float float_b = boost::any_cast<float>(b);

    if (float_a > float_b)
        return a;
    else if (float_a < float_b)
        return b;
    else{
        string str_a = boost::any_cast<string>(a);
        string str_b = boost::any_cast<string>(