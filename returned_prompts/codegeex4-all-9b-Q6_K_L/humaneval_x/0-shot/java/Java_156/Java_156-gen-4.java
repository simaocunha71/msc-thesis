```java
public String intToMiniRoman(int number) {
        String[] roman = {"m","cm","d","cd","c","xc","l","xl","x","ix","v","iv","i"};
        int[] ints = {1000,900,500,400,100,90,50,40,10,9,5,4,1};
        String result = "";
        for (int i=0; i<ints.length; i++) {
            if (number==0) break;
            while (number-ints[i]>=0) {
                number -= ints[i];
                result += roman[i];
            }
        }
        return result;
    }
```