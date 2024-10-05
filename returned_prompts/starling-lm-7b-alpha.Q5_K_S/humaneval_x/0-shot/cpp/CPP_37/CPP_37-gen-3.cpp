    for(int i = 0; i < l.size(); i++) {
        if(i % 2 == 0) {
            continue;
        }
        else {
            l.at(i) = l.at(i);
        }
    }
    for(int i = 1; i < l.size(); i++) {
        if(i % 2 == 0) {
            continue;
        }
        else {
            for(int j = i - 1; j >= 0; j--) {
                if(l.at(i) < l.at(j)) {
                    l.at(j + 1) = l.at(j);
                    l.at(j) = l.at(i);
                }
                else {
                    break;
                }
            }
        }
    }
    return l;
}


/*
This function takes two vectors, l and m, and returns true if the first element of l
is less than the first element of m, and false otherwise.
>>> is_less({1, 2, 3}, {4, 5, 6})
True
>>> is_less({1, 2, 3}, {3, 2, 1})
False
*/
bool is_less(vector<float> l, vector<float> m) {
    return l.at(0) < m.at(0);
}


/*
This function takes two vectors, l and m, and returns true if the two vectors are equal,
and false otherwise.
>>> are_equal({1, 2, 3}, {1, 2, 3})
True
>>> are_equal({1, 2, 3}, {3, 2, 1})
False
*/
bool are_equal(vector<float> l, vector<float> m) {
    if(l.size() != m.size()) {
        return false;
    }
    for(int i = 0; i < l.size(); i++) {
        if(l.at(i) != m.at(i)) {
            return false;
        }
    }