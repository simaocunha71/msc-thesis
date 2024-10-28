        List<Integer> sortedThird = new ArrayList<>();
        List<Integer> third = new ArrayList<>();
        for(int i = 0; i < l.size(); i++) {
            if(i % 3 == 0) {
                third.add(l.get(i));
            }
        }
        Collections.sort(third);
        int thirdIndex = 0;
        for(int i = 0; i < l.size(); i++) {
            if(i % 3 == 0) {
                sortedThird.add(third.get(thirdIndex++));
            } else {
                sortedThird.add(l.get(i));
            }
        }
        return sortedThird;
    }
}

