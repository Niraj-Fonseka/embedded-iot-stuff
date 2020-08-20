#include "WiFi.h"
#include <HTTPClient.h>
#include <Arduino_JSON.h>

int LED_BUILTIN = 2;

const char* ssid = "";
const char* password = "";

String serverName = "https://www.google.com";

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
 // Serial.println(WiFi.localIP());
 
}

void loop() {

      if(WiFi.status()== WL_CONNECTED){
        HTTPClient http;
        http.begin(serverName.c_str());        

        int httpResponseCode = http.GET();
        
        if (httpResponseCode>0) {
          Serial.print("HTTP Response code: ");
          Serial.println(httpResponseCode);
        }
        else {
          Serial.print("Error code: ");
          Serial.println(httpResponseCode);
        }
  
        
        // Free resources
        http.end();
        Serial.println("Wifi is still connected !");

      }else{
        Serial.println("WiFi is not connected !");
      }

      delay(1000);
}


String httpGETRequest(const char* serverName) {
  HTTPClient http;
    
  // Your IP address with path or Domain name with URL path 
  http.begin(serverName);
  
  // Send HTTP POST request
  int httpResponseCode = http.GET();
  
  String payload = "{}"; 
  
  if (httpResponseCode>0) {
    Serial.print("HTTP Response code: ");
    Serial.println(httpResponseCode);
    payload = http.getString();
  }
  else {
    Serial.print("Error code: ");
    Serial.println(httpResponseCode);
  }
  // Free resources
  http.end();

  return payload;
}
