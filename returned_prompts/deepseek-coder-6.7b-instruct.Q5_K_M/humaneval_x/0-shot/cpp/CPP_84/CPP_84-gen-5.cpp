    int digit;
    string binary = "";
    while(N > 0){
        digit = N % 2;
        binary = to_string(digit) + binary;
        N = N / 2;
    }
    return binary;
}

int main(){
    int N;
    scanf("%d", &N);
    printf("%s", solve(N).c_str());
    return 0;
}

*/

#include <iostream>
#include <string>
using namespace std;

string solve(int N) {
    int digit;
    string binary = "";
    while(N > 0) {
        digit = N % 2;
        binary = to_string(digit) + binary;
        N = N / 2;
    }
    return binary;
}

int main() {
    int N;
    cin >> N;
    cout << solve(N);
    return 0;
}/*

