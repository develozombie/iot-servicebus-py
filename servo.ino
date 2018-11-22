//www.elegoo.com
//2016.12.08
#include <Servo.h>

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position

void setup() {
  Serial.begin(115200);
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
}

void loop() {
  if(Serial.available() > 0)
  {
    char data = Serial.read();
    char str[2];
    str[0] = data;
    str[1] = '\0';
    Serial.print(str);
    switch(str[0])
    {
      case 'a':
        myservo.write(90);
        delay(20);
        break;
      case 'i':
        myservo.write(0);
        delay(20);
        break;
      break;
      case 'd':
        myservo.write(180);
        delay(20);
        break;
      break;
    }
  }
}
