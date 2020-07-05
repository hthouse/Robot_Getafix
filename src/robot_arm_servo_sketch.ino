/* 
  Copyright 2020 Hiwot T. Sidelil, All rights reserved.
  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at
  
      https://www.apache.org/licenses/LICENSE-2.0 
      
  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS"ssssssss9 BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
*/


#include <Wire.h>
//#include <Adafruit_MotorShield.h>
#include <Servo.h> 

Servo clamp_servo;  // create servo object to control a servo  
Servo v_arm_servo;
Servo h_arm_servo;

String move_arm = "";
String ser_rx_data;

void setup() {
  Serial.begin(9600);           // set up Serial library at 9600 bps
  Serial.println("robot arm init!");
  
  clamp_servo.attach(11);  // attach the servo on pin 9,10,11 to the servo object 
  v_arm_servo.attach(9);
  h_arm_servo.attach(10);

  Serial.println("clamp_servo");
  Serial.println(clamp_servo.read());
  Serial.println("v_arm_servo");
  Serial.println(v_arm_servo.read());
  Serial.println("h_arm_servo");
  Serial.println(h_arm_servo.read());
 
  h_arm_servo.write(120); //120-center-default 20-left
  v_arm_servo.write(135); //135-drop-default, 200-lift
  clamp_servo.write(0); //0-open-default, 200-closed
  //Serial.println(clamp_servo.read()); // test servo position
  //Serial.println(v_arm_servo.read());
  //Serial.println(h_arm_servo.read());

  delay(100);
}

void loop() {
  if(Serial.available()){
        ser_rx_data = Serial.readStringUntil('\n');
        Serial.println("received command: " + ser_rx_data);
    }
  move_arm= ser_rx_data;
  ser_rx_data ="";
   if (move_arm == "open_arm") {
      clamp_servo.write(0);       // sets the servo to open clamp arm position  
      Serial.println(clamp_servo.read());
      move_arm ="";
      delay(15);
      }
   else if (move_arm == "close_arm") {
      clamp_servo.write(130);       // sets the servo to closed arm position
      Serial.println(clamp_servo.read());
      move_arm ="";
      delay(15);
      }
   else if (move_arm == "drop_arm") {
      v_arm_servo.write(135);       // sets the servo arm position to drop lower 
      Serial.println(v_arm_servo.read());
      move_arm ="";
      delay(15);
      }
   else if (move_arm == "lift_arm") {
      v_arm_servo.write(200);       // sets the servo position according to the scaled value 
      Serial.println(v_arm_servo.read());
      move_arm ="";
      delay(15);
      }
   else if (move_arm == "turn_arm") {
      h_arm_servo.write(20);       // sets the servo position according to the scaled value 
      Serial.println(h_arm_servo.read());
      move_arm ="";
      delay(15);
      }
   else if (move_arm == "center_arm") {
      h_arm_servo.write(120);       // sets the servo position according to the scaled value 
      Serial.println(h_arm_servo.read());
      move_arm ="";
      delay(15);
      }  
   else if (move_arm == "release_servo") {
       clamp_servo.detach();
       h_arm_servo.detach();
       v_arm_servo.detach();
       move_arm ="";
       }

}
