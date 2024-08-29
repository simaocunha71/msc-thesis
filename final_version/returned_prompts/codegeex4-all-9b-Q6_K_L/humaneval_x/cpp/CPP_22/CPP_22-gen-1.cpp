```cpp
#include <vector>
#include <boost/any.hpp>
#include <list>
#include <type_traits>
#include <limits>

std::vector<int> filter_integers(std::list<boost::any> values) {
    std::vector<int> filtered_values;
    for (const auto &value : values) {
        if (std::is_same<std::remove_cv_t<std::remove_reference_t<decltype(value)>>, int>::value) {
            filtered_values.push_back(boost::any_cast<int>(value));
        }
    }
    return filtered_values;
}
```