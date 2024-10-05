        List<Integer> copy = new ArrayList<>(array);
        int sum = array.get(0) + array.get(array.size() - 1);
        Collections.sort(copy);
        if(sum % 2 == 0) 
            Collections.reverse(copy);
        return copy;
     }
}

