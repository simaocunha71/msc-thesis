    int sum = 0;
    int sign = 1;
    for(int i = 0; i < arr.size(); i++) {
        if(arr[i] == 0) {
            sign *= 0;
        }
        else if(arr[i] < 0) {
            sign *= -1;
        }
        else {
            sign *= 1;
        }
    }
    if(sign == 0) {
        sum = -32768;
    }
    else {
        for(int i = 0; i < arr.size(); i++) {
            if(arr[i] < 0) {
                arr[i] = -arr[i];
            }
            sum += arr[i];
        }
    }
    return sum;
}


B:
int prod_signs(vector<int> arr) {
    int sign = 1, sum = 0;
    for(int i = 0; i < arr.size(); i++) {
        if(arr[i] == 0) {
            sign *= 0;
        }
        else if(arr[i] < 0) {
            sign *= -1;
        }
        else {
            sign *= 1;
        }
    }
    if(sign == 0) {
        sum = -32768;
    }
    else {
        for(int i = 0; i < arr.size(); i++) {
            if(arr[i] < 0) {
                arr[i] = -arr[i];
            }
            sum += arr[i];
        }
    }
    return sum;
}


C:
int prod_signs(vector<int> arr) {
    int sign = 1, sum = 0;
    for(int i = 0; i < arr.size(); i++) {
        if(arr[i] == 0) {
            sign = 0;
        }
        else if(arr[i] < 0) {
            sign *= -1;
        }
        else {
            sign