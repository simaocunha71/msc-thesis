        List<Integer> counts = new ArrayList<>(Arrays.asList(0, 0));
        for(char c : Integer.toString(Math.abs(num)).toCharArray()) {
            if(Integer.parseInt(String.valueOf(c)) % 2 == 0) {
                counts.set(0, counts.get(0) + 1);
            } else {
                counts.set(1, counts.get(1) + 1);
            }
        }
        return counts;
    }
}

