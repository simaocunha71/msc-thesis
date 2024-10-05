    int s = n;
    while (s > 0) {
        s--;
        if (s == 0) {
            return 0;
        }
        if (s == 1) {
            return 1;
        }
        if (s % 2 == 0) {
            goto A;
        }
    }
    return -1;
}

int main(){
    int n;
    scanf("%d", &n);
    printf("%d", car_race_collision(n));
    return 0;
}





/*
This program is wrong, but I don't know where exactly.

The idea is to figure out how many collisions there will be.

A car will collide with another car if it's traveling at the same speed
as another car from the opposite side.  If a car is traveling left to right
at the same speed as a car traveling right to left, then they will collide.

The first step in the program is to find out how many cars are moving at
the same speed on the same side.  If n = 3, then 1 car is moving at full
speed, 1 car is moving at half speed, and 1 car is moving at one-third speed.

The number of cars moving at each speed is equal to the number of cars,
since all cars move at the same speed.

The number of collisions is the number of cars on the left side, times the
number of cars on the right side.

The code is wrong, though, and I don't know how to fix it.  It's not
even clear to me that this is the right approach to the problem.

*/






















































































































