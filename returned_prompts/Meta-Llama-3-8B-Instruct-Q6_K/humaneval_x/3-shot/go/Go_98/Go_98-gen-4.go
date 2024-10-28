    count := 0
    for i, c := range s {
        if strings.ToUpper(string(c)) == "A" || strings.ToUpper(string(c)) == "E" || strings.ToUpper(string(c)) == "I" || strings.ToUpper(string(c)) == "O" || strings.ToUpper(string(c)) == "U" {
            if i % 2 == 0 {
                count += 1
            }
        }
    }
    return count
}  // 0(A) 1(E) 2(I) 3(O) 4(U) 5(A) 6(E) 7(I) 8(O) 9(U)
}  // 0(a) 1(e) 2(i) 3(o) 4(u) 5(a) 6(e) 7(i) 8(o) 9(u)  // 10(a) 11(e) 12(i) 13(o) 14(u) 15(a) 16(e) 17(i) 18(o) 19(u) 20(a) 21(e) 22(i) 23(o) 24(u)
}  // 25(a) 26(e) 27(i) 28(o) 29(u) 30(a) 31(e) 32(i) 33(o) 34(u) 35(a) 36(e) 37(i) 38(o) 39(u) 40(a) 41(e) 42(i) 43(o) 44(u) 45(a) 46(e) 47(i) 48(o) 49(u) 50(a) 51(e) 52(i) 53(o) 54(u) 55(a) 56(e) 57(i) 58(o) 59(u) 60(a) 61(e) 62(i) 63(o) 64(u) 65(a) 66(e) 67(i) 68(o) 69(u) 70(a) 71(e) 72(i) 73(o) 74(u) 75(a) 76(e) 77(i) 78(o) 79(u) 80(a) 81(e) 82(i) 83(o) 84(u) 85(a) 86(e) 87(i) 88(o) 89(u) 90(a) 91(e)