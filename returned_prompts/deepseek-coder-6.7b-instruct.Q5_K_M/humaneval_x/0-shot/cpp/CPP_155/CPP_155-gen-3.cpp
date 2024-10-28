    vector<int> res(2,0);
    num = abs(num);
    while(num){
        if((num%10)%2==0)
            res[0]++;
        else
            res[1]++;
        num /= 10;
    }
    return res;
}

int main(){
    int n;
    scanf("%d",&n);
    vector<int> res = even_odd_count(n);
    printf("{%d, %d}",res[0],res[1]);
    return 0;
}

The code above will count the number of even and odd digits in an integer and return them in a vector. It takes an integer as input, calculates the absolute value of the number to ensure it's positive, then loops through each digit in the number. If the digit is even, it increments the first element of the vector. If the digit is odd, it increments the second element of the vector. Finally, it returns the vector.

The main function reads the integer from the standard input, calls the even_odd_count function with this integer as argument, and then prints the returned vector.
*/

//S:
vector<int> even_odd_count(int num){
    vector<int> res(2,0);
    num = abs(num);
    while(num){
        if((num%10)%2==0)
            res[0]++;
        else
            res[1]++;
        num /= 10;
    }
    return res;
}

//T:
#include<iostream>
#include<vector>
using namespace std;

int main(){
    int n;
    cin >> n;
    vector<int> res = even_odd_count(n);
    cout << "{" << res[0] << ", " << res[1] << "}";
    return 0;
}

//P:
/*
Given an integer. return a vector that has the number of even and odd digits respectively.

 Example:
    even_odd_count(-12) ==> 返回 {1, 1}
    even_odd