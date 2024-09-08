    vector<int> result;
    for (list_any::iterator it = values.begin(); it != values.end(); ++it) {
        if (boost::any_cast<int>(*it) != 0) {
            result.push_back(boost::any_cast<int>(*it));
        }
    }
    return result;
}

B:
    vector<int> filter_integers(list_any values){
        vector<int> result;
        for (list_any::iterator it = values.begin(); it != values.end(); ++it) {
            boost::any a = *it;
            if (boost::any_cast<int>(a) != 0) {
                result.push_back(boost::any_cast<int>(a));
            }
        }
        return result;
    }

C:
    vector<int> filter_integers(list_any values){
        vector<int> result;
        for (list_any::iterator it = values.begin(); it != values.end(); ++it) {
            boost::any a = *it;
            int n;
            if (boost::any_cast<int>(a, n)) {
                result.push_back(n);
            }
        }
        return result;
    }

D:
    vector<int> filter_integers(list_any values){
        vector<int> result;
        for (list_any::iterator it = values.begin(); it != values.end(); ++it) {
            boost::any a = *it;
            if (is_same(typeid(int), typeid(a)).name() == "i") {
                result.push_back(boost::any_cast<int>(a));
            }
        }
        return result;
    }

E:
    vector<int> filter_integers(list_any values){
        vector<int> result;
        for (list_any::iterator it = values.begin(); it != values.end(); ++it) {
            boost::any a = *it;
            if (boost::is_same<boost::any, int>::value) {
                result.push_back(boost::any_cast<int>(a));
            }
        }
        return result;
    }

F:
    vector<int> filter_integers(list_any values){
        vector<int> result;
        for (list_any::iterator it = values.begin(); it != values.end(); ++it) {
            boost::any a = *it;
            if (boost::any_cast<int>(a) != 0) {
                result.push_back(boost::any_cast<int>(a));
            } else {
                // ignore non-integer values
            }
        }
        return result;
    }  //