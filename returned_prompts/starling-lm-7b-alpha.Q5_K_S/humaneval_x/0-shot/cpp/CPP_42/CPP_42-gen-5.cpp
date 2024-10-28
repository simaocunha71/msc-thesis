    for (int i=0; i<l.size(); i++) {
        l[i]++;
    }
    return l;
}
vector<int> incr_vector(vector<int> v) {
    return incr_list(v);
}

/*
Return vector with all elements multiplied by 2.
>>> double_vector({1, 2, 3})
{2, 4, 6}
>>> double_vector({5, 3, 5, 2, 3, 3, 9, 0, 123})
{10, 6, 10, 4, 6, 6, 18, 0, 246}
*/
vector<int> double_list(vector<int> l){
    for (int i=0; i<l.size(); i++) {
        l[i]=l[i]*2;
    }
    return l;
}
vector<int> double_vector(vector<int> v) {
    return double_list(v);
}

/*
Return vector with all elements multiplied by 3.
>>> triple_vector({1, 2, 3})
{3, 6, 9}
>>> triple_vector({5, 3, 5, 2, 3, 3, 9, 0, 123})
{15, 9, 15, 6, 9, 9, 27, 0, 369}
*/
vector<int> triple_list(vector<int> l){
    for (int i=0; i<l.size(); i++) {
        l[i]=l[i]*3;
    }
    return l;
}
vector<int> triple_vector(vector<int> v) {
    return triple_list(v);
}

/*
Return vector with all negative numbers replaced by 0.
>>> zero_neg_vector({1, 2, -3, 4})
{1, 2, 0, 4}
>>> zero_neg_vector({-3, -2, -5, 0, 3