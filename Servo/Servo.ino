
#include <Servo.h>

Servo myservo;  
int pos = 0;   
int trigpin = 12;
int  echopin = 11;
int  redLed = 7;
int  greenLed = 6;
int sounds = 4;
void setup() {
  Serial.begin(9600);
  myservo.attach(9); 
  pinMode(trigpin,OUTPUT);
  pinMode(echopin,INPUT);
  pinMode(redLed,OUTPUT);
  pinMode(greenLed,OUTPUT);
  pinMode(sounds,OUTPUT);
}

void loop() {
  //for testing purposes GIT
  int duration , distance;
  digitalWrite(greenLed,HIGH);
  for (pos = 0; pos <= 180; pos += 1) { 
    myservo.write(pos); 
    digitalWrite(trigpin,HIGH);
    delayMicroseconds(1000);
    digitalWrite(trigpin,LOW);
    duration = pulseIn(echopin,HIGH);
    distance = (duration/2) / 29.1;
    if(distance <= 10){
      digitalWrite(greenLed,LOW);
      digitalWrite(redLed,HIGH);
      digitalWrite(sounds,HIGH);
      Serial.println("WARNING TOO CLOSE");
      tone(sounds,988,1000);
     // delay(50);
      digitalWrite(redLed,LOW);
      digitalWrite(sounds,LOW);
    }else{
      digitalWrite(greenLed,HIGH);
      digitalWrite(redLed,LOW);
    }
    Serial.print(distance);
    Serial.println("cm");
    delay(15);                      
  }
  for (pos = 180; pos >= 0; pos -= 1) { 
    myservo.write(pos);  
    digitalWrite(trigpin,HIGH);
    delayMicroseconds(1000);
    digitalWrite(trigpin,LOW);
    duration = pulseIn(echopin,HIGH);
    distance = (duration/2) / 29.1;
    if(distance <= 10){
      digitalWrite(greenLed,LOW);
      digitalWrite(redLed,HIGH);
      digitalWrite(sounds,HIGH);
      Serial.println("WARNING TOO CLOSE");
      tone(sounds,988,1000);
     // delay(50);
      digitalWrite(redLed,LOW);
      digitalWrite(sounds,LOW);
    }else{
      digitalWrite(greenLed,HIGH);
      digitalWrite(redLed,LOW);
    }
    Serial.print(distance);
    Serial.println("cm");
    delay(15);
  }
  
}
