    vector<int> result;
    for(list_any::iterator it = values.begin(); it != values.end(); ++it)
    {
        if (is_integer(*it))
        {
            result.push_back(boost::any_cast<int>(*it));
        }
    }
    return result;
}

bool is_integer(boost::any a)
{
    return boost::any_cast<int>(a).empty() ? false : true;
}
