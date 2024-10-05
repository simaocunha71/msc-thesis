    string binary = "";
    while(N > 0){
        binary = to_string(N % 2) + binary;
        N /= 2;
    }
    return binary;
}

int main(){
    int N;
    scanf("%d",&N);
    string out_ = solve(N);
    cout << out_ << endl;
}

The code takes an integer and converts it to binary. It then prints out the binary number.
*/

#include<stdio.h>
#include<string>
using namespace std;

string solve(int N) {
    string binary = "";
    while(N > 0) {
        binary = to_string(N % 2) + binary;
        N /= 2;
    }
    return binary;
}

int main() {
    int N;
    scanf("%d", &N);
    string out_ = solve(N);
    cout << out_ << endl;
    return 0;
}

/*
