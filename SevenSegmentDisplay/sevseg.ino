#include "SevSeg.h"
SevSeg sevseg; 

void setup(){
    byte numDigits = 1;
    byte digitPins[] = {};
    byte segmentPins[] = {6, 5, 2, 3, 4, 7, 8, 9};
    bool resistorsOnSegments = true;

    byte hardwareConfig = COMMON_CATHODE; 
    sevseg.begin(hardwareConfig, numDigits, digitPins, segmentPins, resistorsOnSegments);
    sevseg.setBrightness(100);
}

void loop(){
        char p[] = "Dont Panic";

        for (int i = 0 ; i < 10; i++){
          char temp[1] = {""};
          temp[0] = p[i];
          sevseg.setChars(temp);
          delay(1000);
          sevseg.refreshDisplay(); 
        }
        
}
