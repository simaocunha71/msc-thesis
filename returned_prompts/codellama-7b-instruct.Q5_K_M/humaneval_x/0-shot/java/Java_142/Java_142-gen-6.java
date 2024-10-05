        for(int i = 0; i < lst.size(); i++){
            if(i % 3 == 0 && i % 4 == 0){
                lst.set(i, Math.pow(lst.get(i), 3));
            }else if(i % 3 == 0){
                lst.set(i, Math.pow(lst.get(i), 2));
            }
        }
        return lst.stream().mapToInt(i->i).sum();
    }
}

