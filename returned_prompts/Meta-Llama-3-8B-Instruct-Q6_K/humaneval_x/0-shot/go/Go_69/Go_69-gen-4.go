    if(n > m){
        return "-1";
    }
    int sum = 0;
    int count = 0;
    for(int i = n; i <= m; i++){
        sum += i;
        count++;
    }
    double avg = (double)sum / count;
    avg = floor(avg + 0.5);
    string str = to_string(avg);
    int binary = 0;
    for(int i = 0; i < str.length(); i++){
        if(str[i] == '1'){
            binary |= 1 << (str.length() - i - 1);
        }
    }
    string binaryStr = "";
    while(binary > 0){
        binaryStr = to_string(binary % 2) + binaryStr;
        binary /= 2;
    }
    return binaryStr;
}

int main()
{
    cout<<rounded_avg(1,5)<<endl;
    cout<<rounded_avg(7,5)<<endl;
    cout<<rounded_avg(10,20)<<endl;
    cout<<rounded_avg(20,33)<<endl;
    return 0;
}

S:
The problem is asking to find the average of two given numbers and then convert it to binary. If the first number is greater than the second, return "-1".

Here is the solution in C++:

```cpp
#include <iostream>
#include <cmath>
#include <string>

using namespace std;

string rounded_avg(int n, int m) {
    if (n > m) {
        return "-1";
    }
    int sum = 0;
    for (int i = n; i <= m; i++) {
        sum += i;
    }
    double avg = (double) sum / (m - n + 1);
    avg = floor(avg + 0.5);
    string str = to_string(avg);
    int binary = 0;
    for (int i = 0; i < str.length(); i++) {
        if (str[i] == '1') {
            binary |= 1 << (str.length() - i - 1);
        }
    }
    string binaryStr = "";
    while (binary > 0) {
        binaryStr = to_string(binary % 2) + binaryStr;
        binary /= 2;
    }
    return binaryStr;
}

int main() {
    cout << rounded_avg(1, 5) << endl;
    cout << rounded_avg(7, 5) <<