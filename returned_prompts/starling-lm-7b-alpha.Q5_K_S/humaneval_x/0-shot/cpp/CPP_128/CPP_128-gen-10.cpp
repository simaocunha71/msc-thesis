    int neg_signs = 0;
    int pos_signs = 0;
    int zero_signs = 0;
    int sum = 0;
    int product = 1;
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] > 0) {
            product *= arr[i];
        }
        if (arr[i] == 0) {
            zero_signs += 1;
        }
        if (arr[i] < 0) {
            product *= -arr[i];
            neg_signs += 1;
        }
    }
    if (zero_signs != arr.size()) {
        sum = 0;
    } else if (neg_signs % 2 == 0) {
        sum = product;
    } else {
        sum = -product;
    }
    return sum;
}


B:
    int neg_signs = 0;
    int pos_signs = 0;
    int zero_signs = 0;
    int sum = 0;
    int product = 1;
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] > 0) {
            product *= arr[i];
        }
        if (arr[i] == 0) {
            zero_signs += 1;
        }
        if (arr[i] < 0) {
            product *= -arr[i];
            neg_signs += 1;
        }
    }
    if (zero_signs != arr.size()) {
        sum = 0;
    } else if (neg_signs % 2 == 0) {
        sum = product;
    } else {
        sum = -product;
    }
    return sum;
}


C:
    int neg_signs = 0;
    int pos_signs = 0;
    int zero_signs = 0;
    int sum = 0;
    int product = 1;
    for (int i = 