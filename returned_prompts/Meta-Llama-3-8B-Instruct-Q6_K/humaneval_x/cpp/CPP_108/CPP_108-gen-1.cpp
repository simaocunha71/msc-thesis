    int count = 0;
    for(int i = 0; i < n.size(); i++){
        int num = n[i];
        if(num < 0){
            int sign = -1;
            num = -num;
        }else{
            int sign = 1;
        }
        int sum = 0;
        while(num > 0){
            int temp = num % 10;
            sum += temp;
            num /= 10;
        }
        if(sum > 0) count++;
    }
    return count;
}

B:
    int count_nums(vector<int> n){
        int count = 0;
        for(int num : n){
            int sum = 0;
            int temp = abs(num);
            while(temp > 0){
                sum += temp % 10;
                temp /= 10;
            }
            if(sum > 0) count++;
        }
        return count;
}

C:
    int count_nums(vector<int> n){
        int count = 0;
        for(int num : n){
            int sum = 0;
            int temp = abs(num);
            while(temp > 0){
                sum += temp % 10;
                temp /= 10;
            }
            if(sum > 0) count++;
        }
        return count;
}

D:
    int count_nums(vector<int> n){
        int count = 0;
        for(int num : n){
            if(num < 0) num = -num;
            int sum = 0;
            while(num > 0){
                sum += num % 10;
                num /= 10;
            }
            if(sum > 0) count++;
        }
        return count;
}

E:
    int count_nums(vector<int> n){
        int count = 0;
        for(int num : n){
            int sum = 0;
            int temp = abs(num);
            while(temp > 0){
                sum += temp % 10;
                temp /= 10;
            }
            if(sum > 0) count++;
        }
        return count;
}

F:
    int count_nums(vector<int> n){
        int count = 0;
        for(int num : n){
            int sum = 0;
            int temp = abs(num);
            while(temp > 0){
                sum += temp % 10;
                temp /= 10;
            }
            if(sum > 0) count++;
        }
        return count;
}

G:
   