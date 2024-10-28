        int sum = 0;
        int i = 0, j = q.size() - 1;
        while (i < j) {
            if (!q.get(i).equals(q.get(j))) {
                return false;
            }
            sum += q.get(i);
            i++;
            j--;
        }
        if (q.size() % 2 != 0) {
            sum += q.get(i);
        }
        return sum <= w;
    }
}

