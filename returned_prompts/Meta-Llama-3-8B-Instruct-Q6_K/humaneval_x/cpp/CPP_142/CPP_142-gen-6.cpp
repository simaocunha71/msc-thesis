    int sum = 0;
    for(int i=0;i<lst.size();i++){
        if(i%3==0 && i%4!=0)
            sum += lst[i]*lst[i];
        else if(i%4==0 && i%3!=0)
            sum += pow(lst[i],3);
    }
    return sum;
}

int main() {
    vector<int> lst = {1,2,3};
    printf("Sum of squares is: %d\n",sum_squares(lst));
    return 0;
}

B:
    int sum = 0;
    for(int i=0;i<lst.size();i++){
        if(i%3==0 && i%4!=0)   // if i is a multiple of 3 and not a multiple of 4
            sum += lst[i]*lst[i];  // square the number
        else if(i%4==0 && i%3!=0)   // if i is a multiple of 4 and not a multiple of 3
            sum += pow(lst[i],3);  // cube the number
    }
    return sum;
}

C:
    int sum = 0;
    for(int i=0;i<lst.size();i++){
        if(i%3==0 && i%4!=0)
            sum += pow(lst[i],2);
        else if(i%4==0 && i%3!=0)
            sum += pow(lst[i],3);
    }
    return sum;
}

D:
    int sum = 0;
    for(int i=0;i<lst.size();i++){
        if(i%3==0 && i%4!=0)
            sum += lst[i]*lst[i];
        else if(i%4==0 && i%3!=0)
            sum += pow(lst[i],3);
    }
    return sum;

E:
    int sum = 0;
    for(int i=0;i<lst.size();i++){
        if(i%3==0 && i%4!=0)
            sum += pow(lst[i],2);
        else if(i%4==0 && i%3!=0)
            sum += pow(lst[i],3);
    }
    return sum;
F:
    int sum = 0;
    for(int i=0;i<lst.size();i++){
        if(i%3==0)
            sum += lst[i]*lst[i];
        else if(i%4==0)
