int pin = 7;
int count=0;
unsigned long duration,power;
void setup()
{
  Serial.begin(9600);
  pinMode(pin, INPUT);
  
}
void loop()
{
  duration = pulseIn(pin, LOW);
  if(duration>14000){
    power = duration - 14000;
  }
  else{
    power=0;
  }
  
  Serial.println(power/100);
  write_to_memory(power/100);
  delay(100);
}

void write_to_memory(int value){
  if(value<256){
    val1=value;
    val2=0;
    val3=0;
  }
  else if(value<65536){
    val1=value%256;
    val2=value/256;
    val3=0;
  }
  else if(value<16777216){
    val1=value%256;
    val2=value%65536;
    val3=value/65536;
  }
  EEPROM.write(0,val1);
  EEPROM.write(1,val2);
  EEPROM.write(2,val3);
}