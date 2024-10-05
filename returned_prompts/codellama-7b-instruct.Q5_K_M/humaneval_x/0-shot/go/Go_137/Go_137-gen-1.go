	switch a.(type) {
	case int:
		switch b.(type) {
		case int:
			if a.(int) > b.(int) {
				return a
			} else {
				return nil
			}
		case float64:
			if a.(int) > int(b.(float64)) {
				return a
			} else {
				return nil
			}
		case string:
			if float64(a.(int)) > stringToFloat64(b.(string)) {
				return a
			} else {
				return nil
			}
		}
	case float64:
		switch b.(type) {
		case int:
			if a.(float64) > float64(b.(int)) {
				return a
			} else {
				return nil
			}
		case float64:
			if a.(float64) > b.(float64) {
				return a
			} else {
				return nil
			}
		case string:
			if a.(float64) > stringToFloat64(b.(string)) {
				return a
			} else {
				return nil
			}
		}
	case string:
		switch b.(type) {
		case int:
			if stringToFloat64(a.(string)) > float64(b.(int)) {
				return a
			} else {
				return nil
			}
		case float64:
			if stringToFloat64(a.(string)) > b.(float64) {
				return a
			} else {
				return nil
			}
		case string:
			if stringToFloat64(a.(string))