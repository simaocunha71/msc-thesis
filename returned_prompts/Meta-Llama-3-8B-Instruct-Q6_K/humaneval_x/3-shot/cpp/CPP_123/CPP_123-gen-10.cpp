    vector<int> result;
    int curr = n;
    while(curr != 1) {
        if(curr % 2 == 0) {
            curr /= 2;
        } else {
            curr = 3 * curr + 1;
        }
        if(curr % 2 != 0) {
            result.push_back(curr);
        }
    }
    sort(result.begin(), result.end());
    return result;
}  // 1 is not included in the result as per the problem description
