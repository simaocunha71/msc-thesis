        int sum = 0;
        for (int i = 0; i < q.size(); i++) {
            sum += q.get(i);
        }

        if (sum > w) {
            return false;
        }

        int start = 0;
        int end = q.size() - 1;

        while (start < end) {
            if (q.get(start) != q.get(end)) {
                return false;
            }
            start++;
            end--;
        }

        return true;
    }
}

