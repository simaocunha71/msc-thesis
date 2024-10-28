    int sum = 0;
    for (int i = 0; i < array.size(); i++) {
        sum += array[i];
    }
    if (sum % 2 == 0) {
        sort(array.begin(), array.end(), greater<int>());
    } else {
        sort(array.begin(), array.end());
    }
    return array;
}

int main() {
    vector<int> a;
    vector<int> a = {2, 4, 3, 0, 1, 5};
    vector<int> a = {2, 4, 3, 0, 1, 5, 6};
    vector<int> b;
    vector<int> a = {};
    vector<int> a = {5};
    vector<int> a = {2, 4, 3, 0, 1, 5};
    vector<int> a = {2, 4, 3, 0, 1, 5, 6};
    vector<int> b;
    vector<int> a = {};
    vector<int> a = {5};
    vector<int> a = {2, 4, 3, 0, 1, 5};
    vector<int> a = {2, 4, 3, 0, 1, 5, 6};
    vector<int> b;
    vector<int> a = {};
    vector<int> a = {5};
    vector<int> a = {2, 4, 3, 0, 1, 5};
    vector<int> a = {2, 4, 3, 0, 1, 5, 6};
    vector<int> b;
    vector<int> a = {};
    vector<int> a = {5};
    vector<int> a = {2, 4, 3, 0, 1, 5};
    vector<int> a = {2, 4, 3, 0, 1, 5, 6};
    vector<int> b;
    vector<int> a = {};