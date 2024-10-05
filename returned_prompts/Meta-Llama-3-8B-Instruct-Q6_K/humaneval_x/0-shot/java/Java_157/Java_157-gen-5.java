        // sort the sides to ensure a <= b <= c
        int min = Math.min(Math.min(a, b), c);
        int mid = Math.max(Math.min(a, b), c);
        int max = Math.max(a, b);

        // check if the sides can form a right-angled triangle
        if (min * min + mid * mid == max * max) {
            return true;
        } else {
            return false;
        }
    }
}