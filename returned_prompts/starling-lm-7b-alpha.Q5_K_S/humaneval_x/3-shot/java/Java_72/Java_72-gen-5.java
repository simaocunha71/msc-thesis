        int left_sum = 0, right_sum = 0;
        for (int i = 0; i < q.size() / 2; i++) {
            left_sum += q.get(i);
        }
        for (int i = q.size() / 2; i < q.size(); i++) {
            right_sum += q.get(i);
        }
        return left_sum <= right_sum && left_sum + right_sum <= w;
    }
}

