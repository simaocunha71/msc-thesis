        int sum = 0;
        for (int i : q) {
            sum += i;
        }
        return q.equals(new ArrayList<>(Collections.reverse(q))) && sum <= w;
    }
}

