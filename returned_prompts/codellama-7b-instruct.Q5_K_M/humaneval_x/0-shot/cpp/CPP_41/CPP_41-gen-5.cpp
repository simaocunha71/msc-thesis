    if (n == 1) return 0;
    if (n == 2) return 0;
    if (n == 3) return 1;
    int result = 0;
    for (int i = 3; i < n; i++) {
        result += car_race_collision(i);
    }
    return result;
}

