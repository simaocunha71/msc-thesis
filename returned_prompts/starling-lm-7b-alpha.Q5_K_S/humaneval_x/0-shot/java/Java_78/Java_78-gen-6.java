    List<Character> list = new ArrayList<>();
    for(int i = 0; i < num.length(); i++) {
        char c = num.charAt(i);
        if(c == '0' || c == '1' || c == '2' || c == '3' || c == '4' || c == '5' || c == '6' || c == '7' || c == '8' || c == '9') {
            if(c == '0') {
                list.add('2');
            } else if(c == '1') {
                list.add('3');
            } else if(c == '2') {
                list.add('5');
            } else if(c == '3') {
                list.add('7');
            } else if(c == '4') {
                list.add('11');
            } else if(c == '5') {
                list.add('13');
            } else if(c == '6') {
                list.add('17');
            } else if(c == '7') {
                list.add('19');
            } else if(c == '8') {
                list.add('23');
            } else {
                list.add('29');
            }
            continue A;
        } else if(c == 'A' || c == 'B' || c == 'C' || c == 'D' || c == 'E' || c == 'F') {
            if(c == 'A') {
                list.add('3');
            } else if(c == 'B') {
                list.add('11');
            } else if(c == 'C') {
                list.add('13');
            } else if(c == 'D') {
                list.add('17');
            } else if(c == 'E') {
                list.add('19');
            } else {
                list.add('23');
            }
            continue A;
        } else {
            continue A;
        }
    }
    return list