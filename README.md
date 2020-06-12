# **Robot "Getafix"**
My Tiny AI Robot that features edge computation, real-time object recognition using Raspberry pi 4B, Coral Edge TPU and Arduino.

## **Overview:**
Introducing one of my favorite pet projects that began with the humorous idea challenge, why not train a robot analog to a dog to fetch us a beer. Thus, the robot should be capable of detecting and recognizing beer bottles which is our object of interest, navigate to the bottle location and, be able to pick the bottle using a robot arm, then detect the person, locate, and carry it the person. This will need a combination of real-time object recognition using custom trained model, appropriate robot locomotion, navigation, robotic arm, power and the like. 

I called the first iteration robot that provides basic capabilities Getafix after the village druid character in [“The Adventures of Asterix”](https://en.wikipedia.org/wiki/Asterix). I am sharing the how’s and the design details in order to inspire interested roboteers and students with the application of Artificial Intelligence (AI or Tiny AI), real-time object recognition on edge computation using Raspberry Pi 4B, Google Coral Edge TPU and Arduino electronics. More importantly, the robot provides a combination of microprocessor, microcontroller, AI accelerator that is an Application Specific Integrated Circuit (ASIC) and peripheral electronics, that potentially can be used to assist disabled users or in industries to automatically identify, target and interact with any object, furthermore, it can be used as a development and testing bed for further innovative application of AI and robotics projects. can be used as a development and testing bed for further innovative application of AI and robotics projects. 
![](media/robopic3.jpg)

## **Robot Capabilities:**
* Locomotion, continuous tracks driven by two (x2) DC Motor with metal gearbox.
* Detect object of interest such as beer bottles, cans and cups from live camera live feed using deep learning Object-Recognition.
* Navigate to the object and pickup object and navigate back to starting point.
* Measure object distance using ultrasonic sensors.
* Gripper clamp robotic arm with two degrees of freedom.

## **Architecture/ How it all Connects:**
![](media/roboarch1.jpg)

<table style="width: 676px;" border="1">
<tbody>
<tr>
<td style="width: 618.2px;" colspan="2">
<p><strong>Components and Specification:</strong></p>
</td>
<td style="width: 55.8px;">
<p><strong>Cost</strong></p>
</td>
</tr>
<tr>
<td style="width: 16px;">
<p>1</p>
</td>
<td style="width: 602.2px;">
<p>Robot tank aluminum alloy chassis (SR14-B) with continuous tracks and drive two DC motor 33GB-520 DC6-12V 350 RPM</p>
</td>
<td style="width: 55.8px;">
<p>&nbsp;$33</p>
</td>
</tr>
<tr>
<td style="width: 16px;">
<p>2</p>
</td>
<td style="width: 602.2px;">
<p>CanaKit Raspberry Pi 4B 4GBRAM and 32GBmicroSD Starter Kit</p>
</td>
<td style="width: 55.8px;">
<p>&nbsp;$100</p>
</td>
</tr>
<tr>
<td style="width: 16px;">
<p>3</p>
</td>
<td style="width: 602.2px;">
<p>Camera Day &amp; Night Vision, IR-Cut Video Camera 1080p HD Webcam 5MP OV5647 Sensor for Raspberry Pi</p>
</td>
<td style="width: 55.8px;">
<p>&nbsp;$29</p>
</td>
</tr>
<tr>
<td style="width: 16px;">
<p>4</p>
</td>
<td style="width: 602.2px;">
<p>Heatsink Kit (x20pcs) Aluminum + Copper + 3M 8810 Thermal Conductive Adhesive Tape for Cooling Pi and Arduino electronics</p>
</td>
<td style="width: 55.8px;">
<p>&nbsp;$8</p>
</td>
</tr>
<tr>
<td style="width: 16px;">
<p>5</p>
</td>
<td style="width: 602.2px;">
<p>Cooling fan (included in Raspberry Pi Starter Kit)</p>
</td>
<td style="width: 55.8px;">
<p>-</p>
</td>
</tr>
<tr>
<td style="width: 16px;">
<p>6</p>
</td>
<td style="width: 602.2px;">
<p>Full Function Motor HAT, Robot Expansion Board Supports Stepper/Motor/Servo/IR Remote for Raspberry Pi 4B</p>
</td>
<td style="width: 55.8px;">
<p>&nbsp;$28</p>
</td>
</tr>
<tr>
<td style="width: 16px;">
<p>7</p>
</td>
<td style="width: 602.2px;">
<p>Coral USB Accelerator</p>
</td>
<td style="width: 55.8px;">
<p>&nbsp;$75</p>
</td>
</tr>
<tr>
<td style="width: 16px;">
<p>8</p>
</td>
<td style="width: 602.2px;">
<p>Arduino UNO R3 Complete Starter Kit</p>
</td>
<td style="width: 55.8px;">
<p>&nbsp;$40</p>
</td>
</tr>
<tr>
<td style="width: 16px;">
<p>9</p>
</td>
<td style="width: 602.2px;">
<p>High Speed SG5010 Digital Servo Motor (38g) for Arduino UNO (4pcs)</p>
</td>
<td style="width: 55.8px;">
<p>&nbsp;$24</p>
</td>
</tr>
<tr>
<td style="width: 16px;">
<p>10</p>
</td>
<td style="width: 602.2px;">
<p>Stepper motor 28byj-48 (include in the Arduino kit)</p>
</td>
<td style="width: 55.8px;">
<p>-</p>
</td>
</tr>
<tr>
<td style="width: 16px;">
<p>11</p>
</td>
<td style="width: 602.2px;">
<p>Adafruit Motor/Stepper/Servo Shield for Arduino v2.3 Kit</p>
</td>
<td style="width: 55.8px;">
<p>&nbsp;$19</p>
</td>
</tr>
<tr>
<td style="width: 16px;">
<p>12</p>
</td>
<td style="width: 602.2px;">
<p>Ultrasonic Sensor HC-SR04 (include in the Arduino kit)</p>
</td>
<td style="width: 55.8px;">&nbsp;</td>
</tr>
<tr>
<td style="width: 16px;">
<p>13</p>
</td>
<td style="width: 602.2px;">
<p>Power Supply Module 2.6V-5.5V 3A to 5V 2A Mini DC-DC Battery Booster USB Mobile Step-up Power Supply with Battery Indicator</p>
</td>
<td style="width: 55.8px;">
<p>&nbsp;$8</p>
</td>
</tr>
<tr>
<td style="width: 16px;">
<p>14</p>
</td>
<td style="width: 602.2px;">
<p>Adafruit PowerBoost 1000C Battery boost and Charger</p>
</td>
<td style="width: 55.8px;">
<p>&nbsp;$23</p>
</td>
</tr>
<tr>
<td style="width: 16px;">
<p>15</p>
</td>
<td style="width: 602.2px;">
<p>Charger PCB BMS Protection Board-18650 for Li-ion Lithium Battery Cell 1S 3.7V 4A (5pcs)</p>
</td>
<td style="width: 55.8px;">
<p>&nbsp;$8</p>
</td>
</tr>
<tr>
<td style="width: 16px;">
<p>16</p>
</td>
<td style="width: 602.2px;">
<p>Six (6P, 20100mAH total) LG MJ1 18650 3500mAh 3.6V Battery, (6pcs)</p>
</td>
<td style="width: 55.8px;">
<p>&nbsp;$38</p>
</td>
</tr>
<tr>
<td style="width: 16px;">
<p>17</p>
</td>
<td style="width: 602.2px;">
<p>USB-A to USB-C Cable 90 Degree Plug USB 3.0 Cable 0.8ft/0.25m</p>
</td>
<td style="width: 55.8px;">
<p>&nbsp;$8</p>
</td>
</tr>
<tr>
<td style="width: 16px;">
<p>18</p>
</td>
<td style="width: 602.2px;">
<p>USB-A to USB-B Cable 90 Degree Plug USB 2.0 Cable 0.5ft</p>
</td>
<td style="width: 55.8px;">
<p>&nbsp;$6</p>
</td>
</tr>
<tr>
<td style="width: 16px;">
<p>19</p>
</td>
<td style="width: 602.2px;">
<p>Angled USB C Cable Extension Gold Plated 90 Degree Type C to USB 3.0 Left Angle Male Adapter Data Sync Charging USB-C Cord (90°Type C-USB 3.0 A Left)</p>
</td>
<td style="width: 55.8px;">
<p>&nbsp;$9</p>
</td>
</tr>
<tr>
<td style="width: 16px;">
<p>20</p>
</td>
<td style="width: 602.2px;">
<p>One each 1KOhm and 2KOhm resistors (include in the Arduino kit)</p>
</td>
<td style="width: 55.8px;">
<p>-</p>
</td>
</tr>
<tr>
<td style="width: 16px;">
<p>21</p>
</td>
<td style="width: 602.2px;">
<p>104nF (x2 pcs) and 47nF (x4pcs) Ceramic Disc Capacitors (include in the Arduino kit)</p>
</td>
<td style="width: 55.8px;">
<p>-</p>
</td>
</tr>
<tr>
<td style="width: 16px;">
<p>22</p>
</td>
<td style="width: 602.2px;">
<p>Toggle switch DPDT</p>
</td>
<td style="width: 55.8px;">
<p>&nbsp;$10</p>
</td>
</tr>
<tr>
<td style="width: 16px;">
<p>23</p>
</td>
<td style="width: 602.2px;">
<p>0.7 and 0.5mm screws, nuts and washers set</p>
</td>
<td style="width: 55.8px;">
<p>&nbsp;$16</p>
</td>
</tr>
<tr>
<td style="width: 16px;">
<p>24</p>
</td>
<td style="width: 602.2px;">
<p>Motor Coupler 5mm with two screws and preferably flex fastener</p>
</td>
<td style="width: 55.8px;">
<p>&nbsp;$16</p>
</td>
</tr>
<tr>
<td style="width: 16px;">
<p>25</p>
</td>
<td style="width: 602.2px;">
<p>5mm aluminum tube</p>
</td>
<td style="width: 55.8px;">
<p>&nbsp;$5</p>
</td>
</tr>
<tr>
<td style="width: 16px;">
<p>26</p>
</td>
<td style="width: 602.2px;">
<p>PLA 1.75mm 3D printer filament</p>
</td>
<td style="width: 55.8px;">
<p>&nbsp;$20</p>
</td>
</tr>
<tr>
<td style="width: 16px;">
<p>27</p>
</td>
<td style="width: 602.2px;">
<p>3D printed stepper motor 28byj-48 mount support</p>
<p>(<a href="https://www.thingiverse.com/thing:3020621">https://www.thingiverse.com/thing:3020621</a>)</p>
</td>
<td style="width: 55.8px;">
<p>-</p>
</td>
</tr>
<tr>
<td style="width: 16px;">
<p>28</p>
</td>
<td style="width: 602.2px;">
<p>3D printed gripper clamp robot arm</p>
<p>(<a href="https://www.thingiverse.com/thing:2195839">https://www.thingiverse.com/thing:2195839</a>)</p>
</td>
<td style="width: 55.8px;">
<p>-</p>
</td>
</tr>
<tr>
<td style="width: 16px;">
<p>29</p>
</td>
<td style="width: 602.2px;">
<p>3D printed camera and ultrasound mount support</p>
<p>(<a href="https://www.thingiverse.com/thing:3476484">https://www.thingiverse.com/thing:3476484</a>)</p>
</td>
<td style="width: 55.8px;">
<p>-</p>
</td>
</tr>
<tr>
<td style="width: 16px;">&nbsp;</td>
<td style="width: 602.2px;">
<p>Total</p>
</td>
<td style="width: 55.8px;">
<p>&nbsp;$523</p>
</td>
</tr>
</tbody>
</table>

## **Essential items and tools needed for the build:**
* Screw driver set
* Power drill
* 3D printer (I used my Prusa Mendel Iteration-2 (RepRap)
* Small color monitor with HDMI port, keyboard and mouse
* Vernier Calipers (preferably digital)
* Soldering Iron and Tin/Lead with rosin flux core
* Needle nose pliers with cutter
* Digital Multimeter
* MS VS Code
* MS VOTT
* Arduino Software (IDE)

## **Lesson Learned and Pain Points:**
* Stacking the boards vertically is the best option to use the space in the robot platform. 
* Use appropriate heat sinks and cooling fan to ensure efficient performance of the components.
* Use screws and bolts and zip locks as much as possible and minimize the use of glue when building your robot.
* Use snubber and protection circuits to avoid unnecessary noise interference or prevent failure of components. 
* Measure accurately and edit 3D model files as necessary before printing 3D objects.
* Labeling images is time taking and laborious.
* Update your Linux build and libraries including the Pi firmware.

## **Training the Object Detection Model:**
Data Collection; for this project, I used Google and Bing image search in order to get pictures of my favorite beer bottles and cans. Google Chrome extensions makes it easier to download and organize images, such as “Fatkun Batch Download Image” and “Image Downloader Continued”. 
Augmenting and Transforming Images, is an important technique to further enhance the training image data by performing basic transformation such as flipping/rotating, grayscale, blurring and injecting random noise into the images. I used this python code to perform the necessary image augmentation <will add link>.
Labeling the Images; Microsoft Visual Object Tagging Tool is one of the great tools that can be used to label images. Alternatively, Google Cloud AutoML Vision services for Custom Machine Learning Models can be used after uploading the images to Google Cloud Storage.  I used eight lables that include cups, water bottle and beers (jucifer, lagunita ipa, corona, guinness, heineken).I have uploaded sample dataset I used in training the custom model. <will add link>.

Training Model;  An easier way to perform custom object detection model training is to do transfer training using the MobileNet SDD model as detailed here https://coral.ai/docs/edgetpu/retrain-detection/#requirements. Alternatively, Google Cloud AutoML Vision services can be used to train TensorFlow lite models that works on the Coral edge TPU. 
Training Accuracy;
![](media/model_accuracy.jpg)
In addition to the custom object detection model this robotics project uses a pre-trained model on the COCO dataset to detect person in order to deliver the object of interest.

## **The Coding Fun:**
The basic concept is as outlined on the diagram below, first initialize by setting parameters that includes  the use of the custom object detection model to perform inference on the image frames from the camera, to detect the object of interest and obtain the corresponding  bounding box and object label, check the label of the object detected matches the object of interest that is for this robot version, is a specific type of beer say “Guinness”. If matched, calculate the dynamic horizontal target zone and the centroid of the detected object. Then determine if the object is to the left or right of the central horizontal target zone and, decide to actuate the robot main locomotion motors according to the direction of the target zone and distance of the object measured via the ultrasonic sensors.
The dynamic horizontal target zone is made out of two dynamic vertical lines that is a function of how far the object is from the robot, the target zone is wider for far detections and gets narrower as the object/robot gets closer. This targeting method makes it easier to align the robot from far and move it in place to pick the object using the robot arm. 

![](media/getafix_robot_main_code_flow.jpg)

The object is picked when the object is within the horizontal target zone lines and the detected object distance is below the set minimum or the object detection bounding box frame width has reached the set maximum value. Then the robot is close enough to actuate the robot arm and pick up the object of interest. Once the object is picked the robot main code switches the object detection inference model to the pre-trained model and initializes the necessary parameters and, starts looking for the second object of interest that is a person in the room. And, similarly targets and moves to the person and drops the object close to the person. 

In case the robot could not detect or loses sight the objects of interest the robot main code executes a search maneuver which I call the “Rooster Move”, by moving forward and back and rotating side to side until it detects and locks on the object.
As shown in the above section “how things are connected” the robot arm is driven off the Arduino and SHIELD boards linked via serial USB cable to the Raspberry Pi. The robot locomotion is controlled by the Raspberry Pi HAT. One can control all motors and servos from the Arduino or the Pi depending on what you want to achieve or experiment. The robot main code communicates to the Arduino sketch code via serial interface and issues a set of commands defined in the sketch code 
<will add link to code> 

## **Future Upgrades:**
* Adapt the use of Robotic Operating System (ROS).
* Use wide angle view camera lens with fisheye correction.
* Use Accelerometer and Gyroscope sensor to identify the exact orientation and motion of the robot relative to the detected object of interest.
* Add infrared based distance sensor to increase accurately of distance measurement. 
* Grip sensor on the robot arm clamp.
* Current sink sensing to identify load on the servo’s and motor drives.
* Perfect the “Rooster Move” and add automatic obstacle avoidance system.
* Voice recognition to select object of interest or issue a voice command to the robot.


## **References:**
++++++++++UNDER CONSTRUCTION++++++++++

