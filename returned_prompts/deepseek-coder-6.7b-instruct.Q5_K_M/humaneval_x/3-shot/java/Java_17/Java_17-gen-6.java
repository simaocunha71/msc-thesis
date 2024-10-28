        List<Integer> beats = new ArrayList<>();
        for(String note : string.split(" ")) {
            switch(note) {
                case "o": beats.add(4); break;
                case "o|": beats.add(2); break;
                case ".|": beats.add(1); break;
            }
        }
        return beats;
     }
}

