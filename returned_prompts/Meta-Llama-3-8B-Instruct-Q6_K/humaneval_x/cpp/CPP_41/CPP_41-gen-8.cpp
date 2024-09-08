    int collisions = 0;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if(i != j){
                if((i+j+1)%2 == 0){
                    collisions++;
                }
            }
        }
    }
    return collisions;
}

int main(){
    int n;
    scanf("%d", &n);
    printf("%d\n", car_race_collision(n));
    return 0;
}

