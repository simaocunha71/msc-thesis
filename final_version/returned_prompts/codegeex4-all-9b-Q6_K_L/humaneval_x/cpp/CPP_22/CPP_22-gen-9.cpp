#include <iostream>
#include <vector>
#include <list>
#include <boost/any.hpp>
#include <boost/algorithm/string.hpp>
#include <boost/algorithm/string/classification.hpp>

typedef std::list<boost::any> list_any;

std::vector<int> filter_integers(list_any values) {
    std::vector<int> out;
    for (auto &value : values) {
        if (value.type() == typeid(int)) {
            out.push_back(boost::any_cast<int>(value));
        }
    }
    return out;
}

int main() {
    std::list<boost::any> values1 = {boost::any(5), boost::any(3.14)};
    std::cout << "filtered: ";
    for (auto &value : filter_integers(values1)) {
        std::cout << value << " ";
    }
    std::cout << std::endl;

    std::list<boost::any> values2 = {boost::any(1), boost::any(2), boost::any(3), boost::any("abc"), boost::any({}), boost::any({})};
    std::cout << "filtered: ";
    for (auto &value : filter_integers(values2)) {
        std::cout << value << " ";
    }
    std::cout << std::endl;

    return 0;
}

输出：
filtered: 5
filtered: 1 2 3