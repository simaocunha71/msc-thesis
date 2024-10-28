    int count=0;
    for(int i=0;i<num.size();i++){
        char ch=num[i];
        if(ch=='2' || ch=='3' || ch=='5' || ch=='7' || ch=='B' || ch=='D'){
            count++;
        }
    }
    return count;
}



