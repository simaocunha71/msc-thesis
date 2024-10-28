        List<String> romanNumbers = new ArrayList<String>();
        romanNumbers.add("M");
        romanNumbers.add("CM");
        romanNumbers.add("D");
        romanNumbers.add("CD");
        romanNumbers.add("C");
        romanNumbers.add("XC");
        romanNumbers.add("L");
        romanNumbers.add("XL");
        romanNumbers.add("X");
        romanNumbers.add("IX");
        romanNumbers.add("V");
        romanNumbers.add("IV");
        romanNumbers.add("I");

        List<String> miniRoman = new ArrayList<String>();

        while (number > 0) {
            for (String roman : romanNumbers) {
                if (number >= roman.charAt(0) - '0') {
                    number -= roman.charAt(0) - '0';
                    miniRoman.add(roman);
                    break;
                }
            }
        }

        Collections.reverse(miniRoman);
        return String.join("", miniRoman);
    }
}

public class SolutionTest {
    @Test
    public void intToMiniRoman() {
        assertThat(new Solution().intToMiniRoman(19), equalTo("xix"));
        assertThat(new Solution().intToMiniRoman(152), equalTo("clii"));
        assertThat(new Solution().intToMiniRoman(426), equalTo("cdxxvi"));
    }
}
