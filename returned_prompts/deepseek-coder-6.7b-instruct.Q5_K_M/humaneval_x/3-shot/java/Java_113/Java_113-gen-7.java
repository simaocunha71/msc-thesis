        List<String> result = new ArrayList<>();
        for  (String s  : lst)  {
            int count = (int) s.chars()
                                .mapToObj(i -> Character.getNumericValue(i))
                                .filter(i -> i % 2 != 0)
                                .count();
            result.add("the number of odd elements " + count + "n the str" + count + "ng " + count + " of the " + count + "nput.");
         }
        return result;
     }
}

