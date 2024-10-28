    vector<string> order;
    if ((planet1=="Mercury")||(planet1=="Venus")||(planet1=="Earth")||(planet1=="Mars")||(planet1=="Jupiter")||(planet1=="Saturn")||(planet1=="Uranus")||(planet1=="Neptune"))
    {
        if ((planet2=="Mercury")||(planet2=="Venus")||(planet2=="Earth")||(planet2=="Mars")||(planet2=="Jupiter")||(planet2=="Saturn")||(planet2=="Uranus")||(planet2=="Neptune"))
        {
            if (planet1=="Mercury")
            {
                if (planet2=="Mercury")
                {
                    order={"Mercury"};
                }
                if (planet2=="Venus")
                {
                    order={"Mercury","Venus"};
                }
                if (planet2=="Earth")
                {
                    order={"Mercury","Venus","Earth"};
                }
                if (planet2=="Mars")
                {
                    order={"Mercury","Venus","Earth","Mars"};
                }
                if (planet2=="Jupiter")
                {
                    order={"Mercury","Venus","Earth","Mars","Jupiter"};
                }
                if (planet2=="Saturn")
                {
                    order={"Mercury","Venus","Earth","Mars","Jupiter","Saturn"};
                }
                if (planet2=="Uranus")
                {
                    order={"Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus"};
                }
                if (planet2=="Neptune")
                {
                    order={"Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Ne