    return lst;
}

// TESTS

#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <cstdlib>
#include <cassert>
using namespace std;

void _assert(bool b) {
    if (!b)
        throw runtime_error("test failed");
}

int _test_strange_sort_list(vector<int> lst, vector<int> expected){
    try{
        vector<int> res = strange_sort_list(lst);
        _assert(res == expected);
    }catch(exception& e){
        cerr << e.what() << endl;
        return 1;
    }
    return 0;
}

int _test_strange_sort_list_empty(vector<int> lst, vector<int> expected){
    try{
        vector<int> res = strange_sort_list(lst);
        _assert(res == expected);
    }catch(exception& e){
        cerr << e.what() << endl;
        return 1;
    }
    return 0;
}

int _test_strange_sort_list_unsorted(vector<int> lst, vector<int> expected){
    try{
        vector<int> res = strange_sort_list(lst);
        _assert(res == expected);
    }catch(exception& e){
        cerr << e.what() << endl;
        return 1;
    }
    return 0;
}

int test_strange_sort_list(){
    vector<int> lst = {1, 2, 3, 4};
    vector<int> expected = {1, 4, 2, 3};
    _test_strange_sort_list(lst, expected);
    lst = {5, 5, 5, 5};
    expected = {5, 5, 5, 5};
    _test_strange_sort_list(lst, expected);
    lst = {};
    expected = {};
    _test_strange_sort_list