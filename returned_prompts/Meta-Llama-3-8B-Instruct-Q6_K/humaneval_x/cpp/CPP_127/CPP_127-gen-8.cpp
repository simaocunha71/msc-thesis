    if(interval1[1] < interval2[0] || interval2[1] < interval1[0])
        return "NO"; // intervals do not intersect
    int start = max(interval1[0], interval2[0]);
    int end = min(interval1[1], interval2[1]);
    if(end - start > 1)
        return "YES";
    else return "NO";
}

int main()
{
    vector<int> interval1={1, 2};
    vector<int> interval2={2, 3};
    printf("%s\n",intersection(interval1,interval2).c_str());

    interval1={-1, 1};
    interval2={0, 4};
    printf("%s\n",intersection(interval1,interval2).c_str());

    interval1={-3, -1};
    interval2={-5, 5};
    printf("%s\n",intersection(interval1,interval2).c_str());

    return 0;
}
B:
```c
#include <iostream>
#include <vector>
#include <string>

using namespace std;

string intersection(vector<int> interval1, vector<int> interval2) {
    if (interval1[1] < interval2[0] || interval2[1] < interval1[0])
        return "NO"; // intervals do not intersect

    int start = max(interval1[0], interval2[0]);
    int end = min(interval1[1], interval2[1]);

    if (end - start > 1) {
        for (int i = 2; i <= end - start; i++) {
            if (isPrime(i))
                return "YES";
        }
        return "NO";
    }
    else return "NO";
}

bool isPrime(int n) {
    if (n <= 1) return false;
    for (int i = 2; i * i <= n; i++)
        if (n % i == 0) return false;
    return true;
}

int main() {
    vector<int> interval1 = {1, 2};
    vector<int> interval2 = {2, 3};
    cout << intersection(interval1, interval2) << endl;

    interval1 = { -1, 1 };
    interval2 = { 0, 4 };
    cout << intersection(interval1, interval2) << endl;

    interval1 = { -3, -1 };
    interval