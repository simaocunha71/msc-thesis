    vector<int> arr(n + 1);
    if (n < 0)
        return arr;
    arr[0] = 3;
    if (n == 0)
        return arr;
    arr[1] = 1;
    if (n == 1)
        return arr;
    arr[2] = 2;
    if (n == 2)
        return arr;
    for (int i = 3; i <= n; i++){
        if (i % 2 == 0)
            arr[i] = 1 + i / 2;
        else
            arr[i] = arr[i - 1] + arr[i - 2] + arr[i + 1];
    }
    return arr;
}
int main(){
    int n = 5;
    vector<int> result