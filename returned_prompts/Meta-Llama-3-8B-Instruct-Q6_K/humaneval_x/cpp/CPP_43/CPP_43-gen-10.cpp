    if (l.size() < 2) {
        return false;
    }
    set<int> s;
    for (int i = 0; i < l.size(); i++) {
        if (s.find(-l[i]) != s.end()) {
            return true;
        }
        s.insert(l[i]);
    }
    return false;
}

int main() {
    vector<int> l = {2, 4, -5, 3, 5, 7};
    printf("%d\n", pairs_sum_to_zero(l));
    return 0;
}

