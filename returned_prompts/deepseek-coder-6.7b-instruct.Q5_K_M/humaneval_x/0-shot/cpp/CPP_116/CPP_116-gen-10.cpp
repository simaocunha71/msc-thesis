    sort(arr.begin(), arr.end(), [](int a, int b){
        int countA = __builtin_popcount(abs(a));
        int countB = __builtin_popcount(abs(b));
        if(countA == countB)
            return a < b;
        return countA < countB;
    });
    return arr;
}

int main() {
    vector<int> arr = {1, 5, 2, 3, 4};
    vector<int> res = sort_array(arr);
    for(int i = 0; i < res.size(); i++)
        printf("%d ", res[i]);
    return 0;
}

/*
