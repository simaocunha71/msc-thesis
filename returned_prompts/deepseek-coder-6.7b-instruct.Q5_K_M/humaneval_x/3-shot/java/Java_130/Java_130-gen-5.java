        List<Integer> sequence 
        sequence.add(1);
        sequence.add(3);
        sequence.add(2);
        sequence.add(8);
        for (int i = 4; i <= n; i++) {
            if (i % 2 == 0) {
                sequence.add(1 + i / 2);
            } else {
                sequence.add(sequence.get(i - 1) + sequence.get(i - 2) + sequence.get(i + 1));
            }
        }
        return sequence;
    }
}

