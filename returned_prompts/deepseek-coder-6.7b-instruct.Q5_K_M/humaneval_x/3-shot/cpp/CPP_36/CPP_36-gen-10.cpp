    int count=0;
    for (int i=0; i<n; i++){
        if (i%11==0 || i%13==0){
            string str = to_string(i);
            for (char c : str){
                if (c == '7'){
                    count++;
                    break;
                }
            }
        }
    }
    return count;
}

