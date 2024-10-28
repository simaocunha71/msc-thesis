        Collections.sort(lst);
        int target = lst.get(lst.size() - 1);
        int frequency = Collections.frequency(lst, target);

        for (int i = target - 1; i > 0; i--) {
            int freq = Collections.frequency(lst, i);
            if (freq >= i) return i;
        }
        return -1;
    }
}

