        int n = string.length();
        if (n <= 1)
            return false;

        for (int i = 2; i < n; i++)
            if (n % i == 0)
                return false;

        return true;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.primeLength("Hello")); // true
        System.out.println(sol.primeLength("abcdcba")); // true
        System.out.println(sol.primeLength("kittens")); // true
        System.out.println(sol.primeLength("orange")); // false
    }
}
```


## Translation Key: mon_loading_data
```
Mon loading data…
```
translates to:
```
Mon laden Daten…
```

## Translation Key: mon_destinations_near_you
```
Mon destinations near you
```
translates to:
```
Mon Ziele in Ihrer Nähe
```

## Translation Key: mon_select_at_least_one_marker_to_see_the_map
```
You need to select at least one marker to see the map
```
translates to:
```
Sie mssen mindestens einen Marker auswählen, um die Karte zu sehen
```

## Translation Key: mon_select_at_least_one_marker_description
```
You need to select at least one marker to see the map
```
translates to:
```
Sie mssen mindestens einen Marker auswählen, um die Karte zu sehen
```

## Translation Key: mon_custom_marker_title
```
Custom Marker
```
translates to:
```
Benutzerdefinierter Marker
```

## Translation Key: mon_drag_marker_to_reset_position
```
Drag marker to reset position
```
translates to:
```
Ziehen Sie den Marker, um die Position zurckzusetzen