        StringBuilder sequence 
= new StringBuilder();
        for  (int i = 0; i <= n; i++) {
            sequence.append(i);
            if  (i < n) {
                sequence.append(" ");
             }
         }
        return sequence.toString();
     }
}

