    int sum = 0, sign = 1;
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] == 0) {
            sign = 0;
        } else {
            sign *= (arr[i] > 0) ? 1 : -1;
        }
        sum += abs(arr[i]);
    }
    if (arr.size() == 0) {
        return -32768;
    }
    return sum * sign;
}

B:
    int prod_signs(vector<int> arr){
    int sum = 0;
    int sign = 1;
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] == 0) {
            sign = 0;
        } else {
            sign *= (arr[i] > 0) ? 1 : -1;
        }
        sum += abs(arr[i]);
    }
    if (arr.size() == 0) {
        return -32768;
    }
    return sum * sign;
}
C:
    int prod_signs(vector<int> arr){
    if (arr.size() == 0) {
        return -32768;
    }
    int sum = 0;
    int sign = 1;
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] > 0) {
            sign *= 1;
        } else if (arr[i] < 0) {
            sign *= -1;
        }
        sum += abs(arr[i]);
    }
    return sum * sign;
}
D:
    int prod_signs(vector<int> arr){
    if (arr.size() == 0) {
        return -32768;
    }
    int sum = 0;
    for (int i = 0; i < arr.size(); i++) {
        sum += abs(arr[i]);
    }
    int sign = 1;
    for (int i = 0; i < arr.size(); i++) {
        sign *= (arr[i] > 0) ? 1 : -1;
    }
    return sum * sign;
}
E:
    int prod_signs(vector<int> arr){
    if (arr.empty()) {
        return -32768;
    }
    int sum = 0;
    int sign = 1;
    for (int i = 0; i < arr.size(); i++)