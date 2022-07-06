volatile unsigned long time1=0, time2=0, time3=0;
volatile bool flag=false;
float duty, freq;
int pwmPin = 5;
int interruptPin = 2;

void first(void)
{
  noInterrupts();
  time1 = micros();
  if(time3!=0)flag=true;
  interrupts();
  attachInterrupt(digitalPinToInterrupt(interruptPin),second,FALLING);
}
void second(void)
{
  noInterrupts();
  time2 = micros();
  time3 = time1;
  interrupts();
  attachInterrupt(digitalPinToInterrupt(interruptPin),first,RISING);
}

void setup()
{
  Serial.begin(9600);
  pinMode(2,INPUT);
  pinMode(pwmPin,OUTPUT);
  analogWrite(pwmPin,240);
  attachInterrupt(digitalPinToInterrupt(interruptPin),first,RISING);
}
void loop()
{
  if(flag==true && time1!=time3 && time3!=0){
    noInterrupts();
    duty = ((time2-time3)*1.0)/(time1-time3);
    freq = 1000000.0/(time1-time3);
    
    
    flag=false;
    
    time3=0;
    interrupts();
    Serial.println(duty);
    Serial.println(freq);
  }
}
