    string binary = "";
    int sum = 0;
    while(N){
        sum += N % 10;
        N /= 10;
    }
    while(sum){
        binary = to_string(sum % 2) + binary;
        sum /= 2;
    }
    return binary;
}

int main(){
    int N;
    printf("Enter a positive integer N: ");
    scanf("%d", &N);
    printf("The sum of digits in binary: %s\n", solve(N).c_str());
    return 0;
}

*/
#include<iostream>
#include<string>
using namespace std;
string solve(int N){
    string binary = "";
    int sum = 0;
    while(N){
        sum += N % 10;
        N /= 10;
    }
    while(sum){
        binary = to_string(sum % 2) + binary;
        sum /= 2;
    }
    return binary;
}

int main(){
    int N;
    cout<<"Enter a positive integer N: ";
    cin>>N;
    cout<<"The sum of digits in binary: "<<solve(N)<<endl;
    return 0;
}

//C++/sum_of_digits_in_binary/test.cpp
#include<iostream>
#include<cassert>
#include "sum_of_digits_in_binary.cpp"
using namespace std;

int main(){
    assert(solve(1000) == "1");
    assert(solve(150) == "110");
    assert(solve(147) == "1100");
    cout<<"All test cases passed"<<endl;
    return 0;
}

//C++/sum_of_digits_in_binary/test_main.cpp
#include<iostream>
#include "sum_of_digits_in_binary.cpp"
using namespace std;

int main(){
    int N;
    cout<<"