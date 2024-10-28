        int aUnit = a % 10;
        int bUnit = b % 10;
        int aUnitDigit = aUnit;
        int bUnitDigit = bUnit;
        int aTenDigit = (a % 100) / 10;
        int bTenDigit = (b % 100) / 10;
        int aHundredDigit = a / 100;
        int bHundredDigit = b / 100;
        int aThousandDigit = (a % 10000) / 1000;
        int bThousandDigit = (b % 10000) / 1000;

        int product = aUnit * bUnit;
        int result = product + aTenDigit * bUnitDigit + aUnitDigit * bTenDigit;
        result = result + aHundredDigit * bUnitDigit + aUnitDigit * bHundredDigit;
        result = result + aThousandDigit * bUnitDigit + aUnitDigit * bThousandDigit;

        return result;
    }
}
