        Set<Integer> elements = new HashSet<>(l);

        for (int i = 0; i < l.size(); i++) {
            for (int j = i + 1; j < l.size(); j++) {
                int k = -1 * (l.get(i) + l.get(j));
                if (elements.contains(k)) return true;
            }
        }
        return false;
    }
}




```