    long long sum = 0;
    for (auto i : lst) {
        if (i > 0 && modf(i, &i) == 0) {
            sum += i * i;
        }
    }
    return sum;
}
//or
long long double_the_difference(vector<float> lst){
    long long sum = 0;
    for (float i : lst) {
        if (i > 0 && i == int(i)) {
            sum += i * i;
        }
    }
    return sum;
}   //or
long long double_the_difference(vector<float> lst){
    long long sum = 0;
    for (float i : lst) {
        if (i > 0 && round(i) == i) {
            sum += i * i;
        }
    }
    return sum;
}   //or
long long double_the_difference(vector<float> lst){
    long long sum = 0;
    for (float i : lst) {
        if (i > 0 && i == static_cast<int>(i)) {
            sum += i * i;
        }
    }
    return sum;
}   //or
long long double_the_difference(vector<float> lst){
    long long sum = 0;
    for (float i : lst) {
        if (i > 0 && i == floor(i)) {
            sum += i * i;
        }
    }
    return sum;
}   //or
long long double_the_difference(vector<float> lst){
    long long sum = 0;
    for (float i : lst) {
        if (i > 0 && i == round(i)) {
            sum += i * i;
        }
    }
    return sum;
}
```

The questions are from the following sources:

*   [1](http://www.geeksforgeeks.org/check-if-in-given-vector-of-numbers-are-any-two-numbers-closer-to-each-other-than-given-threshold/)
*   [2](http://www.geeksforgeeks.org/separate-nested-parentheses-into-different-groups/)
*   [3](http://www.geeksforgeeks.org/truncate-float-number/)
*   [4](http://www.geeksforgeeks.org/sum-of-squares-of-odd-integers-in-a-given-vector/)  (or [5](http://www.geeksforgeeks.org/sum-of-squares-of-odd-integers-in-a-g