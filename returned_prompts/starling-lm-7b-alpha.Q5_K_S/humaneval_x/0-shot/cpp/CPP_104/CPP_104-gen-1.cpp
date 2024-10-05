#include <vector>
#include <algorithm>

std::vector<int> unique_digits(std::vector<int> x) {
    std::vector<int> ret;
    for (int i = 0; i < x.size(); i++) {
        int tmp = x[i];
        bool flag = true;
        while (tmp > 0) {
            if (tmp % 10 % 2 == 0) {
                flag = false;
                break;
            }
            tmp /= 10;
        }
        if (flag) {
            ret.push_back(x[i]);
        }
    }
    std::sort(ret.begin(), ret.end());
    return ret;
}

int main() {
    std::vector<int> x = {15, 33, 1422, 1};
    std::vector<int> ret = unique_digits(x);
    for (int i = 0; i < ret.size(); i++) {
        printf("%d ", ret[i]);
    }
    return 0;
}











