    vector<int> odd_numbers;
    int num = n;
    while (num != 1) {
        if (num % 2 != 0) {
            odd_numbers.push_back(num);
        }
        if (num % 2 == 0) {
            num = num / 2;
        } else {
            num = num * 3 + 1;
        }
    }
    return odd_numbers;
}
// sort the vector in ascending order
sort(odd_numbers.begin(), odd_numbers.end());
return odd_numbers;
}*/



