    sort(arr.begin(), arr.end(), [](int a, int b){
        int c = __builtin_popcount(abs(a));
        int d = __builtin_popcount(abs(b));
        return c == d ? a < b : c < d;
    });
    return arr;
}

int main(){
    vector<int> arr = {1, 5, 2, 3, 4};
    arr = sort_array(arr);
    for(int i=0; i<arr.size(); i++)
        printf("%d ", arr[i]);
    return 0;
}

The builtin_popcount function counts the number of set bits in the binary representation of a number. The sort function uses a lambda function to compare the number of ones in the binary representation of two numbers. If the number of ones is the same, it then compares the decimal values of the numbers.
*/

