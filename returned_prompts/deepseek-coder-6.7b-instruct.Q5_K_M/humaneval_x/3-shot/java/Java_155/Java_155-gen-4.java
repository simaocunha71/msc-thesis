        List<Integer> counts = new ArrayList<Integer>(Arrays.asList(0, 0));
        for(char c: Integer.toString(Math.abs(num)).toCharArray()) {
            counts.set(Character.getNumericValue(c) % 2, counts.get(Character.getNumericValue(c) % 2) + 1);
        }
        return counts;
     }
}

