        for (int i = 0; i < numbers.size(); i++) {
            for (int j = i + 1; j < numbers.size(); j++) {
                double distance = Math.abs(numbers.get(i) - numbers.get(j));
                if (distance < threshold) return true;
            }
        }
        return false;
    }

This is an O(n^2) solution to the problem. It's not great, but it is correct. In general, it's hard to avoid an O(n^2) solution for this problem because you do have to check every pair of numbers.

