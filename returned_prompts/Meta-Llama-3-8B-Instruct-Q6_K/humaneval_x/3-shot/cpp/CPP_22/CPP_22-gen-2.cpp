    vector<int> result;
    for (auto value : values)
    {
        if (boost::any_cast<int>(value)!=0)
        {
            result.push_back(boost::any_cast<int>(value));
        }
    }
    return result;
}  // using boost::any and boost::any_cast
// or
#include<type_traits>
#include<stdexcept>
vector<int> filter_integers(list_any values){
    vector<int> result;
    for (auto value : values)
    {
        if (is_same_v<decltype(value), int>)
        {
            result.push_back(std::get<int>(value));
        }
    }
    return result;
}  // using c++17 and std::get
// or
#include<type_traits>
#include<stdexcept>
vector<int> filter_integers(list_any values){
    vector<int> result;
    for (auto value : values)
    {
        if (is_integer_v<decltype(value)>)
        {
            result.push_back(std::get<decltype(value)>(value));
        }
    }
    return result;
}  // using c++17 and std::get

