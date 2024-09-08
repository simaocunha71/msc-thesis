    if(array.empty()) {
        return array;
    }
    int sum = array[0] + array[array.size() - 1];
    if(sum % 2 == 0) {
        sort(array.begin(), array.end(), greater<int>());
    } else {
        sort(array.begin(), array.end());
    }
    return array;
}

int main() {
    vector<int> v = {2, 4, 3, 0, 1, 5};
    sort_array(v);
    for(int i = 0; i < v.size(); i++) {
        printf("%d ", v[i]);
    }
    printf("\n");
    return 0;
}

C:
6 5 4 3 2 1 0


