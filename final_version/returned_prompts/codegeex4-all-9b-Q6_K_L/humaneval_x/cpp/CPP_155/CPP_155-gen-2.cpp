#include <iostream>
#include <vector>
using namespace std;

vector<int> even_odd_count(int num) {
    int even = 0, odd = 0;
    string numStr = to_string(abs(num));
    for (char c : numStr) {
        int digit = c - '0';
        if (digit % 2 == 0) {
            even++;
        } else {
            odd++;
        }
    }
    return {even, odd};
}

B:
#include <iostream>
#include <vector>
using namespace std;

vector<int> even_odd_count(int num) {
    int even = 0, odd = 0;
    string numStr = to_string(abs(num));
    for (char c : numStr) {
        int digit = c - '0';
        if (digit % 2 == 0) {
            even++;
        } else {
            odd++;
        }
    }
    return {even, odd};
}

C:
#include <iostream>
#include <vector>
using namespace std;

vector<int> even_odd_count(int num) {
    int even = 0, odd = 0;
    string numStr = to_string(abs(num));
    for (char c : numStr) {
        int digit = c - '0';
        if (digit % 2 == 0) {
            even++;
        } else {
            odd++;
        }
    }
    return {even, odd};
}

D:
#include <iostream>
#include <vector>
using namespace std;

vector<int> even_odd_count(int num) {
    int even = 0, odd = 0;
    string numStr = to_string(abs(num));
    for (char c : numStr) {
        int digit = c - '0';
        if (digit % 2 == 0) {
            even++;
        } else {
            odd++;
        }
    }
    return {even, odd};
}

C 和 D 两个选项是重复的，应该被排除。

因此，正确的答案是：
A 和 B

A 和 B 都是正确的，但是 B 更具可读性，因为它使用了 `std::string` 的迭代器来遍历数字的每一位，而不是将数字转换为字符串并使用 `std::string::size()` 函数来获取数字的位数。这使得代码更简洁，更易于理解。
