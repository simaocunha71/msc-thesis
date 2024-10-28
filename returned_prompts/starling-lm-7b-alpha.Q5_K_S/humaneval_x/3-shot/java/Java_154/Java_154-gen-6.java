        Set<String> rotations = getRotations(b);
        for (String rotation : rotations) {
            if (a.contains(rotation)) return true;
        }
        return false;
    }

    private Set<String> getRotations(String word) {
        Set<String> rotations = new HashSet<>();
        for (int i = 0; i < word.length(); i++) {
            String rotation = word.substring(i) + word.substring(0, i);
            rotations.add(rotation);
        }
        return rotations;
    }
}

