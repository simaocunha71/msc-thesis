    vector<int> result;
    int sum = 0;
    int product = 1;
    for(int i: numbers){
        sum += i;
        product *= i;
    }
    result.push_back(sum);
    result.push_back(product);
    return result;
}
int main() {
    vector<int> numbers = {1, 2, 3, 4};
    vector<int> result = sum_product(numbers);
    printf("Sum: %d, Product: %d\n", result[0], result[1]);
    return 0;
}

B:
    vector<int> sum_product(map<int, int> numbers) {
        int sum = 0;
        int product = 1;
        for(auto it = numbers.begin(); it != numbers.end(); it++) {
            sum += it->second;
            product *= it->second;
        }
        return {sum, product};
    }

    int main() {
        map<int, int> numbers = {{1, 1}, {2, 2}, {3, 3}, {4, 4}};
        vector<int> result = sum_product(numbers);
        cout << "Sum: " << result[0] << ", Product: " << result[1] << endl;
        return 0;
    }

C:
    vector<int> sum_product(map<int, int> numbers) {
        int sum = 0;
        int product = 1;
        for(auto it = numbers.begin(); it != numbers.end(); it++) {
            sum += it->second;
            product *= it->second;
        }
        return {sum, product};
    }

    int main() {
        map<int, int> numbers;
        numbers[1] = 1;
        numbers[2] = 2;
        numbers[3] = 3;
        numbers[4] = 4;
        vector<int> result = sum_product(numbers);
        cout << "Sum: " << result[0] << ", Product: " << result[1] << endl;
        return 0;
    }

D:
    #include <vector>
    #include <numeric>
    using namespace std;

    vector<int> sum_product(vector<int> numbers) {
        return {accumulate(numbers.begin(), numbers.end(), 0), 1};
    }

    int main() {
        vector<int> numbers = {1, 2, 3, 4};
        vector<int> result = sum_product(numbers);
        cout