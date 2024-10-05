    vector<int> integers;
    list_any::iterator it;
    for(it = values.begin(); it != values.end(); ++it){
        if(boost::any_cast<int>(&(*it))){
            integers.push_back(boost::any_cast<int>((*it)));
        }
    }
    return integers;
}
int main(){
    list_any values = {1, 2, 3, "abc", std::string("test"), 5.5, 0};
    vector<int> integers = filter_integers(values);
    for(vector<int>::iterator it = integers.begin(); it != integers.end(); ++it){
        printf("%d ", *it);
    }
    return 0;
}


A: The problem is that in Python you can filter list by type using built-in isinstance function. But in C++ we have to use dynamic_cast or typeid, and Boost.Any isn't suitable for this. We can use std::variant or boost::variant, but it's more complex than necessary. So we have to use a std::list of Boost.Any.
Here is the correct version of your code:
#include<iostream>
#include<vector>
#include<list>
#include<boost/any.hpp>

typedef std::list<boost::any> list_any;

std::vector<int> filter_integers(list_any values){
    std::vector<int> integers;
    for(auto& value: values){
        if(boost::any_cast<int>(&value)){
            integers.push_back(boost::any_cast<int>(value));
        }
    }
    return integers;
}

int main(){
    list_any values = {1, 2, 3, "abc", std::string("test"), 5.5, 0};
    std::vector<int> integers = filter_integers(values);
    for(int i : integers){
        std::cout << i << " ";
    }
    return 0;
}

In this code, we use range-based for loop to iter