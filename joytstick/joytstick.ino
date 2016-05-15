int button = 7;
int x_axis = 0;
int y_axis = 1;

void setup(){
  pinMode(button,INPUT);
  digitalWrite(button,HIGH);
  Serial.begin(9600);
}
  
void loop(){
  Serial.print("X Axis ");
  Serial.print(analogRead(x_axis));
  Serial.print("\n");
  Serial.print("Y Axis ");
  Serial.print(analogRead(y_axis));
  Serial.print("\n");
  delay(500);
}
