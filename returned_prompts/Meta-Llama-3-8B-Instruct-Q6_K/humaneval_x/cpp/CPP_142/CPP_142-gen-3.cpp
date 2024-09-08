    int sum = 0;
    for(int i = 0; i < lst.size(); i++){
        if(i % 3 == 0 && i % 4 != 0){
            sum += lst[i] * lst[i] * lst[i];
        }
        else if(i % 4 == 0 && i % 3 != 0){
            sum += lst[i] * lst[i] * lst[i] * lst[i] * lst[i] * lst[i];
        }
        else{
            sum += lst[i];
        }
    }
    return sum;
}

int main() {
    vector<int> lst = {1,2,3};
    printf("%d\n",sum_squares(lst));
    return 0;
}

B:
    int sum = 0;
    for(int i = 0; i < lst.size(); i++){
        if(i % 3 == 0 && i % 4 != 0){
            sum += pow(lst[i],3);
        }
        else if(i % 4 == 0 && i % 3 != 0){
            sum += pow(lst[i],4);
        }
        else{
            sum += lst[i];
        }
    }
    return sum;
}
int main() {
    vector<int> lst = {1,2,3};
    printf("%d\n",sum_squares(lst));
    return 0;
}

C:
    int sum = 0;
    for(int i = 0; i < lst.size(); i++){
        if(i % 3 == 0 && i % 4 != 0){
            sum += lst[i]*lst[i];
        }
        else if(i % 4 == 0 && i % 3 != 0){
            sum += pow(lst[i],3);
        }
        else{
            sum += lst[i];
        }
    }
    return sum;
}

D:
    int sum = 0;
    for(int i = 0; i < lst.size(); i++){
        if(i % 3 == 0 && i % 4 != 0){
            sum += pow(lst[i],3);
        }
        else if(i % 4 == 0 && i % 3 != 0){
            sum += lst[i]*lst[i]*lst[i];
        }
        else{
            sum += lst[i];
        }
    }
    return sum;
}

E:
    int sum = 0;
    for(int i = 0;