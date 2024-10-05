        for(int i=0;i<a.length();i++) {
            if (a.substring(i).contains(b)) {
                return true;
            }
            String tmp = b + b;
            if (tmp.contains(a.substring(i))) {
                return true;
            }
        }
        return false;
    }

    public boolean cycpatternCheck2(String a, String b) {
        List<String> list = new ArrayList<>();
        for(int i=0;i<b.length();i++) {
            String tmp = b.substring(i);
            if (tmp.length() > b.length()) {
                break;
            }
            list.add(tmp);
        }
        for(String s : list) {
            if (a.contains(s)) {
                return true;
            }
        }
        return false;
    }

    public boolean cycpatternCheck3(String a, String b) {
        return b.length() <= a.length() && (a.contains(b) || b.substring(0, b.length()-1).contains(b.substring(1)));
    }
}





































































































































































































































