    string binary_string = "";
    while(N > 0){
        int remainder = N%2;
        N = N/2;
        binary_string = to_string(remainder) + binary_string;
    }
    return binary_string;
}


int main(){
    int N;
    printf("Enter a number: ");
    scanf("%d", &N);
    string result = solve(N);
    printf("The binary equivalent is: %s", result.c_str());
    return 0;
}

*/

//C++ Code/Sum of digits in binary.cpp
#include<iostream>
#include<string>
using namespace std;

string solve(int N){
    string binary_string = "";
    while(N > 0){
        int remainder = N%2;
        N = N/2;
        binary_string = to_string(remainder) + binary_string;
    }
    return binary_string;
}

int main(){
    int N;
    cout<<"Enter a number: ";
    cin>>N;
    string result = solve(N);
    cout<<"The binary equivalent is: "<<result;
    return 0;
}

//C++ Code/Sum of digits in binary_v2.cpp
#include<iostream>
#include<string>
using namespace std;

int solve(int N){
    int sum = 0;
    while(N > 0){
        int remainder = N%10;
        N = N/10;
        sum += remainder;
    }
    return sum;
}

int main(){
    int N;
    cout<<"Enter a number: ";
    cin>>N;
    int result = solve(N);
    cout<<"The sum of digits is: "<<result;
    return 0;
}

//C++ Code/Sum of digits in binary_v3.cpp
#include<iostream>
#include<string>
using namespace std;

string solve(int N){
    string binary_string = "";
    while(N > 0){
        int