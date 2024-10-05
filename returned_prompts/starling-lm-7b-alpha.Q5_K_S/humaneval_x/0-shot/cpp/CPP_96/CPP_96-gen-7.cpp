    vector<int>prime;
    if(n==0){
        return prime;
    }
    else if(n==1){
        return prime;
    }
    else if(n==2){
        prime.push_back(2);
        return prime;
    }
    else if(n==3){
        prime.push_back(2);
        prime.push_back(3);
        return prime;
    }
    else if(n==4){
        prime.push_back(2);
        return prime;
    }
    else if(n==5){
        prime.push_back(2);
        prime.push_back(3);
        prime.push_back(5);
        return prime;
    }
    else{
        prime.push_back(2);
        prime.push_back(3);
        prime.push_back(5);
        prime.push_back(7);
        for(int i=9;i<n;i+=2){
            int j;
            for(j=3;j*j<=i;j+=2){
                if(i%j==0){
                    break;
                }
            }
            if(i*i>n){
                break;
            }
            if(j*j>i){
                prime.push_back(i);
            }
        }
        return prime;
    }
}











































































































































































