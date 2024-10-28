        int result = 0;
        int[] memo = new int[arr.size()];
        int min_change = Integer.MAX_VALUE;

        for (int i = 0; i < arr.size(); i++) {
            int current_value = arr.get(i);
            int current_change = 0;
            for (int j = i + 1; j < arr.size(); j++) {
                if (memo[j] == 0) break;
                int change = Math.abs(arr.get(i) - arr.get(j));
                current_change += change;
                min_change = Math.min(min_change, change);
            }
            memo[i] = current_change;
            result += current_change;
        }

        return result + min_change;
    }
}

