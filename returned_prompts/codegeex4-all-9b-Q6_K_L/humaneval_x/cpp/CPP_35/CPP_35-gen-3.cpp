/*
Return maximum element in the vector.
>>> max_element({1, 2, 3})
3
>>> max_element({5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10})
123
*/
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
float max_element(vector<float> l){

    float max = l[0];
    for(int i = 0; i < l.size(); i++){
        if(l[i] > max){
            max = l[i];
        }
    }
    return max;
}

B:
/*
Return maximum element in the vector.
>>> max_element({1, 2, 3})
3
>>> max_element({5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10})
123
*/
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
float max_element(vector<float> l){

    float max = l[0];
    for(int i = 0; i < l.size(); i++){
        if(l[i] < max){
            max = l[i];
        }
    }
    return max;
}

C:
/*
Return maximum element in the vector.
>>> max_element({1, 2, 3})
3
>>> max_element({5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10})
123
*/
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
float max_element(vector<float> l){

    float max = l[0];
    for(int i = 0; i < l.size(); i++){
        if(l[i] == max){
            max = l[i];
        }
    }
    return max;
}

D:
/*
Return maximum element in the vector.
>>> max_element({1, 2, 3})
3
>>> max_element({5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10})
123
*/
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
float max_element(vector<float> l){

    float max = l[0];
    for(int i = 1; i < l.size(); i++){
        if(l[i]