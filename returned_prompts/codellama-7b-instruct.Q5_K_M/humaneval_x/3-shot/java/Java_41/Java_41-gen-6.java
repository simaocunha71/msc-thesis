        // this is a clever approach
        // the key insight is that we can simplify the problem by only considering the right-most
        // car of the left-going cars and the left-most car of the right-going cars.
        // this way we can reduce the problem to a smaller set of cars and a smaller
        // time period.  We can repeat this process for a number of times, which is
        // the number of times we have to consider the left and right most cars.

        // this is the number of times we repeat the process
        int num_iterations = (n-1)/2;
        // this is the number of times we have to consider the left and right most cars
        int num_cars = n;

        int total_collisions = 0;

        for (int i = 0; i < num_iterations; i++) {
            // this is the number of cars we have to consider in the next iteration
            int next_num_cars = num_cars / 2;

            // this is the number of cars we have to consider in the current iteration
            int curr_num_cars = num_cars;

            // this is the number of cars we have to consider in the next iteration
            int prev_num_cars = next_num_cars;

            // this is the number of cars we have to consider in the current iteration
            int curr_iteration_collisions = 0;

            for (int j = 0; j < curr_num_cars; j++) {
                // this is the number of collisions in the current iteration
                int curr_collisions = 0;

                // this is the number of cars we have to consider in the next iteration
                int next_collisions = 0;

                for (int k = j+1; k < curr_num_cars; k++) {
                    // if the cars collide, increment the number of collisions
                    if (j > k) {
                        curr_collisions += 1;
                    } else {
                        next_collisions += 1;
                    }
                }

                // if the cars collide, increment the number of collisions
