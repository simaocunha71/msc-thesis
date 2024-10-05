    vector<int> result;
    for (boost::any val : values)
    {
        if (is_same<int, boost::any::value_type>::value)
        {
            result.push_back(boost::any_cast<int>(val));
        }
    }
    return result;
}  // https://www.boost.org/doc/libs/1_69_0/libs/any/doc/tutorial.html


