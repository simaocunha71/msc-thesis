
#include <stdio.h>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

bool has_close_elements(vector<float> numbers, float threshold) {
    for (int i = 0; i < numbers.size(); i++)
        for (int j = i + 1; j < numbers.size(); j++)
            if (fabs(numbers[i] - numbers[j]) < threshold)
                return true;
    return false;
}

vector<string> separate_paren_groups(string paren_string) {
    vector<string> all_parens;
    string current_paren;
    int level = 0;
    char chr;
    for (size_t i = 0; i < paren_string.length(); i++) {
        chr = paren_string[i];
        if (chr == '(') {
            level += 1;
            current_paren += chr;
        } else if (chr == ')') {
            level -= 1;
            current_paren += chr;
            if (level == 0) {
                all_parens.push_back(current_paren);
                current_paren = "";
            }
        }
    }
    return all_parens;
}

float truncate_number(float number) {
    return number - floor(number);
}

vector<int> minPath(vector<vector<int>> grid, int k) {
    vector<int> res;
    vector<vector<int>> min_dist;
    int i, j;
    for (i = 0; i < grid.size(); i++)
        for (j = 0; j < grid.size(); j++)
            min_dist[i][j] = grid.size() * grid.size();
    return res;
}

int main() {
    printf("has_close_elements({1.0, 2.0, 3.0}, 0.5): %s\n",
           has_close_elements({1.0, 2.0, 3.0}, 0.5) ? "true" : "false");
    printf("has_close_elements({1.0, 2.8, 3.0, 4.0, 5.0, 2.0}, 0.3): %