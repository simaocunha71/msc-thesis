    vector<int> result;
    int count_even = 0;
    int count_odd = 0;
    while (num != 0) {
        int digit = num % 10;
        if (digit % 2 == 0) {
            count_even++;
        } else {
            count_odd++;
        }
        num /= 10;
    }
    result.push_back(count_even);
    result.push_back(count_odd);
    return result;
}

int main() {
    int num;
    cout << "Enter a number: ";
    cin >> num;
    vector<int> result = even_odd_count(num);
    cout << "Number of even digits: " << result[0] << endl;
    cout << "Number of odd digits: " << result[1] << endl;
    return 0;
}
