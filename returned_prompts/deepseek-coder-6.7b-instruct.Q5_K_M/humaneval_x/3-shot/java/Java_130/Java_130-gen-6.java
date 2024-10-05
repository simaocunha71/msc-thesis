        List<Integer> tri_sequence  = new ArrayList<>();
        if  (n  < 0) return tri_sequence;

        if  (n  >=  0) tri_sequence.add(1);
        if  (n  >=  1) tri_sequence.add(3);
        if  (n  >=  2) tri_sequence.add(2);
        if  (n  >=  3) tri_sequence.add(8);

        for  (int i  =  3; i  < n; i++) {
            if  (i  %  2  !=  0) {
                int next_number  = tri_sequence.get(i  -  1)  + tri_sequence.get(i  -  2)  + tri_sequence.get(i  +  1);
                tri_sequence.add(next_number);
            }  else {
                int next_number  = 1  +  (i  /  2);
                tri_sequence.add(next_number);
             }
         }
        return tri_sequence;
     }
}


A: The code you have posted is correct. It seems that there might be some issues with the formatting or the way you're asking the questions.

