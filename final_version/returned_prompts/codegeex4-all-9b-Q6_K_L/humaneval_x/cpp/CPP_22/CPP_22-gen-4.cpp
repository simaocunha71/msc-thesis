#include <vector>
#include <algorithm>
#include <boost/any.hpp>
#include <boost/algorithm/string.hpp>

std::vector<int> filter_integers(std::list<boost::any> values)
{
    std::vector<int> result;
    for(const auto& value : values)
    {
        boost::any_cast<int>(value);
    }
    return result;
}