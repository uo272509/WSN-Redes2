

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200); // set serial for usb printing
  
}

#define PIN_PHOTORESISTOR A0
int photoresistor = 0;

void readPhotoresistor() {
  photoresistor = analogRead(PIN_PHOTORESISTOR);
  Serial.printf("Photoresistor: %d\n", photoresistor);
  return;
}

void loop() {
  // put your main code here, to run repeatedly:
  readPhotoresistor();
  
  delay(1000);
  
  delay(1000);
}
