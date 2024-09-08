    vector<int> result = nums;
    sort(result.begin(), result.end(), [&](int a, int int b) {
        int sumA = 0;
        int sumB = 0;
        for (int i = 0; i < abs(a); i++) {
            sumA += abs(a) % 10;
            abs(a) /= 10;
        }
        for (int i = 0; i < abs(b); i++) {
            sumB += abs(b) % 10;
            abs(b) /= 10;
        }
        if (sumA < sumB) {
            return true;
        }
        if (sumA > sumB) {
            return false;
        }
        return a < b;
    });
    return result;
}

B:
    // Using a lambda function
    sort(nums.begin(), nums.end(), [](int a, int b) {
        int sumA = 0;
        int sumB = 0;
        int absA = abs(a);
        int absB = abs(b);
        while (absA > 0) {
            sumA += absA % 10;
            absA /= 10;
        }
        while (absB > 0) {
            sumB += absB % 10;
            absB /= 10;
        }
        if (sumA < sumB) {
            return true;
        }
        if (sumA > sumB) {
            return false;
        }
        return a < b;
    });
    return nums;

C:
    // Using a custom comparator
    sort(nums.begin(), nums.end(), [](int a, int b) {
        int sumA = 0;
        int sumB = 0;
        int absA = abs(a);
        int absB = abs(b);
        while (absA > 0) {
            sumA += absA % 10;
            absA /= 10;
        }
        while (absB > 0) {
            sumB += absB % 10;
            absB /= 10;
        }
        if (sumA < sumB) {
            return true;
        }
        if (sumA > sumB) {
            return false;
        }
        return a < b;
    });
    return nums;

D:
    // Using a custom comparator
    sort(nums.begin(), nums.end(), [](int a, int b) {
        int sumA = 0