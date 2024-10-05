        boolean flag = true;
        int sum = 0;
        for (int i = 0; i < q.size(); i++) {
            sum += q.get(i);
        }
        if (sum > w) {
            flag = false;
        }
        int left = 0;
        int right = q.size() - 1;
        while (left < right) {
            if (q.get(left) != q.get(right)) {
                flag = false;
            }
            left++;
            right--;
        }
        return flag;
    }
}
