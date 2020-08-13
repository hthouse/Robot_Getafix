# Copyright 2020 Hiwot T. Sidelil, All rights reserved.

# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from edgetpu.detection.engine import DetectionEngine
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import numpy as np
import time
import io
import picamera
from picamera import Color
import RPi.GPIO as GPIO
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
import atexit
import serial
import sys
import autofocus_lib
import cv2

def distance():
    GPIO.setmode(GPIO.BCM)
    #set GPIO Pins
    GPIO_TRIGGER = 17
    GPIO_ECHO = 27
     
    #set GPIO direction (IN / OUT)
    GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
    GPIO.setup(GPIO_ECHO, GPIO.IN)
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s and 13503.0 in/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 13514.17) / 2
    distance = round(distance,1)
    return distance

def robo_arm(action):
    #initialize serial port
    ser=serial.Serial("/dev/ttyACM0",9600,timeout=5)  #change ACM number as found from ls /dev/tty/ACM*
    ser.baudrate=9600
#     ser.flushInput()
#     ser.flushOutput()
    time.sleep(5)
    if action == "pick":
        arm_orders=["close_arm\n","lift_arm\n","turn_arm\n"]
    elif action == "drop":
        arm_orders=["center_arm\n","drop_arm\n","open_arm\n"]
    for command in arm_orders:
        myorder=str.encode(command)
        ser.write(myorder)
        print(myorder)
        time.sleep(5)
    #ser.flushInput()
    #ser.flushOutput()

def turnOffMotors():
    # recommended for auto-disabling motors on shutdown!
    mh.getMotor(1).run(Raspi_MotorHAT.RELEASE)
    mh.getMotor(2).run(Raspi_MotorHAT.RELEASE)
    mh.getMotor(3).run(Raspi_MotorHAT.RELEASE)
    mh.getMotor(4).run(Raspi_MotorHAT.RELEASE)
    
def moto_move(movement,angle,dist):
    ##DC motor 
    mh = Raspi_MotorHAT(addr=0x6f)
    myMotor_left = mh.getMotor(1)
    myMotor_right = mh.getMotor(2)
    atexit.register(turnOffMotors)
    
    turn_steps = int(angle * 250/90)
    move = int (dist * 100/6.7)
    spd=90
    if movement=="backward":
        print ("Backward! ")
        myMotor_left.run(Raspi_MotorHAT.FORWARD)
        myMotor_right.run(Raspi_MotorHAT.FORWARD)
        myMotor_left.setSpeed(spd)
        myMotor_right.setSpeed(spd)
        for j in range(0,move,1):
            time.sleep(0.01)
        #print ("Release/Stop")
        myMotor_left.run(Raspi_MotorHAT.RELEASE)
        myMotor_right.run(Raspi_MotorHAT.RELEASE)
        time.sleep(0.5)
#         for i in range(0,255,1):
#             myMotor_left.setSpeed(i)
#             myMotor_right.setSpeed(i)
#             time.sleep(0.01)
    elif movement=="forward":
        print ("Forward! ")
        myMotor_left.run(Raspi_MotorHAT.BACKWARD)
        myMotor_right.run(Raspi_MotorHAT.BACKWARD)
        myMotor_left.setSpeed(spd)
        myMotor_right.setSpeed(spd)
        for j in range(0,move,1):
            time.sleep(0.01)
        #print ("Release/Stop")
        myMotor_left.run(Raspi_MotorHAT.RELEASE)
        myMotor_right.run(Raspi_MotorHAT.RELEASE)
        time.sleep(0.5)
#         for i in range(0,255,1):
#             myMotor_left.setSpeed(i)
#             myMotor_right.setSpeed(i)
#             time.sleep(0.01)  
    elif movement=="left":
        print ("Turn Left! ")
        myMotor_left.run(Raspi_MotorHAT.BACKWARD)
        myMotor_left.setSpeed(230)
        myMotor_right.run(Raspi_MotorHAT.FORWARD)
        myMotor_right.setSpeed(30)
        for j in range(0,turn_steps,1):
            time.sleep(0.01)
        #print ("Release/Stop")
        myMotor_left.run(Raspi_MotorHAT.RELEASE)
        myMotor_right.run(Raspi_MotorHAT.RELEASE)
        time.sleep(0.5)
#             for i in range(5,100,1):
#                 myMotor_right.setSpeed(i)
#                 time.sleep(0.01)
    elif movement=="right":
        print ("Turn Right! ")
        myMotor_right.run(Raspi_MotorHAT.BACKWARD)
        myMotor_right.setSpeed(230)
        myMotor_left.run(Raspi_MotorHAT.FORWARD)
        myMotor_left.setSpeed(30)
        for j in range(0,turn_steps,1):
            time.sleep(0.01)
        #print ("Release/Stop")
        myMotor_left.run(Raspi_MotorHAT.RELEASE)
        myMotor_right.run(Raspi_MotorHAT.RELEASE)
        time.sleep(0.5)
