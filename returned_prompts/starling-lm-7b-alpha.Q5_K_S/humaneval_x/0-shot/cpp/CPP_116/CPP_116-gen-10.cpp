    vector<int> result = arr;
    sort(result.begin(), result.end());
    return result;
}

vector<int> sort_vector(vector<int> arr){
    vector<int> result = arr;
    sort(result.begin(), result.end(), [](int a, int b){
        if (count_ones(a) == count_ones(b)){
            return a < b;
        } else {
            return count_ones(a) < count_ones(b);
        }
    });
    return result;
}

int count_ones(int n) {
    int count = 0;
    while (n) {
        count += n & 1;
        n >>= 1;
    }
    return count;
}


/*
    sort_vector({1, 5, 2, 3, 4})
    {1, 2, 3, 4, 5}

    sort_vector({-2, -3, -4, -5, -6})
    {-6, -5, -4, -3, -2}

    sort_vector({1, 0, 2, 3, 4})
    {0, 1, 2, 3, 4}
*/













































































































































































































