    vector<float> l2;
    for(int i = 0; i < l.size(); i++){
        if (l[i] > 0){
            l2.push_back(l[i]);
        }
    }
    return l2;
}


/*
Return the maximum number from the vector.
>>> max_num({-1, 2, -4, 5, 6})
6
>>> max_num({5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10})
123
*/
int max_num(vector<float> l){
B:
    int max = 0;
    for(int i = 0; i < l.size(); i++){
        if (l[i] > max){
            max = l[i];
        }
    }
    return max;
}


/*
Return the minimum number from the vector.
>>> min_num({-1, 2, -4, 5, 6})
-1
>>> min_num({5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10})
-10
*/
int min_num(vector<float> l){
C:
    int min = 1000;
    for(int i = 0; i < l.size(); i++){
        if (l[i] < min){
            min = l[i];
        }
    }
    return min;
}


/*
Return the sum of all numbers in the vector.
>>> sum_nums({-1, 2, -4, 5, 6})
8
>>> sum_nums({5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10})
130
*/
int sum_nums(vector<float> l){
D:
    int sum = 0;
    for(int i = 0; i < l.size(); i++){
       