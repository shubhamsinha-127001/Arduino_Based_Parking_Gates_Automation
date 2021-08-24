#include <LiquidCrystal.h>
#include <Servo.h>

Servo servo;

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

//to rective the message from the python visuaal studio
int incomingByte = 1 ;

void setup() {
  servo.attach(8);
  servo.write(0);
  delay(2000);
  //for servo
  lcd.begin(16, 2);
  //lcd.print("hello, world!");
  Serial.begin(9600);
  pinMode(8, OUTPUT);
  pinMode(11, OUTPUT);
}

void loop() {
  int flag = 0;
  //if (Serial.available() > 0) {
    //incomingByte = Serial.readStringUntil('\n');
    if (incomingByte == 1) {
      if (flag == 0) {
        lcd.clear();
        lcd.print("Authorized");
        flag++;
      }
      servo.write(190);
      delay(1000);
      servo.write(0);
      delay(1000);
      //for servo
      digitalWrite(11, HIGH);
      delay(500);
      digitalWrite(11, LOW);
      delay(50);
      Serial.write("Led on for authorized");
    }

    else if (incomingByte == 0) {
      lcd.clear();
      lcd.print("NON Authorized");
      digitalWrite(8, HIGH);
      delay(500);
      digitalWrite(8, LOW);
      delay(50);
      Serial.write("Led on for non authorized");
    }

    else {
      Serial.write("invald input from teh pythong dile is recived");
    }
  //}
}