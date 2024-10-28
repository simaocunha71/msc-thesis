	if a == nil && b == nil {
		return nil
	}

	if a == nil {
		return b
	}

	if b == nil {
		return a
	}

	switch a.(type) {
	case int:
		switch b.(type) {
		case int:
			if a.(int) > b.(int) {
				return a
			}
			if a.(int) == b.(int) {
				return nil
			}
			return b
		case float64:
			return b
		case string:
			return b
		}
	case float64:
		switch b.(type) {
		case int:
			return a
		case float64:
			if a.(float64) > b.(float64) {
				return a
			}
			if a.(float64) == b.(float64) {
				return nil
			}
			return b
		case string:
			return b
		}
	case string:
		switch b.(type) {
		case int:
			return a
		case float64:
			return a
		case string:
			if a.(string) > b.(string) {
				return a
			}
			if a.(string) == b.(string) {
				return nil
			}
			return b
		}
	}

	return a

}

