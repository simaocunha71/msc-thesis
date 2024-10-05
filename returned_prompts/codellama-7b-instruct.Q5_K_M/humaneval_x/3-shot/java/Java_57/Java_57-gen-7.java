        if (l.size() < 2) return true;

        Integer last = l.get(0);
        int last_change = 0;
        for (int i = 1; i < l.size(); i++) {
            Integer current = l.get(i);
            if (current > last) last_change = 1;
            if (current < last) last_change = -1;
            if (last_change != 0 && last_change != (current - last) / last) return false;
            last = current;
        }
        return true;

    }
}

