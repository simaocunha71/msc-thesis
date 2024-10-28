    if a == b {
        return nil
    } else if aFloat, ok := a.(float64); ok {
        if bFloat, ok := b.(float64); ok {
            if aFloat > bFloat {
                return aFloat
            } else {
                return bFloat
            }
        } else if bString, ok := b.(string); ok {
            if bFloat, err := strconv.ParseFloat(bString, 64); err == nil {
                if aFloat > bFloat {
                    return aFloat
                } else {
                    return bFloat
                }
            }
        }
    } else if bFloat, ok := b.(float64); ok {
        if aFloat, ok := a.(float64); ok {
            if aFloat > bFloat {
                return aFloat
            } else {
                return bFloat
            }
        } else if aString, ok := a.(string); ok {
            if aFloat, err := strconv.ParseFloat(aString, 64); err == nil {
                if aFloat > bFloat {
                    return aFloat
                } else {
                    return bFloat
                }
            }
        }
    } else if aString, ok := a.(string); ok {
        if bString, ok := b.(string); ok {
            if aString > bString {
                return aString
            } else {
                return bString
            }
        } else if bFloat, ok := b.(float64); ok {
            if bFloatStr := fmt.Sprintf("%f", bFloat); bFloatStr == aString {
                return aString
            } else {
                return bFloat
            }
        }
    }
    return nil
}



