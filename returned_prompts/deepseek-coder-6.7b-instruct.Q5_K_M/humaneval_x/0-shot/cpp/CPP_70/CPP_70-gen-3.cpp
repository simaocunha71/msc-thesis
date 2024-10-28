    sort(lst.begin(), lst.end());
    vector<int> result;
    while(!lst.empty()){
        result.push_back(lst.front());
        lst.erase(lst.begin());
        if(!lst.empty()){
            result.push_back(lst.back());
            lst.pop_back();
        }
    }
    return result;
}

int main(){
    vector<int> lst = {1, 2, 3, 4};
    vector<int> res = strange_sort_list(lst);
    for(int i = 0; i < res.size(); i++){
        printf("%d ", res[i]);
    }
    return 0;
}

*/

//Test/test_strange_sort.cpp
#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include "catch.hpp"
#include "strange_sort.cpp"

TEST_CASE("Test Strange Sorting", "[strange_sort_vector]") {
    REQUIRE(strange_sort_vector({1, 2, 3, 4}) == vector<int>({1, 4, 2, 3}));
    REQUIRE(strange_sort_vector({5, 5, 5, 5}) == vector<int>({5, 5, 5, 5}));
    REQUIRE(strange_sort_vector({}) == vector<int>({}));
}#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>

void error_handling(char *message);

int main(int argc, char *argv[])
{
    int sock;
    struct sockaddr_in serv_addr;
    char message[30];
    int str_len=0;

    if(argc != 3