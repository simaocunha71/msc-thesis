        int sum = 0;
        for (int i : q) {
            sum += i;
        }
        if (sum > w) {
            return false;
        }
        return q.toString().equals(new StringBuilder(q.toString()).reverse().toString());
    }
}

