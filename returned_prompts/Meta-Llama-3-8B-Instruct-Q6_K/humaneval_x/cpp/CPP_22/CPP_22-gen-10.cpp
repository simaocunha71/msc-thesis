    vector<int> result;
    for(list_any::iterator it = values.begin(); it != values.end(); ++it) {
        boost::any &any = *it;
        if (boost::any_cast<int>(&any)) {
            result.push_back(boost::any_cast<int>(any));
        }
    }
    return result;
}

