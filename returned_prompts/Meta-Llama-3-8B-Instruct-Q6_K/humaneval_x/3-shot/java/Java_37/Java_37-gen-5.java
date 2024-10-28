        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < l.size(); i++) {
            if (i % 2 == 0) {
                List<Integer> evenNumbers = new ArrayList<>();
                for (int j = 0; j < l.size(); j++) {
                    if (j % 2 == 0) {
                        evenNumbers.add(l.get(j));
                    }
                }
                Collections.sort(evenNumbers);
                result.add(evenNumbers.get(0));
            } else {
                result.add(l.get(i));
            }
        }
        return result;
    }
} 