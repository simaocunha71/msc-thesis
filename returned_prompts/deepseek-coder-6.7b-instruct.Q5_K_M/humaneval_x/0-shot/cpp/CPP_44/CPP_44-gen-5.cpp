    string s = "";
    while(x > 0){
        s = to_string(x % base) + s;
        x /= base;
    }
    return s;
}
int main(){
    int x, base;
    printf("Enter the number and base:\n");
    scanf("%d %d", &x, &base);
    string result = change_base(x, base);
    printf("The result is: %s\n", result.c_str());
    return 0;
}

*/

#include<iostream>
#include<string>
using namespace std;

string change_base(int x,int base){
    string s = "";
    while(x > 0){
        s = to_string(x % base) + s;
        x /= base;
    }
    return s;
}

int main(){
    int x, base;
    cout<<"Enter the number and base:\n";
    cin>>x>>base;
    string result = change_base(x, base);
    cout<<"The result is: "<<result<<endl;
    return 0;
}

// CPP Program to convert a decimal number to binary using recursion

#include<iostream>
using namespace std;

void decToBinary(int n)
{
    if (n / 2 != 0) {
        decToBinary(n / 2);
    }
    cout<<n % 2;
}

int main()
{
    int n;
    cout << "Enter a decimal number:\n";
    cin >> n;
    decToBinary(n);
    return 0;
}

// CPP Program to convert a binary number to decimal

#include<iostream>
#include<cmath>
using namespace std;

int convertBinToDec(int bin)
{
    int dec = 0, i = 0, remainder;
    while (bin != 0)
    {
        remainder = bin % 10;
        bin /= 10;
        dec += remainder * pow(2, i);
        ++i;
    }