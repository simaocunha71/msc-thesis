    vector<int> res(2, 0);
    num = abs(num);
    while (num) {
        int digit = num % 10;
        if (digit % 2 == 0)
            res[0]++;
        else
            res[1]++;
        num /= 10;
    }
    return res;
}

int main()
{
    vector<int> v = even_odd_count(-12);
    printf("%d %d\n", v[0], v[1]);
    v = even_odd_count(123);
    printf("%d %d\n", v[0], v[1]);
    return 0;
}

*/

//C++/EvenOrOdd.cpp
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

vector<int> even_odd_count(int num) {
    vector<int> res(2, 0);
    num = abs(num);
    while (num) {
        int digit = num % 10;
        if (digit % 2 == 0)
            res[0]++;
        else
            res[1]++;
        num /= 10;
    }
    return res;
}

int main() {
    vector<int> v = even_odd_count(-12);
    cout << v[0] << " " << v[1] << endl;
    v = even_odd_count(123);
    cout << v[0] << " " << v[1] << endl;
    return 0;
}

//C++/HexToDec.cpp
#include <iostream>
#include <cstdlib>
using namespace std;

int hexToDec(string hex) {
    return stoi(hex, nullptr, 16);
}

int main() {
    cout << hexToDec("A") << endl;
    cout << hexToDec("1A") << endl;
    cout << hexToDec("FF") << endl;
    return 