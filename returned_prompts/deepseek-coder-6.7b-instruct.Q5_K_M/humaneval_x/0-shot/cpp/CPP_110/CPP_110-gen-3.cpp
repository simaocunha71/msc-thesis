
}

int main() {
  vector<int> lst1 = {1, 2, 3, 4};
  vector<int> lst2 = {1, 2, 3, 4};
  printf("%s\n", exchange(lst1, lst2).c_str());
  return 0;
}
*/

#include<vector>
#include<string>
using namespace std;

string exchange(vector<int> lst1,vector<int> lst2){
    int odd_lst1=0, even_lst2=0;
    for(int i=0; i<lst1.size(); i++){
        if(lst1[i]%2 != 0)
            odd_lst1++;
    }
    for(int i=0; i<lst2.size(); i++){
        if(lst2[i]%2 == 0)
            even_lst2++;
    }
    if(odd_lst1 > even_lst2)
        return "NO";
    else
        return "YES";
}

//test/test_exchange.cpp
#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "doctest.h"
#include "../src/exchange.cpp"

TEST_CASE("Testing exchange function") {
    //test case 1
    vector<int> lst1 = {1, 2, 3, 4};
    vector<int> lst2 = {1, 2, 3, 4};
    string res = "YES";
    CHECK(exchange(lst1, lst2) == res);

    //test case 2
    lst1 = {1, 2, 3, 4};
    lst2 = {1, 5, 3, 4};
    res = "NO";
    CHECK(exchange(lst1, lst2) == res);

    //test case 3
    lst1 = {2, 2, 2, 2};
    lst2 =