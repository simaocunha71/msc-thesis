        List<Integer> result = new ArrayList<>();

        for(Object obj : values) {
            if(obj instanceof Integer) {
                result.add((Integer) obj);
            }
        }

        return result;
     }
}