#         for i in range(0,200,1):
#             myMotor_left.setSpeed(i)
#             time.sleep(0.01)      
    elif movement=="release":
        #print ("Release/Stop")
        myMotor_left.run(Raspi_MotorHAT.RELEASE)
        myMotor_right.run(Raspi_MotorHAT.RELEASE)
        time.sleep(1.0)  

def _monkey_patch_picamera():
    # https://github.com/waveform80/picamera/issues/383
    original_send_buffer = picamera.mmalobj.MMALPortPool.send_buffer

    def silent_send_buffer(zelf, *args, **kwargs):
        try:
            original_send_buffer(zelf, *args, **kwargs)
        except picamera.exc.PiCameraMMALError as error:
            if error.status != 14:
                raise error
    picamera.mmalobj.MMALPortPool.send_buffer = silent_send_buffer

def _read_label_file(file_path):
    # Read labels.txt file provided by the model
    with open(file_path, 'r', encoding="utf-8") as f:
        lines = f.readlines()
    ret = {}
    for line in lines:
        pair = line.strip().split(maxsplit=1)
        ret[int(pair[0])] = pair[1].strip()
    return ret

def variance_of_laplacian(image):
    # compute the Laplacian of the image and then return the focus
    # measure, which is simply the variance of the Laplacian
    return cv2.Laplacian(image, cv2.CV_64F).var()

# Main loop
def main():
    #model_filename = "beer2_model_edgetpu.tflite"
    model_filename = "model_1.tflite"
    #label_filename = "beer2_dict.txt"
    label_filename = 'model_low_model-dict.txt'
    
    model_filename_2 = "mobilenet_ssd_v2_coco_quant_postprocess_edgetpu.tflite"
    label_filename_2 = "coco_labels.txt"
    
    label_of_interest_1 = "jucifer_c"
    label_of_interest_2 = "person"
    move_order="look"
    line_1=240
    line_2=400
    
    engine = DetectionEngine(model_filename)
    labels = _read_label_file(label_filename)
    
    engine_2 = DetectionEngine(model_filename_2)
    labels_2 = _read_label_file(label_filename_2)
    
    obj_prcnt = 0.3
    arm_action = "pick"
    CAMERA_WIDTH = 1280 #640 #1920 #1280
    CAMERA_HEIGHT = 720  #480 #1080 #720 

    fnt = ImageFont.load_default()
    #fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuMathTeXGyre.ttf",9)
    
    search_maneuver_counter = 0
    search_maneuver = [{"mvnt1":"forward", "angle":0, "dist":10},\
                        {"mvnt1":"backward", "angle":0, "dist":10},\
                        {"mvnt1":"left", "angle":45, "dist":0},\
                        {"mvnt1":"right", "angle":90, "dist":0} ]
    robo_arm("drop") #position arm open, centered and lowered
    # To view preview on VNC,
    # https://raspberrypi.stackexchange.com/a/74390
    with picamera.PiCamera() as camera:
        _monkey_patch_picamera()
        camera.resolution = (CAMERA_WIDTH, CAMERA_HEIGHT)
        camera.framerate = 15 #15fps
        camera.rotation = 180 #rotate frame 180 degree
        camera.annotate_foreground = Color("black")
        camera.annotate_background = Color('#7fff00')

        _, width, height, channels = engine.get_input_tensor_shape()
        print("{}, {}".format(width, height))
        overlay_renderer = None
        camera.video_stabilization = True
        camera.exposure_mode = 'night'
        camera.awb_mode = 'shade'
        camera.contrast = 10
        camera.brightness = 60
        camera.led = True
        #camera.exposure_compensation = 10
        camera.start_preview(alpha=220, fullscreen=True)
        #camera.start_preview(alpha=128, fullscreen=False, window=(0, 0, 640, 480))
        
        try:
            stream = io.BytesIO()
            for foo in camera.capture_continuous(stream,
                                                 format='rgb', use_video_port=True):
                # Make Image object from camera stream
                stream.truncate()
                stream.seek(0)
                input = np.frombuffer(stream.getvalue(), dtype=np.uint8)
                input = input.reshape((CAMERA_HEIGHT, CAMERA_WIDTH, 3))
                image = Image.fromarray(input)
                autofocus_lib.focusing(10)
