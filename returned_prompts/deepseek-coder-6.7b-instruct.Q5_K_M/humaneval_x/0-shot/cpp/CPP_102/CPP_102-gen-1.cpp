    if(x>y){
        return -1;
    }
    if(x%2 == 0 && x>=0){
        return x;
    }
    else if(y%2 == 0 && y>=0){
        return y;
    }
    else{
        return choose_num(x+1,y-1);
    }

}

int main(){
    printf("%d\n",choose_num(12,15));
    printf("%d\n",choose_num(13,12));
    return 0;
}

