    vector<string> result;

    if(planet1=="Mercury"||planet1=="Venus"||planet1=="Earth"||planet1=="Mars"||planet1=="Jupiter"||planet1=="Saturn"||planet1=="Uranus"||planet1=="Neptune"){
        if(planet2=="Mercury"||planet2=="Venus"||planet2=="Earth"||planet2=="Mars"||planet2=="Jupiter"||planet2=="Saturn"||planet2=="Uranus"||planet2=="Neptune"){
            if(planet1==planet2){
                result.push_back(planet1);
            }else{
                int index=0;
                for(int i=0;i<8;i++){
                    if(planet1=="Mercury"){
                        index=i;
                        break;
                    }
                    if(planet1=="Venus"){
                        index=i;
                        break;
                    }
                    if(planet1=="Earth"){
                        index=i;
                        break;
                    }
                    if(planet1=="Mars"){
                        index=i;
                        break;
                    }
                    if(planet1=="Jupiter"){
                        index=i;
                        break;
                    }
                    if(planet1=="Saturn"){
                        index=i;
                        break;
                    }
                    if(planet1=="Uranus"){
                        index=i;
                        break;
                    }
                    if(planet1=="Neptune"){
                        index=i;
                        break;
                    }
                }
                for(int i=index;i<8;i++){
                    if(planet2=="Mercury"){
                        index=i;
                        break;