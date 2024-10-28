    int count=0;
    char buffer[50];
    for(int i=11; i<n; i++){
        if(i%11==0 || i%13==0){
            sprintf(buffer, "%d", i);
            for(int j=0; buffer[j] != 0; j++){
                if(buffer[j] == '7'){
                    count++;
                    break;
                }
            }
        }
    }
    return count;
}


