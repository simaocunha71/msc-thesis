/*
1. Declare and initialize a vector of integers.
2. Start a while loop with the condition n > 1.
3. If n is odd, add n to the vector and then set n to n * 3 + 1.
4. If n is even, add n to the vector and then set n to n / 2.
5. After the loop ends, sort the vector and return it.
*/

vector<int> get_odd_collatz(int n){
    vector<int> oddCollatz;
    while(n > 1){
        if(n % 2 != 0){
            oddCollatz.push_back(n);
            n = n * 3 + 1;
        }
        else{
            oddCollatz.push_back(n);
            n = n / 2;
        }
    }
    sort(oddCollatz.begin(), oddCollatz.end());
    return oddCollatz;
}
B:
/*
1. Declare and initialize a vector of integers.
2. Start a while loop with the condition n > 1.
3. If n is odd, add n to the vector and then set n to n * 3 + 1.
4. If n is even, add n to the vector and then set n to n / 2.
5. After the loop ends, sort the vector and return it.
*/

vector<int> get_odd_collatz(int n){
    vector<int> oddCollatz;
    while(n > 1){
        if(n % 2 != 0){
            oddCollatz.push_back(n);
            n = n * 3 + 1;
        }
        else{
            oddCollatz.push_back(n);
            n = n / 2;
        }
    }
    sort(oddCollatz.begin(), oddCollatz.end());
    return oddCollatz;
}

C:
/*
1. Declare and initialize a vector of integers.
2. Start a while loop with the condition n > 1.
3. If n is odd, add n to the vector and then set n to n * 3 + 1.
4. If n is even, add n to the vector and then set n to n / 2.
5. After the loop ends, sort the vector and return it.
*/

vector<int> get_odd_collatz(int n){
    vector<int> oddCollatz;
    while(n > 1){
        if(n % 2 != 0){
            oddCollatz.push_back(n);
            n = n * 