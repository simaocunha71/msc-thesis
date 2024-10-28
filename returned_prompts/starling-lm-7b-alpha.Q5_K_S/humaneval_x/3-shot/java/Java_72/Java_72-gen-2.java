        int sum = q.stream().mapToInt(i -> i).sum();
        if (sum > w) return false;
        int left = 0;
        int right = q.size() - 1;
        while (left < right) {
            if (q.get(left) != q.get(right)) return false;
            left += 1;
            right -= 1;
        }
        return true;
    }
}

