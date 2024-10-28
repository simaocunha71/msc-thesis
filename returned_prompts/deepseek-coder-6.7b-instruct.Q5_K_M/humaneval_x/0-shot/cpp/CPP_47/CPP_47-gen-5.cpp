    sort(l.begin(), l.end());
    float median;
    int size = l.size();
    if (size % 2 == 0){
        median = (l[size / 2 - 1] + l[size / 2]) / 2;
    }
    else{
        median = l[size / 2];
    }
    return median;
}

int main(){
    vector<float> v1 = {3, 1, 2, 4, 5};
    vector<float> v2 = {-10, 4, 6, 1000, 10, 20};
    printf("%f\n", median(v1));
    printf("%f\n", median(v2));
    return 0;
}

*/

//Programming_C++/C++_Practice/CPP_Practice/CPP_Practice/CPP_Practice/Exam_Practice/2022_04_29/main.cpp
﻿/*

