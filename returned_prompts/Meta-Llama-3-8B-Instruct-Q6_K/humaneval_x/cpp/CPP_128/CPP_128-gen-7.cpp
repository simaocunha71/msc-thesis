    if(arr.empty()){
        return -32768;
    }
    int sign = 1;
    int sum = 0;
    for(int i=0; i<arr.size(); i++){
        if(arr[i] == 0){
            return 0;
        }
        sign *= (arr[i] > 0) ? 1 : ((arr[i] < 0) ? -1 : 0);
        sum += abs(arr[i]);
    }
    return sign * sum;
}

B:
    int prod_signs(vector<int> arr){
        if(arr.empty()){
            return -32768;
        }
        int sign = 1;
        int sum = 0;
        for(int i=0; i<arr.size(); i++){
            if(arr[i] == 0){
                return 0;
            }
            sign *= (arr[i] > 0) ? 1 : ((arr[i] < 0) ? -1 : 0);
            sum += abs(arr[i]);
        }
        return sign * sum;
    }
}

C:
    int prod_signs(vector<int> arr){
        if(arr.empty()){
            return -32768;
        }
        int sign = 1;
        int sum = 0;
        for(int i=0; i<arr.size(); i++){
            if(arr[i] == 0){
                return 0;
            }
            sign *= (arr[i] > 0) ? 1 : ((arr[i] < 0) ? -1 : 0);
            sum += abs(arr[i]);
        }
        return sign * sum;
    }
}

D:
    int prod_signs(vector<int> arr){
        if(arr.empty()){
            return -32768;
        }
        int sign = 1;
        int sum = 0;
        for(int i=0; i<arr.size(); i++){
            if(arr[i] == 0){
                return 0;
            }
            sign *= (arr[i] > 0) ? 1 : ((arr[i] < 0) ? -1 : 0);
            sum += abs(arr[i]);
        }
        return sign * sum;
    }
}

E:
    int prod_signs(vector<int> arr){
        if(arr.empty()){
            return -32768;
        }
        int sign = 1;
        int sum = 0;
        for(int i=0; i<arr.size(); i++){
            if(arr[i]