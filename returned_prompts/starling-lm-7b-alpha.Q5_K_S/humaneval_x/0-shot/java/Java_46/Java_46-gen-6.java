    int[] fibArr = {0, 0, 2, 0};
    if (n < 0) {
      return -1;
    } else if (n == 0) {
      return 0;
    } else if (n == 1) {
      return 0;
    } else if (n == 2) {
      return 2;
    } else if (n == 3) {
      return 0;
    } else {
      int tmp = 0;
      while (tmp != n) {
        tmp = fibArr[tmp];
        int tmp2 = 0;
        int[] tmpArr = {0, 0, 2, 0};
        while (tmp2 != tmp) {
          tmp2 = tmpArr[tmp2];
          int[] tmpArr2 = {0, 0, 2, 0};
          while (tmp2 != tmpArr2[tmp2]) {
            tmpArr2[tmp2] = tmpArr[tmpArr2[tmp2]];
          }
          for (int i = 0; i < 4; i++) {
            tmpArr[i] = tmpArr2[i];
          }
        }
        fibArr[tmp] = tmpArr[tmp];
      }
      return fibArr[n];
    }
    }
}




































































































































































































