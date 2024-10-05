        List<Integer> result  list = new ArrayList<>();
        for  (String group  : paren_string.split(" ")) {
            int current_depth 0;
            int max_depth 0;
            for  (char c  : group.toCharArray()) {
                if  (c == '(') {
                    current_depth  current_depth  + 1;
                    max_depth  Math.max(max_depth, current_depth);
                 } else if  (c == ')') {
                    current_depth  current_depth  - 1;
                 }
             }
            result.add(max_depth);
         }
         return result;
     }
}

