int readPIN= A3;
int v2;
int delayTime = 1000;


float fromBin2V(int v){
  return (5.0/1023)*v;
}


void setup() {
  pinMode(readPIN, INPUT);
  Serial.begin(9600);

}

void loop() {
  v2 = analogRead(readPIN);
  Serial.println(fromBin2V(v2));
  delay(delayTime);
}
