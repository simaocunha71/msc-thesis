        if (l.size() < 3) return false;
        Collections.sort(l);

        for (int i = 0; i < l.size() - 2; i++) {
            int j = i + 1;
            int k = l.size() - 1;

            while (j < k) {
                int sum = l.get(i) + l.get(j) + l.get(k);
                if (sum == 0) return true;
                else if (sum < 0) j += 1;
                else k -= 1;
            }
        }
        return false;
    }
}

