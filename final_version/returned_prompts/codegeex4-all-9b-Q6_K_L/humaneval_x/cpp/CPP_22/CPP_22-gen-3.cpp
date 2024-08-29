#include <iostream>
#include <vector>
#include <list>
#include <boost/any.hpp>
using namespace std;

vector<int> filter_integers(list<boost::any> values) {
    vector<int> res;
    for (auto& v : values) {
        if (boost::any_cast<int>(v)) {
            res.push_back(boost::any_cast<int>(v));
        }
    }
    return res;
}

int main() {
    list<boost::any> values = {3.14, 5};
    vector<int> res = filter_integers(values);
    for (auto& i : res) {
        cout << i << endl;
    }
    return 0;
}