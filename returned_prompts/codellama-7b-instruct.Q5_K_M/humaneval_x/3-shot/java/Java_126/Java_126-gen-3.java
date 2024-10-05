        if (lst.size() <= 1) return true;

        int last = lst.get(0);

        for (int i = 1; i < lst.size(); i++) {
            int current = lst.get(i);

            if (current < last) return false;

            if (current == last) {
                lst.remove(i);
                i -= 1;
            }

            last = current;
        }

        return true;
    }
}

