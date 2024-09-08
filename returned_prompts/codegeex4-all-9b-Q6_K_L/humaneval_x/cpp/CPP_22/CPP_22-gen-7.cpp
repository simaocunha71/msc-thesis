#include <iostream>
#include <vector>
#include <any>
#include <algorithm>
#include <set>
#include <stdexcept>

std::vector<int> filter_integers(std::vector<std::any> values) {
    std::vector<int> result;

    for (const auto& value : values) {
        if (value.type() == typeid(int)) {
            try {
                result.push_back(std::any_cast<int>(value));
            } catch (const std::bad_any_cast& e) {
                std::cerr << "Bad any cast: " << e.what() << std::endl;
            }
        }
    }

    return result;
}

int main() {
    std::vector<std::any> values = {1, 2, 3, 4, 5.5, "string", std::set<int>{1, 2, 3}};
    std::vector<int> filtered = filter_integers(values);

    for (const auto& value : filtered) {
        std::cout << value << " ";
    }

    return 0;
}
