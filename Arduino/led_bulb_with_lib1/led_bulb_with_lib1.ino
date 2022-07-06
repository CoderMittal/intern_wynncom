#include <IRremote.h>

const byte IR_RECEIVE_PIN = 4;
int redPin = 12;
int greenPin = 8;
int bluePin = 7;

void setup()
{
  Serial.begin(9600);
  IrReceiver.begin(IR_RECEIVE_PIN, ENABLE_LED_FEEDBACK);
  pinMode(redPin,OUTPUT);
  pinMode(greenPin,OUTPUT);
  pinMode(bluePin,OUTPUT);
}

void loop()
{
   if (IrReceiver.decode())
   {
     int data = IrReceiver.decodedIRData.command;
     Serial.println(data);
     if(data==16){
       digitalWrite(redPin,HIGH);
       delay(500);
       digitalWrite(redPin,LOW);
     }
     else if(data==17){
       digitalWrite(greenPin,HIGH);
       delay(500);
       digitalWrite(greenPin,LOW);
     }
     else if(data==18){
       digitalWrite(bluePin,HIGH);
       delay(500);
       digitalWrite(bluePin,LOW);
     }
     else{
       digitalWrite(bluePin,HIGH);
       delay(500);
       digitalWrite(bluePin,LOW);
     }
     IrReceiver.resume();
   }
}