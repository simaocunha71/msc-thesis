    vector<int> result;
    for (int i = 0; i < numbers.size(); i++) {
        bool found = false;
        for (int j = 0; j < result.size(); j++) {
            if (numbers[i] == result[j]) {
                found = true;
                break;
            }
        }
        if (!found) {
            result.push_back(numbers[i]);
        }
    }
    return result;
}

int main() {
    vector<int> numbers = {1, 2, 3, 2, 4};
    vector<int> result = remove_duplicates(numbers);
    for (int i = 0; i < result.size(); i++) {
        printf("%d ", result[i]);
    }
    printf("\n");
    return 0;
}

B:
    vector<int> remove_duplicates(vector<int> numbers){
        vector<int> result;
        for (int i = 0; i < numbers.size(); i++) {
            if (find(result.begin(), result.end(), numbers[i]) == result.end()) {
                result.push_back(numbers[i]);
            }
        }
        return result;
    }
    int main() {
        vector<int> numbers = {1, 2, 3, 2, 4};
        vector<int> result = remove_duplicates(numbers);
        for (int i = 0; i < result.size(); i++) {
            printf("%d ", result[i]);
        }
        printf("\n");
        return 0;
    }
C:
    vector<int> remove_duplicates(vector<int> numbers){
        sort(numbers.begin(), numbers.end());
        vector<int> result;
        for (int i = 0; i < numbers.size(); i++) {
            if (i == 0 || numbers[i] != numbers[i - 1]) {
                result.push_back(numbers[i]);
            }
        }
        return result;
    }
    int main() {
        vector<int> numbers = {1, 2, 3, 2, 4};
        vector<int> result = remove_duplicates(numbers);
        for (int i = 0; i < result.size(); i++) {
            printf("%d ", result[i]);
        }
        printf("\n");
        return 0;
    }

D:
    vector<int> remove_duplicates(vector<int> numbers){
        unordered_map<int, bool> map;
        vector<int> result;
        for (int i = 0; i < numbers.size(); i++) {
            if