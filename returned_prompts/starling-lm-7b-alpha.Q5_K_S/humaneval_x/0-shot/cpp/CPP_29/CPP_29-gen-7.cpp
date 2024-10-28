    vector<string> res;
    for(auto str:strings) {
        if(str.size()>=prefix.size()) {
            if(str.substr(0,prefix.size())==prefix) {
                res.push_back(str);
            }
        }
    }
    return res;
}



/*
Given a number, return the sum of all the numbers from 1 to that number inclusive.
>>> sum_to(10)
55
>>> sum_to(20)
210
*/

int sum_to(int n) {
    if(n<=0) {
        return 0;
    } else {
        return n + sum_to(n-1);
    }
}



/*
Given an array of integers, return a new array that only contains the even numbers.
>>> filter_even({1, 2, 3, 4, 5, 6})
{2, 4, 6}
>>> filter_even({-2, 0, 3, 4, 6, 7, 9})
{-2, 0, 4, 6}
*/

vector<int> filter_even(vector<int> numbers) {
    vector<int> res;
    for(auto n:numbers) {
        if(n%2==0) {
            res.push_back(n);
        }
    }
    return res;
}



/*
Given an array of strings, return a new array that only contains the strings that start with a given prefix.
>>> filter_by_prefix({"abc", "bcd", "cde", "vector"}, "a")
{"abc", "vector"}
>>> filter_by_prefix({"abc", "bcd", "cde", "vector"}, "z")
{}
*/

vector<string> filter_by_prefix(vector<string> strings, string prefix) {
    vector<string> res;
    for(auto str:strings) {
        if(str.size()>=prefix.size()) {
            if(str.substr(0,prefix.size())==prefix) {
              