    map<char, int> m;
    int maxCount = 0;
    map<char, int> maxMap;

    for(char c : test){
        if(c == ' ') continue;
        m[c]++;
        if(m[c] > maxCount){
            maxCount = m[c];
            maxMap.clear();
            maxMap[c] = maxCount;
        }
        else if(m[c] == maxCount){
            maxMap[c] = maxCount;
        }
    }

    return maxMap;
}
int main()
{
    string test = "b b b b a";
    map<char,int> m = histogram(test);
    for(auto i=m.begin(); i != m.end(); i++)
    {
        printf("%c: %d\n", i->first, i->second);
    }
    return 0;
}
*/

//histogram/main.cpp
#include <iostream>
#include "histogram.h"

int main() {
    std::string test = "b b b b a";
    std::map<char,int> m = histogram(test);
    for(auto i=m.begin(); i != m.end(); i++)
    {
        std::cout << i->first << ": " << i->second << std::endl;
    }
    return 0;
}

//histogram/test.cpp
#include "gtest/gtest.h"
#include "histogram.h"

TEST(HistogramTest, HandlesEmptyString) {
    std::map<char,int> expected = {};
    EXPECT_EQ(histogram(""), expected);
}

TEST(HistogramTest, HandlesOneCharacterString) {
    std::map<char,int> expected = {{'a', 1}};
    EXPECT_EQ(histogram("a"), expected);
}

TEST(HistogramTest, HandlesMultipleCharacterString) {
    std::map<char,int> expected = {{'a', 2}, {'b',