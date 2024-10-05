        List<Integer> result = new ArrayList<>();
        List<Integer> temp1 = new ArrayList<>(l1);
        List<Integer> temp2 = new ArrayList<>(l2);
        temp1.retainAll(temp2);
        temp1.sort(Comparator.naturalOrder());
        temp1.forEach(item -> {
            if(result.contains(item)){
                return;
            }
            result.add(item);
        });
        return result;
    }
}





