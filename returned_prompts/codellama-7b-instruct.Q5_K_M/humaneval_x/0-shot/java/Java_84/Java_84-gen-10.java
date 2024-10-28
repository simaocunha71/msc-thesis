        String num = String.valueOf(N);
        String[] str = num.split("");
        int sum = 0;
        for(int i = 0; i < str.length; i++){
            sum += Integer.parseInt(str[i]);
        }
        String res = Integer.toBinaryString(sum);
        return res;
    }
}
