#include "WiFi.h"

int LED_BUILTIN = 2;

const char* ssid = "yourSSID";
const char* password = "yourSSIDpwd";


void setup() {
  pinMode(LED_BUILTIN, OUTPUT);

  Serial.begin(9600);
  WiFi.begin(ssid, password);

   
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("Connecting to WiFi..");
  }

  digitalWrite(LED_BUILTIN, HIGH);

  Serial.println("Connected to the WiFi network");
 
}

void loop() {
}
