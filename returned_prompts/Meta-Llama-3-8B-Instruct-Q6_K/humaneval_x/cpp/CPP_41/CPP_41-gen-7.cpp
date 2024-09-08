    int ans = 0; // Initialize the answer as 0

    // Calculate the total distance the left-moving cars will cover
    int left_distance = n*(n-1)*(2*n-1)/6;

    // Calculate the total distance the right-moving cars will cover
    int right_distance = n*(n-1)*(2*n-1)/6;

    // Calculate the total distance the two sets of cars will cover together
    int total_distance = left_distance + right_distance;

    // Calculate the total number of collisions
    ans = total_distance;

    return ans;
}

int main() {
    int n;
    printf("Enter the number of cars: ");
    scanf("%d", &n);
    printf("The number of collisions is: %d\n", car_race_collision(n));
    return 0;
}

