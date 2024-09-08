bool monotonic(vector<float> l) {
    return all_of(l.begin(), l.end(), [&](float x) { return x >= l[0]; }) ||
           all_of(l.begin(), l.end(), [&](float x) { return x <= l[0]; });
}

B:
bool monotonic(vector<float> l) {
    if (l.size() < 2) {
        return true;
    }
    return all_of(l.begin() + 1, l.end(), [&](float x) { return x >= l[0]; }) ||
           all_of(l.begin() + 1, l.end(), [&](float x) { return x <= l[0]; });
}

C:
bool monotonic(vector<float> l) {
    if (l.size() < 2) {
        return true;
    }
    bool increasing = true;
    bool decreasing = true;
    for (int i = 1; i < l.size(); i++) {
        if (l[i] < l[i - 1]) {
            increasing = false;
        }
        if (l[i] > l[i - 1]) {
            decreasing = false;
        }
    }
    return increasing || decreasing;
}

D:
bool monotonic(vector<float> l) {
    return all_of(l.begin(), l.end(), [&](float x) { return x >= l[0]; }) ||
           all_of(l.begin(), l.end(), [&](float x) { return x <= l[0]; });
}

E:
bool monotonic(vector<float> l) {
    if (l.size() < 2) {
        return true;
    }
    bool increasing = true;
    bool decreasing = true;
    for (int i = 0; i < l.size() - 1; i++) {
        if (l[i] < l[i + 1]) {
            decreasing = false;
        }
        if (l[i] > l[i + 1]) {
            increasing = false;
        }
    }
    return increasing || decreasing;
}

F:
bool monotonic(vector<float> l) {
    return all_of(l.begin(), l.end(), [&](float x) { return x >= l[0]; }) ||
           all_of(l.begin(), l.end(), [&](float x) { return x <= l[0]; });
}

G:
bool monotonic(vector<float> l) {
    if (l.size() < 2) {
        return true;
    }
    return all_of(l.begin() + 