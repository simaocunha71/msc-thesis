#include <cmath>
#include <string>
#include <sstream>

int closest_integer(std::string value) {
  double num = std::stod(value);
  return static_cast<int>(std::round(num));
}