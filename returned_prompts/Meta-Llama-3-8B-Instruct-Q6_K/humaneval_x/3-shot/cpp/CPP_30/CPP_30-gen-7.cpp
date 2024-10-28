    vector<float> result;
    for (int i = 0; i < l.size(); i++) {
        if (l[i] > 0) {
            result.push_back(l[i]);
        }
    }
    return result;
}  // End of function get_positive.