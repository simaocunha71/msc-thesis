        int aUnit = a % 10;
        int bUnit = b % 10;
        int aTen = a / 10;
        int bTen = b / 10;
        int aUnitBUnit = aUnit * bUnit;
        int aTenBTen = aTen * bTen;
        int aUnitBTen = aUnit * bTen;
        int aTenBUnit = aTen * bUnit;
        int result = aUnitBUnit + aTenBTen + aUnitBTen + aTenBUnit;
        return result;
    }
}
