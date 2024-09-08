```cpp
#include <boost/any.hpp>
#include <list>
#include <vector>
#include <iostream>
typedef std::list<boost::any> list_any;
using namespace std;

vector<int> filter_integers(list_any values){
    vector<int> out;
    for (auto& v : values) {
        if (boost::any_cast<int>(v)) {
            out.push_back(boost::any_cast<int>(v));
        }
    }
    return out;
}
```