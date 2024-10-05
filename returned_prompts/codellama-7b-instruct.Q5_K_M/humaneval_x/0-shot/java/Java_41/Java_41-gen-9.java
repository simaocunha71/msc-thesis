        int collisions = 0;
        int mid = n / 2;
        int leftToRight = 0;
        int rightToLeft = 0;
        for (int i = 0; i < n; i++) {
            if (i < mid) {
                leftToRight++;
            } else {
                rightToLeft++;
            }
        }
        while (leftToRight > 0 && rightToLeft > 0) {
            if (leftToRight > rightToLeft) {
                rightToLeft--;
                leftToRight--;
            } else if (leftToRight < rightToLeft) {
                leftToRight--;
                rightToLeft--;
            } else {
                collisions++;
                rightToLeft--;
                leftToRight--;
            }
        }

        return collisions;

    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.carRaceCollision(10));
    }
}
