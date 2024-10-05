public class CarRace {
    public int carRaceCollision(int n) {
        int[] left = new int[n];
        int[] right = new int[n];
        int collisions = 0;
        for (int i = 0; i < n; i++) {
            left[i] = i;
            right[i] = n - 1 - i;
        }
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (left[i] < right[j] && right[j] < left[i] + right[j]) {
                    collisions++;
                    right[j] = n + 1;
                    left[i] = n + 1;
                }
            }
        }
        return collisions;
    }
}

