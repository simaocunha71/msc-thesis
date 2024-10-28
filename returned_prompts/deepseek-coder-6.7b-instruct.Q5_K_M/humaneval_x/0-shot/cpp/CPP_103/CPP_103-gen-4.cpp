    if(n > m){
        return "-1";
    }
B:
    int sum = 0;
    for(int i = n; i <= m; i++){
        sum += i;
    }
C:
    int avg = (int)round((double)sum / (m - n + 1));
D:
    return bitset<32>(avg).to_string();
}
int main() {
    int n = 1, m = 5;
    printf("%s", rounded_avg(n, m).c_str());
    return 0;
}

*/

#include <stdio.h>
#include <math.h>

int main() {
    int n = 1, m = 5;
    if(n > m){
        printf("-1");
        return 0;
    }
    int sum = 0;
    for(int i = n; i <= m; i++){
        sum += i;
    }
    int avg = (int)round((double)sum / (m - n + 1));
    printf("%d", avg);
    return 0;
}

//src/main.cpp
#include <stdio.h>
#include <math.h>
#include <string>
#include <bitset>
using namespace std;

string rounded_avg(int n,int m){
    if(n > m){
        return "-1";
    }
    int sum = 0;
    for(int i = n; i <= m; i++){
        sum += i;
    }
    int avg = (int)round((double)sum / (m - n + 1));
    return bitset<32>(avg).to_string();
}

int main() {
    int n = 1, m = 5;
    printf("%s", rounded_avg(n, m).c_str());
    return 0;
}

//test/test.cpp
#include "../src/main.cpp"
#include <gtest/gtest.h>

TEST(rounded_avgTest, ReturnsExpectedValue) {