    int sum = 0;
    for(int i = 0; i < lst.size(); i++){
        if(i % 3 == 0 && i % 4 != 0)
            sum += lst[i] * lst[i] * lst[i];
        else if(i % 4 == 0 && i % 3 != 0)
            sum += lst[i] * lst[i];
        else
            sum += lst[i];
    }
    return sum;
}

int main(){
    vector<int> lst = {1,2,3};
    printf("Sum of squares = %d\n", sum_squares(lst));
    return 0;
}

B:
    int sum_squares(vector<int> lst){
        int sum = 0;
        for(int i = 0; i < lst.size(); i++){
            if((i+1) % 3 == 0 && (i+1) % 4 != 0)
                sum += pow(lst[i], 3);
            else if((i+1) % 4 == 0 && (i+1) % 3 != 0)
                sum += pow(lst[i], 2);
            else
                sum += lst[i];
        }
        return sum;
    }

    int main(){
        vector<int> lst = {1,2,3};
        printf("Sum of squares = %d\n", sum_squares(lst));
        return 0;
    }

C:
    int sum_squares(vector<int> lst){
        int sum = 0;
        for(int i = 0; i < lst.size(); i++){
            if(i % 12 == 0)
                sum += pow(lst[i], 3);
            else if(i % 4 == 0 && i % 3 != 0)
                sum += lst[i] * lst[i];
            else
                sum += lst[i];
        }
        return sum;
    }

    int main(){
        vector<int> lst = {1,2,3};
        printf("Sum of squares = %d\n", sum_squares(lst));
        return 0;
    }

D:
    int sum_squares(vector<int> lst){
        int sum = 0;
        for(int i = 0; i < lst.size(); i++){
            if(i % 4 == 0)
                sum += pow(lst[i], 2);
            else if(i % 3 == 0)
                sum += lst[i]