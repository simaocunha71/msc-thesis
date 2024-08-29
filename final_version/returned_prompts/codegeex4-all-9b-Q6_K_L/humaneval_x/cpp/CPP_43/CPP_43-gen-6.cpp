bool res=false;
int sum=0;
for(int i=0;i<l.size();i++){
    for(int j=i+1;j<l.size();j++){
        sum=l[i]+l[j];
        if(sum==0){
            res=true;
            break;
        }
    }
}
return res;
}

B:
bool pairs_sum_to_zero(vector<int> l){

bool res=false;
for(int i=0;i<l.size();i++){
    for(int j=i+1;j<l.size();j++){
        if(l[i]+l[j]==0){
            res=true;
            break;
        }
    }
}
return res;
}

C:
bool pairs_sum_to_zero(vector<int> l){

bool res=false;
for(int i=0;i<l.size();i++){
    for(int j=i+1;j<l.size();j++){
        if(l[i]+l[j]==0){
            res=true;
        }else{
            res=false;
        }
    }
}
return res;
}

D:
bool pairs_sum_to_zero(vector<int> l){

bool res=false;
int sum=0;
for(int i=0;i<l.size();i++){
    sum=l[i];
    for(int j=i+1;j<l.size();j++){
        sum+=l[j];
        if(sum==0){
            res=true;
            break;
        }
    }
}
return res;
}

E:
bool pairs_sum_to_zero(vector<int> l){

bool res=false;
int sum=0;
for(int i=0;i<l.size();i++){
    for(int j=i+1;j<l.size();j++){
        if(l[i]+l[j]==0){
            res=true;
            break;
        }
    }
    if(res==true){
        break;
    }
}
return res;
}

F:
bool pairs_sum_to_zero(vector<int> l){

bool res=false;
for(int i=0;i<l.size();i++){
    for(int j=i+1;j<l.size();j++){
        if(l[i]+l[j]==0){
            res=true;
        }else{
            res=false;
        }
    }
    if(res==false){
        break;
    }
}
return res;
}

G:
bool pairs_sum_to_zero(vector<int> l){

bool res=false;
for(int i=0;i<l.size();i++){
    for(int j=i+1;j<l.size();j++){
        if(l[i]+l[j]==0){
            res=true;
        }
    }
    if(res==true){
        break;
    }
}
