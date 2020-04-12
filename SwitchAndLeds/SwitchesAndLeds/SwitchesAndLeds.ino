const int buttonOnePin = 8;
const int buttonTwoPin = 9; 
const int buttonThreePin = 10; 

const int ledOnePin = 2;
const int ledTwoPin = 3;
const int ledThreePin = 4;


int buttonOneState = 0;
int buttonTwoState = 0;
int buttonThreeState = 0;

bool buttonOneOn = false;
bool buttonTwoOn = false;
bool buttonThreeOn = false;

bool ledOn = false; 

void setup() {


  pinMode(ledOnePin,OUTPUT);
  pinMode(ledTwoPin,OUTPUT);
  pinMode(ledThreePin,OUTPUT);

  pinMode(buttonOnePin,INPUT);
  pinMode(buttonTwoPin,INPUT);
  pinMode(buttonThreePin,INPUT);

  Serial.begin(9600);



}

// the loop function runs over and over again forever
void loop() {
  buttonOneState = digitalRead(buttonOnePin);
  buttonTwoState = digitalRead(buttonTwoPin);
  buttonThreeState = digitalRead(buttonThreePin);

  if (buttonOneState == HIGH) {
      Serial.write("Button One Pressed .... \n");
      buttonOneOn = true;
      digitalWrite(ledOnePin, HIGH);
      digitalWrite(ledTwoPin, LOW);
      digitalWrite(ledThreePin, LOW);
  }

  if ( buttonTwoState == HIGH){
      Serial.write("Button Two Pressed .... \n");
      buttonTwoOn = true;
      digitalWrite(ledOnePin, LOW);
      digitalWrite(ledTwoPin, HIGH);
      digitalWrite(ledThreePin, LOW);

  }


  if (buttonThreeState == HIGH){
     Serial.write("Button Three Pressed .... \n");
     buttonThreeOn = true;
     digitalWrite(ledOnePin, LOW);
     digitalWrite(ledTwoPin, LOW);
     digitalWrite(ledThreePin, HIGH);
  }


}
