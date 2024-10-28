        int left = 0;
        int right = q.size() - 1;
        int total = 0;

        while (left < right) {
            if (q.get(left) > q.get(right)) {
                return false;
            }
            total += q.get(left) + q.get(right);
            left += 1;
            right -= 1;
        }
        return total <= w;
    }
}

