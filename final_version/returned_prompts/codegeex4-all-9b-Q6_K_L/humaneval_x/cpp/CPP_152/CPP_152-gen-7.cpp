```cpp
#include <iostream>
#include <vector>
#include <cmath>

std::vector<int> compare(const std::vector<int>& game, const std::vector<int>& guess) {
    std::vector<int> result;
    for (size_t i = 0; i < game.size(); ++i) {
        result.push_back(std::abs(game[i] - guess[i]));
    }
    return result;
}

int main() {
    std::vector<int> game = {1, 2, 3, 4, 5, 1};
    std::vector<int> guess = {1, 2, 3, 4, 2, -2};
    std::vector<int> result = compare(game, guess);

    for (int num : result) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    return 0;
}
```