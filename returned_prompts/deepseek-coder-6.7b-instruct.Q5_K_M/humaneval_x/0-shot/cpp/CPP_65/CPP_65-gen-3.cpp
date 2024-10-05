    string s = to_string(x);
    int n = s.size();
    if (shift >= n) {
        reverse(s.begin(), s.end());
        return s;
    }
    rotate(s.begin(),s.begin()+n-shift,s.end());
    return s;
}
int main(){
    printf("%s\n",circular_shift(12,1).c_str());
    printf("%s\n",circular_shift(12,2).c_str());
    return 0;
}

*/

#endif // CIRCULAR_SHIFT_H

//HW5/HW5/main.cpp
#include <stdio.h>
#include "circular_shift.h"

int main(){
    printf("%s\n",circular_shift(12,1).c_str());
    printf("%s\n",circular_shift(12,2).c_str());
    return 0;
}

//HW5/tests/test_circular_shift.cpp
#include "../HW5/circular_shift.h"
#include <gtest/gtest.h>

TEST(CircularShiftTest, PositiveNos) { 
    EXPECT_EQ("21", circular_shift(12, 1));
    EXPECT_EQ("12", circular_shift(12, 2));
}

int main(int argc, char **argv) {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}

//HW5/tests/test_circular_shift_main.cpp
#include "../HW5/circular_shift.h"
#include <iostream>

int main(){
    std::cout << circular_shift(12,1) << std::endl;
    std::cout << circular_shift(12,2) << std::endl;
    return 0;
}//HW5/HW5/rotate_left.h
#ifndef ROTATE_LEFT_H
#define ROT