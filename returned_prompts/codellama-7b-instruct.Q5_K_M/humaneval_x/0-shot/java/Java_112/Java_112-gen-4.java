        List<Object> r = new ArrayList<Object>();
        String[] a = new String[c.length()];
        int j = 0;
        for(int i = 0; i<c.length(); i++){
            if(c.charAt(i) != c.charAt(i-1)){
                a[j] = c.charAt(i)+"";
                j++;
            }
        }
        String result = s.replaceAll("["+a[0]+"]", "");
        r.add(result);
        for(int i = 1; i<a.length; i++){
            result = result.replaceAll("["+a[i]+"]", "");
        }
        r.add(result.equals(new StringBuilder(result).reverse().toString()));
        return r;
    }
}

