    int collisions = 0;
    for(int i = 0; i < n; i++){
        for(int j = i + 1; j < n; j++){
            if(i + j == n - 1){
                collisions++;
            }
        }
    }
    return collisions;
} // This function returns the number of collisions. The condition i+j == n-1 checks for the cars that collide. For example, if there are 5 cars, the cars at indices 0 and 4, and the cars at indices 1 and 3, and the cars at indices 2 and 4 will collide. The function does not count the cars that collide with themselves. It also does not count the cars that collide with the cars in the other direction. The function works for any number of cars.