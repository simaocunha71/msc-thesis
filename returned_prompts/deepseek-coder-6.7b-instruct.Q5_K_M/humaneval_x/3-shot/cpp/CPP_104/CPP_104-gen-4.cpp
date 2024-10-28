    vector<int> result;
    for (auto num : x) {
        bool has_even_digit = false;
        int copy_num = num;
        while (copy_num > 0) {
            if ((copy_num % 10) % 2 == 0) {
                has_even_digit = true;
                break;
            }
            copy_num /= 10;
        }
        if (!has_even_digit) {
            result.push_back(num);
        }
    }
    sort(result.begin(), result.end());
    return result;
}

