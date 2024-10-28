        List<Integer> evenIndicies = new ArrayList<>();
        for(int i = 0; i < l.size(); i += 2) {
            evenIndicies.add(l.get(i));
        }
        Collections.sort(evenIndicies);

        List<Integer> result = new ArrayList<>();
        int evenIndex = 0;
        for(int i = 0; i < l.size(); i++) {
            if(i % 2 == 0) {
                result.add(evenIndicies.get(evenIndex++));
            } else {
                result.add(l.get(i));
            }
        }
        return result;
    }
}

