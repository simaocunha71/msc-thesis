    int count = 0;
    while(true){
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) {
                printf("L %d\n", i);
            } else {
                printf("R %d\n", i);
            }
        }
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) {
                printf("L %d\n", i);
            } else {
                printf("R %d\n", i);
            }
        }

        if (count >= n) {
            break;
        }
        count += 2;
        if (count >= n) {
            break;
        }
    }
    return count;
}

int main() {
    int n;
    scanf("%d", &n);
    printf("collisions: %d\n", car_race_collision(n));
    return 0;
}









/*
Imagine a road that's a perfectly straight infinitely long line.
n cars are driving left to right;  simultaneously, a different set of n cars
are driving right to left.   The two sets of cars start out being very far from
each other.  All cars move in the same speed.  Two cars are said to collide
when a car that's moving left to right hits a car that's moving right to left.
However, the cars are infinitely sturdy and strong; as a result, they continue moving
in their trajectory as if they did not collide.

This function outputs the number of such collisions.

*/











































































































