        int sum = 0;
        for (int i : q) {
            sum += i;
        }
        if (sum > w) return false;
        int left = 0;
        int right = q.size() - 1;
        while (left < right) {
            if (q.get(left) != q.get(right)) return false;
            left++;
            right--;
        }
        return true;
    }
}

