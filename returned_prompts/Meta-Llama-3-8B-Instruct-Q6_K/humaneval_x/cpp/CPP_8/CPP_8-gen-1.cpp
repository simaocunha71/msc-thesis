    vector<int> result;
    int sum = 0;
    int product = 1;
    for (auto num: numbers) {
        sum += num;
        product *= num;
    }
    result.push_back(sum);
    result.push_back(product);
    return result;
}

B:
    vector<int> result;
    int sum = 0;
    int product = 1;
    if (numbers.empty()) {
        result.push_back(0);
        result.push_back(1);
    } else {
        for (auto num: numbers) {
            sum += num;
            product *= num;
        }
    }
    return result;
}

C:
    vector<int> result;
    int sum = 0;
    int product = 1;
    if (numbers.empty()) {
        result.push_back(0);
        result.push_back(1);
    } else {
        for (auto num: numbers) {
            sum += num;
            product *= num;
        }
        result.push_back(sum);
        result.push_back(product);
    }
    return result;
}

D:
    vector<int> result;
    int sum = 0;
    int product = 1;
    for (auto num: numbers) {
        sum += num;
        product *= num;
    }
    result.push_back(sum);
    result.push_back(product);
    return result;
}

E:
    vector<int> result;
    int sum = 0;
    int product = 1;
    if (numbers.empty()) {
        result.push_back(0);
        result.push_back(1);
    } else {
        for (auto num: numbers) {
            sum += num;
            product *= num;
        }
        result.push_back(sum);
        result.push_back(product);
    }
    return result;
}

F:
    vector<int> result;
    int sum = 0;
    int product = 1;
    if (numbers.empty()) {
        result.push_back(0);
        result.push_back(1);
    } else {
        for (auto num: numbers) {
            sum += num;
            product *= num;
        }
        result.push_back(sum);
        result.push_back(product);
    }
    return result;
}

G:
    vector<int> result;
    int sum = 0;
    int product = 1;
    if (numbers.empty()) {
        result.push_back(0);
        result.push_back(1);
    } else {
        for (auto num: numbers) {
            sum