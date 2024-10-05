        List<Integer> sequence = new ArrayList<Integer>();
        sequence.add(1);
        if(n == 0) return sequence;
        sequence.add(3);
        if(n == 1) return sequence;
        sequence.add(2);
        if(n == 2) return sequence;
        for(int i = 3; i <= n; i++) {
            if(i % 2 == 0) {
                sequence.add(1 + i / 2);
            } else {
                sequence.add(sequence.get(i - 1) + sequence.get(i - 2) + sequence.get(i + 1));
            }
        }
        return sequence;
     }
}

