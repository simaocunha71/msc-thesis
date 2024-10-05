        Set<Integer> seen = new HashSet<>();
        for (int i : l) {
            if (seen.contains(-i)) return true;
            seen.add(i);
        }
        return false;

    }
}

