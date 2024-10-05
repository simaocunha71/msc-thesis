/*
Write your code here.
*/
    int sum = 0;
    for (int i = 0; i < lst.size(); i++) {
        if (i % 3 == 0) {
            sum += lst[i] * lst[i];
        } else if (i % 4 == 0) {
            sum += lst[i] * lst[i] * lst[i];
        } else {
            sum += lst[i];
        }
    }
    return sum;
}

int main()
{
    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        vector<int> lst(n);
        for (int i = 0; i < n; i++) {
            cin >> lst[i];
        }
        int sum = sum_squares(lst);
        cout << sum << endl;
    }
    return 0;
}
