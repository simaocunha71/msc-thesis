        Set<Integer> seen = new HashSet<>();

        for (int i = 0; i < l.size(); i++) {
            int target = 0 - l.get(i);
            if (seen.contains(target)) return true;
            seen.add(l.get(i));
        }
        return false;
    }
}

