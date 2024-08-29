#include <algorithm>
#include <vector>

std::vector<float> find_closest_elements(std::vector<float> numbers) {
  if (numbers.size() < 2) {
    throw std::invalid_argument("Vector must contain at least two elements.");
  }

  std::sort(numbers.begin(), numbers.end());

  float min_diff = std::numeric_limits<float>::max();
  std::pair<float, float> min_pair;

  for (size_t i = 0; i < numbers.size() - 1; ++i) {
    float diff = numbers[i + 1] - numbers[i];
    if (diff < min_diff) {
      min_diff = diff;
      min_pair = std::make_pair(numbers[i], numbers[i + 1]);
    }
  }

  return std::vector<float>{min_pair.first, min_pair.second};
}

int main() {
  auto closest_elements = find_closest_elements({1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 2.2f});
  printf("(%f, %f)\n", closest_elements[0], closest_elements[1]);

  closest_elements = find_closest_elements({1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 2.0f});
  printf("(%f, %f)\n", closest_elements[0], closest_elements[1]);

  return 0;
}

