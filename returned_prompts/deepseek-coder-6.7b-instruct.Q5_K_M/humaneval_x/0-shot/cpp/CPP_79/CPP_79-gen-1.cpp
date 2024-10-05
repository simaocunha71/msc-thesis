  string binary = "";
  while(decimal > 0){
    binary = to_string(decimal%2) + binary;
    decimal /= 2;
  }

  return "db" + binary + "db";
}

int main(){
  printf(decimal_to_binary(15).c_str());
  printf(decimal_to_binary(32).c_str());
}

//C++/decimalToBinary.cpp
#include<iostream>
#include<string>
using namespace std;

string decimalToBinary(int decimal){
  string binary = "";
  while(decimal > 0){
    binary = to_string(decimal % 2) + binary;
    decimal /= 2;
  }
  return binary;
}

int main(){
  int decimal;
  cout << "Enter a decimal number: ";
  cin >> decimal;
  cout << "The binary representation is: " << decimalToBinary(decimal) << endl;
  return 0;
}

//C++/decimalToBinaryString.cpp
#include<iostream>
#include<string>
using namespace std;

string decimalToBinaryString(int decimal){
  string binary = "";
  while(decimal > 0){
    binary = to_string(decimal % 2) + binary;
    decimal /= 2;
  }
  return "db" + binary + "db";
}

int main(){
  int decimal;
  cout << "Enter a decimal number: ";
  cin >> decimal;
  cout << "The binary representation is: " << decimalToBinaryString(decimal) << endl;
  return 0;
}

//C++/factorial.cpp
#include<iostream>
using namespace std;

int factorial(int n){
  if(n == 0){
    return 1;
  }else{
    return n * factorial(n-1);
  }
}

int main(){
  int n;
  cout << "Enter a number: ";
  cin >> n;
  cout << "The factorial of " << n << "