        int sum = 0;
        for (int i : q) {
            sum += i;
        }
        if (sum > w) {
            return false;
        }
        return q.equals(new ArrayList<>(Collections.reverse(q)));
    }
}

