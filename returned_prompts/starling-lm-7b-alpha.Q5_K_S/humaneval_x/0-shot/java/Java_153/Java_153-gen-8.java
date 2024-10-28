        List<String> names = new ArrayList<>();
        for(String e: extensions) {
            int cap = 0, sm = 0;
            for(int i = 0; i < e.length(); i++) {
                if(Character.isUpperCase(e.charAt(i))) {
                    cap++;
                }
                if(Character.isLowerCase(e.charAt(i))) {
                    sm++;
                }
            }
            String strength = String.valueOf((cap - sm));
            if(names.size() == 0) {
                names.add(strength);
                continue;
            }
            if(strength.equals(names.get(names.size() - 1))) {
                names.add(e);
                continue;
            }
            if(Integer.parseInt(strength) > Integer.parseInt(names.get(names.size() - 1))) {
                names.clear();
                names.add(strength);
                names.add(e);
                continue;
            }
        }
        String res = "";
        for(int i = 0; i < names.size(); i++) {
            res += names.get(i);
        }
        return class_name + "." + res;
    }
}





































































































































































































