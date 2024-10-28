    if (array.size() < 2) {
        return array;
    }

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
int main(int argc, char **argv) {
    vector<int> array = { 2, 4, 3, 0, 1, 5, 6 };
    vector<int> res = sort_array(array);
    for (int i = 0; i < res.size(); i++) {
        printf("%d ", res[i]);
    }
}



