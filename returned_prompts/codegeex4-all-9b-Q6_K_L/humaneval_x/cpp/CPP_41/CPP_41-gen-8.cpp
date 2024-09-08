/*
This is my solution.  I was told it's wrong.  I don't understand why it's wrong.
*/
int t = 0;
for (int i = 1; i <= n; i++) {
    t = t + (i * (n-i+1));
}
return t;
}

B:
/*
This is the solution given to me.  I understand this solution but I don't understand why my solution is wrong.
*/
int car_race_collision(int n){
    int t = 0;
    for (int i = 1; i <= n; i++) {
        t = t + i;
    }
    return t * n;
}

C:
/*
This is another solution that I was told is correct.  I don't understand why my solution is wrong.
*/
int car_race_collision(int n){
    int t = 0;
    for (int i = 1; i <= n; i++) {
        t = t + (i * (i-1) / 2);
    }
    return t * 2;
}

