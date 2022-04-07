int fstBit = 6;
int secBit = 7;
int thrdBit = 8;
int fourthBit = 9;


void setup() {
  pinMode(fstBit, OUTPUT);
  pinMode(secBit, OUTPUT);
  pinMode(thrdBit, OUTPUT);
  pinMode(fourthBit, OUTPUT);
}

void binBlink(int fBlink, int sBlink, int thrdBlink, int fourBlink){
  digitalWrite(fstBit, fBlink);
  digitalWrite(secBit, sBlink);
  digitalWrite(thrdBit, thrdBlink);
  digitalWrite(fourthBit, fourBlink);
  delay(1000);
}


void loop() {
  for (int k=0; k<16; k++){
    int i = k;
    int fBlink = i%2;
    i/=2;
    int sBlink = i%2;
    i/=2;
    int thrdBlink = i%2;
    i/=2;
    int fourBlink = i%2;
    binBlink(fBlink, sBlink, thrdBlink, fourBlink);
  }
}
