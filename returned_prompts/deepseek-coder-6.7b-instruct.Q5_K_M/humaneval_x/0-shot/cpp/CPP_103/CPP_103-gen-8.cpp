if(n>m)
{
return "-1";
}
B:
int avg = (n+m)/2;
avg = floor(avg + 0.5);
C:
string binary_string = "";
while(avg > 0){
binary_string = to_string(avg%2) + binary_string;
avg /= 2;
}
D:
return binary_string;
}

Test cases:
cout << rounded_avg(1, 5) << endl;   // should print "11"
cout << rounded_avg(7, 5) << endl;   // should print "-1"
cout << rounded_avg(10, 20) << endl; // should print "1111"
cout << rounded_avg(20, 33) << endl; // should print "11010"

Output:
11
-1
1111
11010


*/

#include <iostream>
#include <cmath>
#include <string>
using namespace std;

string rounded_avg(int n, int m) {
    if (n > m) {
        return "-1";
    }

    int avg = (n + m) / 2;
    avg = floor(avg + 0.5);

    string binary_string = "";
    while (avg > 0) {
        binary_string = to_string(avg % 2) + binary_string;
        avg /= 2;
    }

    return binary_string;
}

int main() {
    cout << rounded_avg(1, 5) << endl;   // should print "11"
    cout << rounded_avg(7, 5) << endl;   // should print "-1"
    cout << rounded_avg(10, 20) << endl; // should print "1111"
    cout << rounded_avg(20, 33) << endl; // should print "11010"

    return 