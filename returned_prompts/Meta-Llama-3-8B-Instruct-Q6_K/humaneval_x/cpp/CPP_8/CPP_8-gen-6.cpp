    int sum = 0;
    long long product = 1;
    for(int i = 0; i < numbers.size(); i++){
        sum += numbers[i];
        product *= numbers[i];
    }
    vector<int> result;
    result.push_back(sum);
    result.push_back(product);
    return result;
}
B:
    vector<int> sum_product(vector<int> numbers){
        int sum = 0;
        long long product = 1;
        for(int i = 0; i < numbers.size(); i++){
            sum += numbers[i];
            product *= numbers[i];
        }
        if(numbers.empty()){
            sum = 0;
            product = 1;
        }
        vector<int> result;
        result.push_back(sum);
        result.push_back(product);
        return result;
    }
C:
    vector<int> sum_product(vector<int> numbers){
        int sum = 0;
        long long product = 1;
        for(int i = 0; i < numbers.size(); i++){
            sum += numbers[i];
            product *= numbers[i];
        }
        vector<int> result;
        if(numbers.empty()){
            sum = 0;
            product = 1;
        }
        result.push_back(sum);
        result.push_back(product);
        return result;
    }
D:
    vector<int> sum_product(vector<int> numbers){
        vector<int> result;
        if(numbers.empty()){
            result.push_back(0);
            result.push_back(1);
        }else{
            int sum = 0;
            long long product = 1;
            for(int i = 0; i < numbers.size(); i++){
                sum += numbers[i];
                product *= numbers[i];
            }
            result.push_back(sum);
            result.push_back(product);
        }
        return result;
}
E:
    vector<int> sum_product(vector<int> numbers){
        vector<int> result;
        if(numbers.empty()){
            result.push_back(0);
            result.push_back(1);
        }else{
            int sum = 0;
            long long product = 1;
            for(int i = 0; i < numbers.size(); i++){
                sum += numbers[i];
                product *= numbers[i];
            }
            result.push_back(sum);
            result.push_back(product);
        }
        return result;
    }
F:
    vector<int> sum_product(vector<int> numbers){
        vector<int> result;
        if(numbers.empty()){
            return {0, 1};
        }