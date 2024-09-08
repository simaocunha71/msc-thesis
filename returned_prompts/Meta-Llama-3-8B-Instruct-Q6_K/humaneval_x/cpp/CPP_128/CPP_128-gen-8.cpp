    int sign_product = 1;
    long long sum_of_magnitudes = 0;
    if(arr.empty()) return -32768;
    for(auto x: arr){
        sign_product *= (x > 0 ? 1 : x < 0 ? -1 : 0);
        sum_of_magnitudes += abs(x);
    }
    return sign_product * sum_of_magnitudes;

}

B:
    int prod_signs(vector<int> arr) {
        int sign_product = 1;
        long long sum_of_magnitudes = 0;
        if(arr.empty()) return -32768;
        for(auto x : arr){
            sign_product *= (x > 0 ? 1 : x < 0 ? -1 : 0);
            sum_of_magnitudes += labs(x);
        }
        return sign_product * sum_of_magnitudes;
    }
}
C:
    int prod_signs(vector<int> arr) {
        int sign_product = 1;
        long long sum_of_magnitudes = 0;
        if(arr.empty()) return -32768;
        for(auto x : arr){
            sign_product *= (x > 0 ? 1 : x < 0 ? -1 : 0);
            sum_of_magnitudes += labs(x);
        }
        return sign_product * sum_of_magnitudes;
    }
}
D:
    int prod_signs(vector<int> arr) {
        if(arr.empty()) return -32768;
        int sign_product = 1;
        long long sum_of_magnitudes = 0;
        for(auto x : arr){
            sign_product *= (x > 0 ? 1 : x < 0 ? -1 : 0);
            sum_of_magnitudes += labs(x);
        }
        return sign_product * sum_of_magnitudes;
    }
}

E:
    int prod_signs(vector<int> arr) {
        if(arr.empty()) return -32768;
        int sign_product = 1;
        long long sum_of_magnitudes = 0;
        for(auto x : arr){
            sign_product *= (x > 0 ? 1 : x < 0 ? -1 : 0);
            sum_of_magnitudes += labs(x);
        }
        return sign_product * sum_of_magnitudes;
    }
}

F:
    int prod_signs(vector<int> arr) {
        if(arr.empty()) return -32768;
        int sign_product