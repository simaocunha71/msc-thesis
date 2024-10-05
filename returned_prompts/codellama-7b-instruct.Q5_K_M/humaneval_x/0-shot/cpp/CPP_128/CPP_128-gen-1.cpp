
    if(arr.size() == 0) return -32768;
    int sum = 0;
    for(auto x: arr){
        sum += abs(x);
    }
    int prod = 1;
    for(auto x: arr){
        if(x > 0) prod *= 1;
        else if(x < 0) prod *= -1;
        else prod *= 0;
    }
    return sum * prod;
}

/*
int prod_signs(vector<int> arr){

B:

    if(arr.size() == 0) return -32768;
    int sum = 0;
    for(auto x: arr){
        sum += abs(x);
    }
    int prod = 1;
    for(auto x: arr){
        if(x > 0) prod *= 1;
        else if(x < 0) prod *= -1;
        else prod *= 0;
    }
    return sum * prod;
}

*/

/*
int prod_signs(vector<int> arr){

C:

    if(arr.size() == 0) return -32768;
    int sum = 0;
    for(auto x: arr){
        sum += abs(x);
    }
    int prod = 1;
    for(auto x: arr){
        if(x > 0) prod *= 1;
        else if(x < 0) prod *= -1;
        else prod *= 0;
    }
    return sum * prod;
}
*/
