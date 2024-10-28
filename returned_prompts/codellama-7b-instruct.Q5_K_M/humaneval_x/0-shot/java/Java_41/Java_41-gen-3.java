        int collisions = 0;
        int[] leftToRight = new int[n];
        int[] rightToLeft = new int[n];

        for (int i = 0; i < n; i++) {
            leftToRight[i] = i;
            rightToRight[i] = n - i - 1;
        }

        int left = 0;
        int right = n - 1;

        while (left < n && right >= 0) {
            if (leftToRight[left] < rightToLeft[right]) {
                left++;
            } else if (leftToRight[left] > rightToLeft[right]) {
                right--;
            } else {
                collisions++;
                left++;
                right--;
            }
        }
        return collisions;
    }
}



