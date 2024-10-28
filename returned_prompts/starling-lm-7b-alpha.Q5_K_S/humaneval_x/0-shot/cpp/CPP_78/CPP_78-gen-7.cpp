    int num_l = num.length();
    int cnt = 0;
    for(int i=0;i<num_l;i++){
        if(num[i]=='2' || num[i]=='3' || num[i]=='5' || num[i]=='7'){
            cnt++;
        }else if(num[i]=='A' || num[i]=='B' || num[i]=='C' || num[i]=='D' || num[i]=='E' || num[i]=='F'){
            cnt++;
            if(num[i]=='A'){
                if(i+1<num_l){
                    if(num[i+1]=='B'){
                        cnt++;
                    }else if(num[i+1]=='C'){
                        cnt++;
                    }else if(num[i+1]=='D'){
                        cnt++;
                    }else if(num[i+1]=='E'){
                        cnt++;
                    }else if(num[i+1]=='F'){
                        cnt++;
                    }
                }
            }else if(num[i]=='B'){
                if(i+1<num_l){
                    if(num[i+1]=='C'){
                        cnt++;
                    }else if(num[i+1]=='D'){
                        cnt++;
                    }else if(num[i+1]=='E'){
                        cnt++;
                    }else if(num[i+1]=='F'){
                        cnt++;
                    }
                }
            }else if(num[i]=='C'){
                if(i+1<num_l){
                    if(num[i+1]=='D'){
                        cnt++;
                    }else if(num[i+1]=='E'){
                        cnt++;
                    }else if(num[i+1]=='F'){
                        cnt++;
