    string binary = "";
    while(N > 0){
        binary = to_string(N%2) + binary;
        N /= 2;
    }
    return binary;
}

int main(){
    int N;
    scanf("%d",&N);
    string out_ = solve(N);
    cout << out_ << endl;
    return 0;
}

*/

#include <stdio.h>
#include <string>

using namespace std;

string solve(int N) {

    string binary = "";
    while (N > 0) {
        binary = to_string(N % 2) + binary;
        N /= 2;
    }
    return binary;
}

int main() {
    int N;
    scanf("%d", &N);
    string out_ = solve(N);
    printf("%s\n", out_.c_str());
    return 0;
}

//src/test_c_code.cpp
#include "gtest/gtest.h"
#include <stdio.h>
#include <string>

using namespace std;

extern string solve(int N);

TEST(solveTest, ReturnsCorrectBinary){
    EXPECT_EQ(solve(1000), "1111101000");
    EXPECT_EQ(solve(150), "10010110");
    EXPECT_EQ(solve(147), "10010011");
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}

//src/test_cpp_code.cpp
#include "gtest/gtest.h"
#include <string>

using namespace std;

extern string solve(int N);

TEST(solveTest, ReturnsCorrectBinary){
    EXPECT_EQ(solve(1000), "1111101000");
    EXPECT_EQ(solve(150), "1