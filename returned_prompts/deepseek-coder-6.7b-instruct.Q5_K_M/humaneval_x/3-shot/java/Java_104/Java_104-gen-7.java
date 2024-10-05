        List<Integer> result = new ArrayList<>();
        for(Integer num : x) {
            if(num % 2 != 0) {
                result.add(num);
            }
        }
        Collections.sort(result);
        return result;
     }
}

