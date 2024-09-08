#include <vector>
#include <string>
using namespace std;
vector<int> even_odd_count(int num) {
    string str = to_string(abs(num));
    int even_count = 0, odd_count = 0;
    for (char c : str) {
        if (c % 2 == 0) {
            even_count++;
        } else {
            odd_count++;
        }
    }
    return {even_count, odd_count};
}