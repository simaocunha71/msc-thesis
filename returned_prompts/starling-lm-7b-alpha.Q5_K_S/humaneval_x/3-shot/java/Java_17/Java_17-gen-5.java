        List<Integer> result = new ArrayList<>();
        StringBuilder notes = new StringBuilder();
        for (char c : string.toCharArray()) {
            if (c != '|') notes.append(c);
            else {
                if (notes.length() == 1) result.add(4);
                else if (notes.length() == 2) result.add(2);
                else result.add(1);
                notes.setLength(0);
            }
        }
        return result;
    }
}

