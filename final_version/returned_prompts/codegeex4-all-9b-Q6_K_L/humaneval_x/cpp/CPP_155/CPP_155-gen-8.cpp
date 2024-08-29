#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    vector<int> even_odd_count(int num) {
        int even = 0, odd = 0;
        int n = abs(num);
        while (n > 0) {
            int digit = n % 10;
            if (digit % 2 == 0)
                even++;
            else
                odd++;
            n /= 10;
        }
        return vector<int>{even, odd};
    }
};