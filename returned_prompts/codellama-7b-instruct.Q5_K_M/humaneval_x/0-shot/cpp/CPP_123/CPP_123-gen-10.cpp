    return 
}

int main(){
    vector<int> v = get_odd_collatz(5);
    for(int i=0;i<v.size();i++){
        printf("%d ", v[i]);
    }
    printf("\n");
    return 0;
}