#                 gray = cv2.cvtColor(input, cv2.COLOR_BGR2GRAY)
#                 vl= variance_of_laplacian(gray)
#                 print(vl)
                # image.save("out.jpg")

                # Make overlay image plane
                img = Image.new('RGBA',
                                (CAMERA_WIDTH, CAMERA_HEIGHT),
                                (255, 0, 0, 0))
                draw = ImageDraw.Draw(img)
                draw.line((line_1, 0, line_1, CAMERA_HEIGHT), width=1)
                draw.line((line_2, 0, line_2, CAMERA_HEIGHT), width=1)
                # Run detection
                #start_ms = time.time()
                results = engine.detect_with_image(image,
                                                 threshold=obj_prcnt, top_k=5)

                #elapsed_ms = (time.time() - start_ms)*1000.0
                if results:
                    for obj in results:
                        if (labels[obj.label_id] != label_of_interest_1):
                            box = obj.bounding_box.flatten().tolist()
                            box[0] *= CAMERA_WIDTH
                            box[1] *= CAMERA_HEIGHT
                            box[2] *= CAMERA_WIDTH
                            box[3] *= CAMERA_HEIGHT
                            # print(box)
                            # print(labels[obj.label_id])
                            draw.rectangle(box, outline='#4287f5') #cyan
                            scrn_lbl = labels[obj.label_id] + str(int(round(obj.score*100,0))) +"%"
                            draw.text((box[0], box[1]-10), scrn_lbl, font=fnt, fill="#98bcf5") #light blue
                        
                        if (labels[obj.label_id] == label_of_interest_1):
                            #draw_bbox(obj, labels, move_order, fnt, '#FF0000', '#7fff00',CAMERA_WIDTH, CAMERA_HEIGHT, draw)
                            box = obj.bounding_box.flatten().tolist()
                            box[0] *= CAMERA_WIDTH
                            box[1] *= CAMERA_HEIGHT
                            box[2] *= CAMERA_WIDTH
                            box[3] *= CAMERA_HEIGHT
                            # print(box)
                            # print(labels[obj.label_id])
                            draw.rectangle(box, outline='#FF0000')#red
                            scrn_lbl = labels[obj.label_id] + str(int(round(obj.score*100,0))) +"%"
                            draw.text((box[0], box[1]-10), scrn_lbl, font=fnt, fill="#7fff00") #yello 
                            camera.annotate_text = str(distance())+"in "
                            #camera.annotate_text = labels[obj.label_id] +", " + str(obj_dist)+"in"
                            obj_width = box[2] - box[0]
                            obj_center = box[0] + obj_width // 2
                            #draw.point((obj_center, box[1] + (box[3] - box[1])//2))
                            draw.text((obj_center, (box[1] + (box[3] - box[1])//2)), "X", font=fnt, fill="red")
                            #print(obj_center - CAMERA_WIDTH // 2)
                            print("C",int(obj_center), ",W", int(obj_width), ",D", int(distance()))
                            line_1= int((CAMERA_WIDTH/2)-(obj_width/2))
                            line_2= int((CAMERA_WIDTH/2)+(obj_width/2))
                            # after render move robot to obj
                            if obj_center > line_2:
                                move_order="R->"
                                print(move_order)
                                moto_move("right",20,0)
                            elif obj_center < line_1:
                                move_order="L<-"
                                print(move_order)
                                moto_move("left",20,0)
                            elif obj_width < (CAMERA_WIDTH * 0.36) or int(distance())>10:
                                move_order="FWD"
                                print(move_order)
                                moto_move("forward", 0, int(distance()-3))
                            if obj_width >= (CAMERA_WIDTH * 0.36) or int(distance())<10:
                                move_order="STP/" +arm_action
                                print(move_order)
                                print("C",int(obj_center), ",W", int(obj_width), ",D", int(distance()))
                                time.sleep(5)
                                moto_move("forward", 0, 2)
                                #moto_move("release",0,0)
                                #time.sleep(1)
                                move_order="PIK"
                                robo_arm(arm_action)
                                print(move_order)
                                print("model switched to COCO dataset")
                                engine = DetectionEngine(model_filename_2)
                                labels = _read_label_file(label_filename_2)
                                label_of_interest_1 = label_of_interest_2
                                obj_prcnt = 0.4
                                arm_action = "drop"
                                
                else:
                    move_order="find obj"
                    print(move_order)
                    if search_maneuver_counter < len(search_maneuver):
                        movement = search_maneuver[search_maneuver_counter]["mvnt1"]
                        angle = search_maneuver[search_maneuver_counter]["angle"]
                        dist = search_maneuver[search_maneuver_counter]["dist"]
                        moto_move(movement,angle,dist)
                        search_maneuver_counter = search_maneuver_counter + 1
                    else:
                        move_order="no obj"
                        print(move_order)
                        search_maneuver_counter = 0
                                   
                    
                if not overlay_renderer:
                    overlay_renderer = camera.add_overlay(
                        img.tobytes(),
                        size=(CAMERA_WIDTH, CAMERA_HEIGHT), layer=4, alpha=255)
                else:
                    overlay_renderer.update(img.tobytes())
        except KeyboardInterrupt:
#             if overlay_renderer:
#                 camera.remove_overlay(overlay_renderer)
            camera.stop_preview()
            GPIO.cleanup()
            turnOffMotors()
            roto_arm("pick")
            print("Exiting due to KBD, goodbye")
            exit()
        finally:
#             if overlay_renderer:
#                 camera.remove_overlay(overlay_renderer)
            camera.stop_preview()
            GPIO.cleanup()
            turnOffMotors()
            roto_arm("pick")
            print("goodbye")
            


if __name__ == "__main__":
    main()
