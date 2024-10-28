    int a=value[0]-'0';
    if(a==0){
        return 0;
    }
    else{
        if(a>0){
            if(value[1]=='.'){
                int b=(value[0]-'0')*10;
                int c=(value[0]-'0')*10+9;
                int d=b-c;
                if(d==10){
                    return (value[0]-'0')*10+9;
                }
                else{
                    return (value[0]-'0')*10;
                }
            }
            else{
                int b=(value[0]-'0')*10;
                int c=(value[0]-'0')*10+9;
                int d=b-c;
                if(d==10){
                    return (value[0]-'0')*10+9;
                }
                else{
                    return (value[0]-'0')*10;
                }
            }
        }
        else{
            if(value[1]=='.'){
                int b=((value[0]-'0')*-1)-9;
                int c=((value[0]-'0')*-1)-10;
                int d=b-c;
                if(d==10){
                    return ((value[0]-'0')*-1)-9;
                }
                else{
                    return ((value[0]-'0')*-1)-10;
                }
            }
            else{
                int b=((value[0]-'0')*-1)-9;
                int c=((value[0]-'0')*-1)-10;
                int d=b-c;
                if(d==10){
                    return ((value[0]-'0')*-1)-9;
                }
                else{
                    return ((value[0]-