
int car_race_collision(int n){
    if(n <= 0) return 0;
    if(n == 1) return 0;

    if(n % 2 == 0){
        return 2 * car_race_collision(n/2) + car_race_collision(n/2 - 1);
    } else {
        return 2 * car_race_collision(n/2) + car_race_collision(n/2);
    }
}
