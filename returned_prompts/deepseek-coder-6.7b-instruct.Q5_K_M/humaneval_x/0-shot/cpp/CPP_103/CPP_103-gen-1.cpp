if(n > m)
{
return "-1";
}

B:
int avg = round((n + m)/2.0);

C:
string binary = "";
while(avg > 0)
{
binary = to_string(avg % 2) + binary;
avg /= 2;
}
return binary;
}
int main()
{
int n,m;
scanf("%d %d",&n,&m);
cout<<rounded_avg(n,m);
return 0;
}
*/

#include <iostream>
#include <cmath>
#include <string>
using namespace std;

string rounded_avg(int n, int m) {
    if (n > m) {
        return "-1";
    }

    int avg = round((n + m) / 2.0);

    string binary = "";
    while (avg > 0) {
        binary = to_string(avg % 2) + binary;
        avg /= 2;
    }
    return binary;
}

int main() {
    int n, m;
    cin >> n >> m;
    cout << rounded_avg(n, m);
    return 0;
}

//C++/rounded_avg.cpp
#include <iostream>
#include <cmath>
#include <string>
using namespace std;

string rounded_avg(int n, int m) {
    if (n > m) {
        return "-1";
    }

    int avg = round((n + m) / 2.0);

    string binary = "";
    while (avg > 0) {
        binary = to_string(avg % 2) + binary;
        avg /= 2;
    }
    return binary;
}

int main() {
    int n, m;
    cin >> n >> m;
    cout << rounded_avg(n, m);
    return 0;
}

//C++/test.cpp
#include <iostream>
#include <