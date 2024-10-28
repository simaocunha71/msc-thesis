
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

bool has_close_elements(const std::vector<float>& numbers, float threshold){
    for (int i = 0; i < numbers.size(); i++)
        for (int j = i + 1; j < numbers.size(); j++)
            if (std::abs(numbers[i] - numbers[j]) < threshold)
                return true;
    return false;
}

std::vector<std::string> separate_paren_groups(const std::string& paren_string){
    std::vector<std::string> all_parens;
    std::string current_paren;
    int level = 0;
    for (char chr : paren_string){
        if (chr == '(')
            level++;
        else if (chr == ')')
            level--;
        current_paren += chr;
        if (level == 0){
            all_parens.push_back(current_paren);
            current_paren = "";
        }
    }
    return all_parens;
}

float truncate_number(float number){
    return number - int(number);
}

std::vector<std::vector<int>> get_row(const std::vector<std::vector<int>>& lst, int x){
    std::vector<std::vector<int>> all_coordinates;
    for (int i = 0; i < lst.size(); i++)
        for (int j = 0; j < lst[i].size(); j++)
            if (lst[i][j] == x){
                std::vector<int> current_coordinate = {i, j};
                all_coordinates.push_back(current_coordinate);
            }
    std::sort(all_coordinates.begin(), all_coordinates.end(), [](const std::vector<int>& a, const std::vector<int>& b){
        if (a[0] != b[0])
            return a[0] < b[0];
        return a[1] > b[1];
    });
    return all_coordinates;
}

int main(){
    std::cout << std::boolalpha;

    std::vector<float> numbers1