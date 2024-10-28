    vector<int> result;
    for (list_any::iterator it = values.begin(); it != values.end(); ++it) {
        if (boost::any_cast<int>(*it) != 0) {
            result.push_back(boost::any_cast<int>(*it));
        }
    }
    return result;
}
// You can also use a lambda function:
// return filter(values.begin(), values.end(), [](boost::any a)->bool{return boost::any_cast<int>(a)!=0;});
// return vector<int>(values.begin(), values.end(), [](boost::any a)->bool{return boost::any_cast<int>(a)!=0;});
// You can also use a for loop:
// vector<int> result;
// for (auto& v : values) {
//     if (boost::any_cast<int>(v) != 0) {
//         result.push_back(boost::any_cast<int>(v));
//     }
// }
// return result;  // return by value is allowed in C++11
// return std::move(result);  // return by rvalue reference in C++11
// return vector<int>(std::make_move_iterator(result.begin()), std::make_move_iterator(result.end()));  // return by rvalue reference in C++11
// return std::vector<int>(std::make_move_iterator(result.begin()), std::make_move_iterator(result.end()));  // return by rvalue reference in C++11
// return vector<int>(result.begin(), result.end());  // return by value is allowed in C++11
// return std::vector<int>(result.begin(), result.end());  // return by value is allowed in C++11
// return vector<int>(std::move(result.begin()), std::move(result.end()));  // return by rvalue reference in C++11
// return std::vector<int>(std::move(result.begin()), std::move(result.end()));  // return by rvalue reference in C++11
// You can also use a for loop with range-based for loop:
// vector<int> result;
// for (auto& v : values) {
//     if (boost::any_cast<int>(v) != 0) {
//         result.push_back(boost::any_cast<int>(v));
//     }
// }
// return result;  // return by value is allowed in C++11
// return std::move(result);  // return by rvalue reference in C++11
// return std::vector<int>(std::make