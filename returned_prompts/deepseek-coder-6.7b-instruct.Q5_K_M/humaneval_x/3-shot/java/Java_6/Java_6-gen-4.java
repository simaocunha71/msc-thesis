        List<Integer> result = new ArrayList<>();
        for  (String group : paren_string.split(" ")) {
            int current_max =0, current_count =0;
            for  (char c : group.toCharArray())  {
                if  (c == '(')  {
                    current_count += 1;
                    current_max = Math.max(current_max, current_count);
                } else if  (c == ')')  {
                    current_count -= 1;
                }
             }
            result.add(current_max);
        }
        return result;
     }
}

