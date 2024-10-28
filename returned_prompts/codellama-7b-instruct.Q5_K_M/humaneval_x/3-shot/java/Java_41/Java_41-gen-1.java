        int left_to_right = n;
        int right_to_left = n;
        int collisions = 0;

        while (left_to_right > 0) {
            collisions += left_to_right;
            right_to_left -= left_to_right;
            left_to_right = right_to_left;
        }

        return collisions;
    }
}

