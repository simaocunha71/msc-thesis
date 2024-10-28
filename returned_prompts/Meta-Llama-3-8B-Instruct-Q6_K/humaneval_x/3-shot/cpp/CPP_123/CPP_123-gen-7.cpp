    vector<int> collatz;
    int num = n;
    while(num != 1) {
        if(num % 2 == 0) {
            num /= 2;
        } else {
            num = num * 3 + 1;
        }
        collatz.push_back(num);
    }
    sort(collatz.begin(), collatz.end());
    vector<int> odd_collatz;
    for(int i = 0; i < collatz.size(); i++) {
        if(collatz[i] % 2 != 0) {
            odd_collatz.push_back(collatz[i]);
        }
    }
    return odd_collatz;
}
// or use a more efficient way to generate the sequence, such as memoization
vector<int> get_odd_collatz(int n) {
    vector<int> collatz;
    int num = n;
    map<int, int> memo;
    while(num != 1) {
        if(memo.find(num) != memo.end()) {
            num = memo[num];
        } else {
            if(num % 2 == 0) {
                memo[num] = num / 2;
                num /= 2;
            } else {
                memo[num] = num * 3 + 1;
                num = num * 3 + 1;
            }
        }
        collatz.push_back(num);
    }
    sort(collatz.begin(), collatz.end());
    vector<int> odd_collatz;
    for(int i = 0; i < collatz.size(); i++) {
        if(collatz[i] % 2 != 0) {
            odd_collatz.push_back(collatz[i]);
        }
    }
    return odd_collatz;
}
// or even more efficient way is to generate the sequence up to the maximum value of the sequence
// and then filter the odd numbers
vector<int> get_odd_collatz(int n) {
    int max_val = 1;
    while(max_val < n) {
        max_val *= 2;
    }
    vector<int> collatz;
    map<int, int> memo;
    int num = n;
    while(num > 1) {
        if(memo.find(num) != memo.end()) {
            num = memo[num];
        } else {
            if(num % 2 == 0) {
                memo[num] = num / 2;
                num /= 2;
            } else {
                memo[num] = num * 3 + 1;
                num