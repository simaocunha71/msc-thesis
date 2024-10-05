        List<Integer> sequence 
= new ArrayList<>(Arrays.asList(3, 1, 2));
        if  (n < 3)  return sequence.subList(0, n + 1);

        for  (int i = 3; i <= n; i++)  {
            if  (i % 2 == 0)  sequence.add(sequence.get(i - 1) + i / 2);
            else  sequence.add(sequence.get(i - 1) + sequence.get(i - 2) + sequence.get(i - 3));
        }
        return sequence;
     }
}

