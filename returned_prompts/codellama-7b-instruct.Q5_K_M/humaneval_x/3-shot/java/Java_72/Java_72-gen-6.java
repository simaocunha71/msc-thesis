        // is q balanced
        boolean is_balanced = true;
        for (int i = 0; i < q.size() / 2; i++) {
            if (q.get(i) != q.get(q.size() - i - 1)) {
                is_balanced = false;
                break;
            }
        }
        // is the sum of the elements less than the max weight
        int sum = 0;
        for (int element : q) {
            sum += element;
        }
        return is_balanced && sum <= w;
    }
}

