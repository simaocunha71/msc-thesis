    vector<int> result;
    if(numbers.empty()) {
        result.push_back(0);
        result.push_back(1);
    } else {
        int sum = 0;
        int product = 1;
        for(auto number : numbers) {
            sum += number;
            product *= number;
        }
        result.push_back(sum);
        result.push_back(product);
    }
    return result;
}

B:
    vector<int> sum_product(vector<int> numbers){
        vector<int> result;
        if(numbers.empty()) {
            result.push_back(0);
            result.push_back(1);
        } else {
            int sum = 0;
            int product = 1;
            for(int i = 0; i < numbers.size(); i++) {
                sum += numbers[i];
                product *= numbers[i];
            }
            result.push_back(sum);
            result.push_back(product);
        }
        return result;
    }

C:
    vector<int> sum_product(vector<int> numbers) {
        vector<int> result;
        if (numbers.empty()) {
            result.push_back(0);
            result.push_back(1);
        } else {
            int sum = 0;
            int product = 1;
            for (int i = 0; i < numbers.size(); i++) {
                sum += numbers[i];
                product *= numbers[i];
            }
            result.push_back(sum);
            result.push_back(product);
        }
        return result;
    }

D:
    vector<int> sum_product(vector<int> numbers) {
        vector<int> result;
        if (numbers.empty()) {
            result.push_back(0);
            result.push_back(1);
        } else {
            int sum = accumulate(numbers.begin(), numbers.end(), 0);
            int product = accumulate(numbers.begin(), numbers.end(), 1, multiplies<int>());
            result.push_back(sum);
            result.push_back(product);
        }
        return result;
    }

E:
    vector<int> sum_product(vector<int> numbers) {
        vector<int> result;
        if (numbers.empty()) {
            result.push_back(0);
            result.push_back(1);
        } else {
            int sum = 0;
            int product = 1;
            for (int number : numbers) {
                sum += number;
                product *= number;
            }
            result.push_back(sum);
            result.push_back(product);
        }
        return result;
    }

F:
    vector<int> sum_product(vector<int> numbers) {
       