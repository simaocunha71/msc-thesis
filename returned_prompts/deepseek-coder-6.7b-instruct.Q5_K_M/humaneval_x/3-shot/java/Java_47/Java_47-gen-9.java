        Collections.sort(l);
        int size = l.size();
        if  (size % 2 == 0) {
            return (l.get(size/2 - 1) + l.get(size/2)) / 2.0;
        } else {
            return l.get(size/2);
        }
     }
}

