    int[] arr = new int[numbers.length()];
    for (int i = 0; i < arr.length; i++) {
        switch (numbers.charAt(i)) {
            case 'zero':
                arr[i] = 0;
                break;
            case 'one':
                arr[i] = 1;
                break;
            case 'two':
                arr[i] = 2;
                break;
            case 'three':
                arr[i] = 3;
                break;
            case 'four':
                arr[i] = 4;
                break;
            case 'five':
                arr[i] = 5;
                break;
            case 'six':
                arr[i] = 6;
                break;
            case 'seven':
                arr[i] = 7;
                break;
            case 'eight':
                arr[i] = 8;
                break;
            case 'nine':
                arr[i] = 9;
                break;
        }
    }
    Arrays.sort(arr);
    StringBuilder sb = new StringBuilder();
    for (int num : arr) {
        switch (num) {
            case 0:
                sb.append("zero");
                break;
            case 1:
                sb.append("one");
                break;
            case 2:
                sb.append("two");
                break;
            case 3:
                sb.append("three");
                break;
            case 4:
                sb.append("four");
                break;
            case 5:
                sb.append("five");
                break;
            case 6:
                sb.append("six");
                break;
            case 7:
                sb.append("seven");
                break;
            case 8:
                sb.append("eight");
                break;
            case 9:
                sb.append("nine");
                break;
        }
