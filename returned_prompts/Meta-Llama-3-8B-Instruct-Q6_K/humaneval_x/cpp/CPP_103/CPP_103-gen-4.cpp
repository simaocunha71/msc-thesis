    if(n > m){
        return "-1";
    }
    int sum = 0;
    int count = 0;
    for(int i = n; i <= m; i++){
        sum += i;
        count++;
    }
    double avg = (double)sum / count;
    avg = floor(avg + 0.5);
    string str = to_string(avg);
    return str;
}B:
    if(n > m){
        return "-1";
    }
    int sum = 0;
    int count = 0;
    for(int i = n; i <= m; i++){
        sum += i;
        count++;
    }
    double avg = (double)sum / count;
    avg = round(avg);
    string str = "";
    while(avg > 0){
        if(avg % 2 == 0){
            str = "0" + str;
        }else{
            str = "1" + str;
        }
        avg /= 2;
    }
    return str;
}

C:
    if(n > m){
        return "-1";
    }
    int sum = 0;
    int count = 0;
    for(int i = n; i <= m; i++){
        sum += i;
        count++;
    }
    double avg = (double)sum / count;
    avg = round(avg);
    string str = "";
    int temp = avg;
    while(temp > 0){
        if(temp % 2 == 0){
            str = "0" + str;
        }else{
            str = "1" + str;
        }
        temp /= 2;
    }
    return str;
}D:
    if(n > m){
        return "-1";
    }
    int sum = 0;
    int count = 0;
    for(int i = n; i <= m; i++){
        sum += i;
        count++;
    }
    double avg = (double)sum / count;
    avg = round(avg);
    string str = "";
    int temp = avg;
    while(temp > 0){
        if(temp % 2 == 0){
            str = "0" + str;
        }else{
            str = "1" + str;
        }
        temp /= 2;
    }
    return str;
}

E:
    if(n > m){
        return "-1";
    }
    int sum = 0;
    int count = 0;
    for