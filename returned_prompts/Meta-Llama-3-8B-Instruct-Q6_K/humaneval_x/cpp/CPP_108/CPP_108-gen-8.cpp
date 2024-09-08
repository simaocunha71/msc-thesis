    int count = 0;
    for(int i = 0; i < n.size(); i++){
        if(n[i] < 0){
            int temp = n[i];
            int sign = 1;
            if(temp < 0){
                sign = -1;
                temp *= -1;
            }
            int sum = 0;
            while(temp > 0){
                sum += temp % 10;
                temp /= 10;
            }
            if(sum * sign > 0){
                count++;
            }
        }
        else if(n[i] > 0){
            int sum = 0;
            int temp = n[i];
            while(temp > 0){
                sum += temp % 10;
                temp /= 10;
            }
            if(sum > 0){
                count++;
            }
        }
    }
    return count;
}