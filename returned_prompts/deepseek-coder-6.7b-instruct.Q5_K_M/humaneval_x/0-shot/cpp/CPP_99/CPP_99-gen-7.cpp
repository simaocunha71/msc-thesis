    double num = stod(value);
    return (int)round(num);
}
*/

#include <iostream>
#include <string>
#include <cmath>

int closest_integer(std::string value) {
    double num = std::stod(value);
    return (int)round(num);
}

int main() {
    std::cout << closest_integer("10") << std::endl;
    std::cout << closest_integer("15.3") << std::endl;
    std::cout << closest_integer("14.5") << std::endl;
    std::cout << closest_integer("-14.5") << std::endl;
    return 0;
}