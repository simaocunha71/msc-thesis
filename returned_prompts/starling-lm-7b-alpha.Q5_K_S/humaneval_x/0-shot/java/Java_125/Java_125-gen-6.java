



if (txt.contains(" ")) {
    String[] arr = txt.split(" ");
    for (String str : arr) {
        System.out.println(str);
    }
} else if (txt.contains(",")) {
    String[] arr = txt.split(",");
    for (String str : arr) {
        System.out.println(str);
    }
} else {
    int count = 0;
    for (int i = 0; i < txt.length(); i++) {
        char c = txt.charAt(i);
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'y') {
            continue;
        }
        if ((c + "").matches("[a-z]{1}")) {
            if (((c + "")).equals("b") || ((c + "")).equals("d") || ((c + "")).equals("f") || ((c + "")).equals("h") || ((c + "")).equals("j") || ((c + "")).equals("k") || ((c + "")).equals("l") || ((c + "")).equals("n") || ((c + "")).equals("p") || ((c + "")).equals("q") || ((c + "")).equals("r") || ((c + "")).equals("t") || ((c + "")).equals("v") || ((c + "")).equals("x") || ((c + "")).equals("z")) {
                if (c % 2 != 0) {
                    count++;
                }
            }
        }
    }
    System.out.println(count);
}
















    }
}







```
