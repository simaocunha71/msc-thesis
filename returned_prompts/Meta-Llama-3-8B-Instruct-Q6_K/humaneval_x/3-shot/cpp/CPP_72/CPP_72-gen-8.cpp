    if (q.size() != 0 && q != vector<int>(q.rbegin(), q.rend())) {
        return false;
    }
    int sum = 0;
    for (int i = 0; i < q.size(); i++) {
        sum += q[i];
    }
    if (sum > w) {
        return false;
    }
    return true;
}