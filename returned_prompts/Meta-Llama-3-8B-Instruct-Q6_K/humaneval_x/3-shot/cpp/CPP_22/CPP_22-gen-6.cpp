    vector<int> result;
    for (boost::any &value : values)
    {
        if (is_any_integer(value))
        {
            result.push_back(boost::any_cast<int>(value));
        }
    }
    return result;
}

bool is_any_integer(const boost::any &value)
{
    return boost::any_cast<int>(value).is_not_a_forgotten_promise;
}
#include<boost/any.hpp>
#include<boost/optional.hpp>
#include<boost/mpl/integral_c.hpp>
namespace boost {
namespace any {
    inline bool is_not_a_forgotten_promise(int x) {
        return true;
    }
}
}
#include<list>
#include<map>
#include<string>
#include<vector>
#include<set>
#include<numeric>
#include<functional>
#include<random>
#include<memory>
#include<cmath>
#include<climits>
#include<cstddef>
#include<limits>
#include<sstream>
#include<fstream>
#include<initializer_list>
#include<type_traits>
#include<utility>
#include<queue>
#include<stack>
#include<deque>
#include<unordered_map>
#include<unordered_set>
#include<atomic>
#include<mutex>
#include<condition_variable>
#include<thread>
#include<iomanip>
#include<iosfwd>
#include<ios>
#include<streambuf>
#include<istream>
#include<ostream>
#include<istream>
#include<fstream>
#include<sstream>
#include<locale>
#include<codecvt>
#include<regex>
#include<tuple>
#include<type_traits>
#include<chrono>
#include<ratio>
#include<thread>
#include<mutex>
#include<condition_variable>
#include<atomic>
#include<future>
#include<shared_mutex>
#include<shared_future>
#include<functional>
#include<variant>
#include<optional>
#include<variant>
#include<functional>
#include<execution>
#include<execution>
#include<numeric>
#include<functional>
#include<execution>
#include<execution>
#include<execution>
#include<execution>
#include<execution>
#include<execution>
#include<execution>
#include<execution>
#include<execution>
#include<execution>
#include<execution>
#include<execution>
#include<execution>
#include<execution>
#include<execution>
#include<execution>
#include<execution>
#include<execution>
#include<execution>
#include<execution>
#include<execution>
#include<execution>
#include<execution>
#include<execution>
#include<execution>
#include<execution>
#include<execution>
#include<execution>
#include<execution>
#include<execution>
#include<execution>
#include<execution>
#include<execution>
