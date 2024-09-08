    float num;
    for(int i=0;i<l.size();i++){
        for(int j=i+1;j<l.size();j++){
            if(l[i]>l[j]){
                num=l[i];
                l[i]=l[j];
                l[j]=num;
            }
        }
    }
    if(l.size()%2==0){
        float a=l[(l.size()/2)-1];
        float b=l[l.size()/2];
        return (a+b)/2;
    }
    else{
        return l[l.size()/2];
    }

B:
    float num;
    for(int i=0;i<l.size();i++){
        for(int j=i+1;j<l.size();j++){
            if(l[i]>l[j]){
                num=l[i];
                l[i]=l[j];
                l[j]=num;
            }
        }
    }
    if(l.size()%2==0){
        return (l[(l.size()/2)-1]+l[l.size()/2])/2;
    }
    else{
        return l[l.size()/2];
    }

C:
    float num;
    for(int i=0;i<l.size();i++){
        for(int j=0;j<l.size();j++){
            if(l[i]>l[j]){
                num=l[i];
                l[i]=l[j];
                l[j]=num;
            }
        }
    }
    if(l.size()%2==0){
        return (l[(l.size()/2)-1]+l[l.size()/2])/2;
    }
    else{
        return l[l.size()/2];
    }

D:
    float num;
    for(int i=0;i<l.size();i++){
        for(int j=0;j<l.size();j++){
            if(l[i]>l[j]){
                num=l[i];
                l[i]=l[j];
                l[j]=num;
            }
        }
    }
    if(l.size()%2==0){
        return (l[l.size()/2]+l[l.size()/2])/2;
    }
    else{
        return l[l.size()/2];
    }

E:
    float num;
    for(int i=0;i<l.size();i++){
        for(int j=0;j<l.size();j++){
            if(l[i]>l[j]){
                num=l[i];
                l[i]=l[j];
                l[j]=num;
            }
        }
    }
    if(l.size()%2==0){
        float a=l[(l.size()/2)-1