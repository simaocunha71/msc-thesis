    int collisions = 0;
    for(int i = 1; i <= n; i++) {
        for(int j = 1; j <= n; j++) {
            if(i != j) {
                int collision_distance = i - j;
                if(collision_distance % 2 == 1) {
                    collisions++;
                }
            }
        }
    }
    return collisions;
}