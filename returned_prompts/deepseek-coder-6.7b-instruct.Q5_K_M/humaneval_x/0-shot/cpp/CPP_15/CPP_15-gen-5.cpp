    string s = "";
    for(int i=0; i<=n; i++){
        s += to_string(i);
        if(i != n)
            s += " ";
    }
    return s;
}

int main(){
    int n;
    scanf("%d",&n);
    printf("%s",string_sequence(n).c_str());
    return 0;
}

*/

// C++ code to solve the problem
#include<iostream>
#include<sstream>
using namespace std;

string string_sequence(int n){
    stringstream ss;
    for(int i=0; i<=n; i++){
        ss << i;
        if(i != n)
            ss << " ";
    }
    return ss.str();
}

int main(){
    int n;
    cin >> n;
    cout << string_sequence(n);
    return 0;
}// C++ code to solve the problem
#include<iostream>
using namespace std;

bool is_prime(int n){
    if(n < 2) return false;
    for(int i = 2; i * i <= n; i++){
        if(n % i == 0) return false;
    }
    return true;
}

int main(){
    int n;
    cin >> n;
    cout << (is_prime(n) ? "Yes" : "No");
    return 0;
}

/*
