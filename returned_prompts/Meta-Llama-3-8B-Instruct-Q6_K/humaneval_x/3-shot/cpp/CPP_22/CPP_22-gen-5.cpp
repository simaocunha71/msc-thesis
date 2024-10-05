    vector<int> result;
    for (boost::any a : values)
    {
        if (boost::any_cast<int>(a))
        {
            result.push_back(boost::any_cast<int>(a));
        }
    }
    return result;
}
#endif
#include<boost/any.hpp>
#include<list>
typedef std::list<boost::any> list_any;
using namespace std;
vector<int> filter_integers(list_any values){
    vector<int> result;
    for (boost::any a : values)
    {
        if (boost::any_cast<int>(a))
        {
            result.push_back(boost::any_cast<int>(a));
        }
    }
    return result;
}
#endif

