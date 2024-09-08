    sort(arr.begin(), arr.end(), [&](int a, int b){
        int count_a = 0, count_b = 0;
        while (a > 0){
            count_a += a % 2;
            a /= 2;
        }
        while (b > 0){
            count_b += b % 2;
            b /= 2;
        }
        if (count_a == count_b){
            return a < b;
        }
        return count_a < count_b;
    });
    return arr;
}
int main(){
    vector<int> arr = {1, 5, 2, 3, 4};
    vector<int> ans = sort_array(arr);
    for (int i = 0; i < ans.size(); i++){
        printf("%d ", ans[i]);
    }
    printf("\n");
    return 0;
}

