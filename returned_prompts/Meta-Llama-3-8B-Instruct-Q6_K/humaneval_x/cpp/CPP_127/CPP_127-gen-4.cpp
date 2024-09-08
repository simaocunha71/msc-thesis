    int start = (interval1[0] <= interval2[0]) ? interval1[0] : interval2[0];
    int end = (interval1[1] >= interval2[1]) ? interval1[1] : interval2[1];

    if (start > end) {
        return "NO";
    }

    int length = end - start + 1;
    vector<bool> isPrime(length + 1);
    isPrime[0] = isPrime[1] = false;
    for (int i = 2; i <= length; i++) {
        isPrime[i] = true;
    }

    for (int i = 2; i * i <= length; i++) {
        if (isPrime[i]) {
            for (int j = i * i; j <= length; j += i) {
                isPrime[j] = false;
            }
        }
    }

    for (int i = 2; i <= length; i++) {
        if (isPrime[i]) {
            return "YES";
        }
    }

    return "NO";
}

int main()
{
    //Test cases
    vector<int> interval1 = {1, 3};
    vector<int> interval2 = {2, 4};
    cout<<intersection(interval1, interval2)<<endl;
    vector<int> interval3 = {-1, 1};
    vector<int> interval4 = {0, 4};
    cout<<intersection(interval3, interval4)<<endl;
    vector<int> interval5 = {-3, -1};
    vector<int> interval6 = {-5, 5};
    cout<<intersection(interval5, interval6)<<endl;
    return 0;
}
*/
Answer:
Here is the complete code that implements the solution:

```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

string intersection(vector<int> interval1, vector<int> interval2) {
    int start = (interval1[0] <= interval2[0]) ? interval1[0] : interval2[0];
    int end = (interval1[1] >= interval2[1]) ? interval1[1] : interval2[1];

    if (start > end) {
        return "NO";
    }

    int length = end - start + 1;
    vector<bool> isPrime(length + 1);
    isPrime[0] = isPrime[1