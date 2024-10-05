    vector<int> result;
    for (list_any::iterator it = values.begin(); it != values.end(); ++it) {
        if (boost::any_cast<int>(*it)) {
            result.push_back(boost::any_cast<int>(*it));
        }
    }
    return result;
}


#include <iostream>
#include <vector>
#include <string>
#include <boost/any.hpp>
#include <list>
#include <boost/foreach.hpp>
using namespace std;

typedef std::list<boost::any> list_any;

vector<int> filter_integers(list_any values)
{
    vector<int> result;
    BOOST_FOREACH(const boost::any& val, values)
        if (boost::any_cast<int>(val))
            result.push_back(boost::any_cast<int>(val));
    return result;
}

int main()
{
    list_any values;
    values.push_back("a");
    values.push_back(3.14);
    values.push_back(5);

    vector<int> result = filter_integers(values);

    cout << "{";
    BOOST_FOREACH(const int& val, result)
        cout << val << ",";
    cout << "}\n";

    values.clear();

    values.push_back(1);
    values.push_back(2);
    values.push_back(3);
    values.push_back("abc");
    values.push_back({});
    values.push_back({});

    result = filter_integers(values);

    cout << "{";
    BOOST_FOREACH(const int& val, result)
        cout << val << ",";
    cout << "}\n";

    return 0;
}






















































