    sort(arr.begin(), arr.end(), [](int a, int b){
        int countA = __builtin_popcount(abs(a));
        int countB = __builtin_popcount(abs(b));
        if(countA == countB)
            return a < b;
        return countA < countB;
    });
    return arr;
}

int main(){
    vector<int> arr = {1, 5, 2, 3, 4};
    vector<int> sorted_arr = sort_array(arr);
    for(int num: sorted_arr){
        printf("%d, ", num);
    }
    return 0;
}

