List<Integer> result = new ArrayList<>();
for(int i = Math.min(a, b); i <= Math.max(a, b); i++) {
    String str = Integer.toString(i);
    for(int j = 0; j < str.length(); j++) {
        if(str.charAt(j) % 2 == 0) {
            result.add(Integer.parseInt(str.substring(j, j+1)));
        }
    }
}
return result;
    }
}
