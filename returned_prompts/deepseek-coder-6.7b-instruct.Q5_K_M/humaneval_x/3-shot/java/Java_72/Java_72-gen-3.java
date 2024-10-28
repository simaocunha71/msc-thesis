        int sum = 0;
        for (int i : q) {
            sum += i;
        }

        if (sum > w) {
            return false;
        }

        Collections.reverse(q);
        return q.equals(q);
    }
}

