        Map<Integer, String> map = new HashMap<>();
        map.put(1000, "m");
        map.put(900, "cm");
        map.put(500, "d");
        map.put(400, "cd");
        map.put(100, "c");
        map.put(90, "xc");
        map.put(50, "l");
        map.put(40, "xl");
        map.put(10, "x");
        map.put(9, "ix");
        map.put(5, "v");
        map.put(4, "iv");
        map.put(1, "i");

        StringBuilder sb = new StringBuilder();
        while (number > 0) {
            for (Map.Entry<Integer, String> entry : map.entrySet()) {
                if (number >= entry.getKey()) {
                    sb.append(entry.getValue());
                    number -= entry.getKey();
                    continue A;
                }
            }
        }
        return sb.toString();
    }
}

# Python3 solution
class Solution:
    def intToRoman(self, num: int) -> str:
        def str(i):
            return ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"][i]
        def strs(i):
            return ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"][i]
        def strh(i):
            return ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"][i]
        def strhundreds(i):
            return ["", "M", "MM", "MMM", "MMMM"][i]
        return strhundreds(num//1000) + strh(num%1000//100) + strs(num%100//10