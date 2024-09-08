    vector<int> result;
    if (n == 1) {
        return result;
    }
    while (n != 1) {
        if (n % 2 == 0) {
            n = n / 2;
        } else {
            n = 3 * n + 1;
        }
        if (n % 2 != 0) {
            result.push_back(n);
        }
    }
    sort(result.begin(), result.end());
    return result;
}

B:
    vector<int> get_odd_collatz(int n) {
        vector<int> result;
        if (n == 1) {
            return result;
        }
        while (n != 1) {
            if (n % 2 == 0) {
                n = n / 2;
            } else {
                n = 3 * n + 1;
            }
            result.push_back(n);
        }
        result.erase(remove_if(result.begin(), result.end(), [](int x) { return x % 2 == 0; }), result.end());
        sort(result.begin(), result.end());
        return result;
    }

C:
    vector<int> get_odd_collatz(int n) {
        vector<int> result;
        if (n == 1) {
            return result;
        }
        while (n != 1) {
            if (n % 2 == 0) {
                n = n / 2;
            } else {
                n = 3 * n + 1;
            }
        }
        for (int i = n; i > 0; i--) {
            if (i % 2 != 0) {
                result.push_back(i);
            }
        }
        sort(result.begin(), result.end());
        return result;
    } 

D:
    vector<int> get_odd_collatz(int n) {
        vector<int> result;
        if (n == 1) {
            return result;
        }
        while (n != 1) {
            if (n % 2 == 0) {
                n = n / 2;
            } else {
                n = 3 * n + 1;
            }
        }
        for (int i = n; i > 0; i--) {
            if (i % 2 != 0) {
                result.push_back(i);
            }
        }
        reverse(result.begin(), result.end());
        return result;
    } 

E:
    vector<int>