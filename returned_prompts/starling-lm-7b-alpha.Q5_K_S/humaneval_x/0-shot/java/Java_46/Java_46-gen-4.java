        int[] array = {0, 0, 2, 0};
        if(n == 0) {
            return array[0];
        }
        if(n == 1) {
            return array[1];
        }
        if(n == 2) {
            return array[2];
        }
        if(n == 3) {
            return array[3];
        }
        int[] newarray = new int[4];
        newarray[0] = array[0];
        newarray[1] = array[1];
        newarray[2] = array[2];
        newarray[3] = array[3] + array[1] + array[0];
        array = newarray;
        n -= 4;
        while(n > 0) {
            int[] temp = new int[4];
            temp[0] = array[0];
            temp[1] = array[1];
            temp[2] = array[2];
            temp[3] = array[3] + array[1] + array[0];
            array = temp;
            n--;
        }
        return array[3];
    }
}






































































































































































































































