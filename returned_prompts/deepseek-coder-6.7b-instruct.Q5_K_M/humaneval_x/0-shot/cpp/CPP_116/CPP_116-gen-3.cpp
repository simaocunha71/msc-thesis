    sort(arr.begin(), arr.end(), [](int a, int b){
        int cnt_a = __builtin_popcount(abs(a));
        int cnt_b = __builtin_popcount(abs(b));
        if(cnt_a == cnt_b)
            return a < b;
        return cnt_a < cnt_b;
    });
    return arr;
}

int main(){
    vector<int> arr = {1, 5, 2, 3, 4};
    vector<int> sorted_arr = sort_array(arr);

    for(int i=0; i<sorted_arr.size(); i++){
        printf("%d ", sorted_arr[i]);
    }

    return 0;
}

The __builtin_popcount function is a GCC built-in function that returns the number of 1s in the binary representation of a number.
The abs function is used to handle negative numbers.
*/

