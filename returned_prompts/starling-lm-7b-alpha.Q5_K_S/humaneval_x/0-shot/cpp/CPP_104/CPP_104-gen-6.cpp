    vector<int> ret;
    for (int i = 0; i < x.size(); i++) {
        if (check_decrease(x[i])) {
            ret.push_back(x[i]);
        }
    }
    sort(ret.begin(), ret.end(), greater<int>());
    return ret;
}

bool check_decrease(int x) {
    while (x) {
        if (x%10%2 == 0) {
            return false;
        }
        x /= 10;
    }
    return true;
}




















































































