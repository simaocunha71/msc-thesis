```cpp
#include <string>
#include <cmath>
#include <iostream>

int closest_integer(const std::string& value) {
    size_t dot_pos = value.find('.');
    if (dot_pos == std::string::npos) {
        return std::stoi(value);
    }

    size_t integer_part = std::stoi(value.substr(0, dot_pos));
    size_t fractional_part = std::stoi(value.substr(dot_pos + 1));
    size_t decimal_places = value.size() - dot_pos - 1;

    double fraction = static_cast<double>(fractional_part) / std::pow(10, decimal_places);
    int rounded = std::round(integer_part + fraction);
    return rounded;
}
```

