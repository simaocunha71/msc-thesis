        Collections.sort(l);
        int len = l.size();

        if  (len % 2 == 0) {
            return ((double)l.get(len / 2 - 1) + (double)l.get(len / 2)) / 2;
        } else {
            return (double) l.get(len / 2);
        }
     }
}

