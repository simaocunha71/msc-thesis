        int sum = 0;
        boolean isBalanced = true;

        for (int i = 0; i < q.size() / 2; i++) {
            if (q.get(i) != q.get(q.size() - 1 - i)) {
                isBalanced = false;
                break;
            }
            sum += q.get(i);
        }

        return isBalanced && sum <= w;
    }
}

