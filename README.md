# microbit-smart-home
This is the code repository for the code I used for the microbits to make my 'smart home.' This is a project for school that I did.

I made the project in Microsoft's MakeCode platform (https://makecode.microbit.org). I'm going to link the files somewhere, maybe I'll use the feature built in to MakeCode where you can export your code as a Github repository, and then I'll just have a link to that.

## **My Adventure**

This project was a lot more than I thought it was going to be. It was a five week long project, so five days a week. Two of the weeks were only 4 school days because of Memorial Day. Plus, class periods are, on average, about 35-40 minutes long depending on wether or not we had Advisory that day. Plus, getting the materials out at the start of the period and putting them back at the end leaves about 30 minutes for working on the project. The classroom wasn't exactly the best place for concentrating on working to make the project, as there were lots of people messing around on the other side of the classroom. So if it seems like this project took way longer than it should've, it's because of the short work time per day and the destractions in the classroom.

## **Timeline**

   ### Week One
   
   On the first week of this project I focused on building the physical model of the house and putting the lights in. To do that, I had limited materials and the wires I chose to connect to the LEDs were alligator clips on one side and the male pin on the other so I could connect them to a breadboard. The following image was the result of Week 1. 
  
  PS: I know the picture looks like it was taken on a potato that's been left out in a field for 39 years, that's because it was. (It was taken on a chromebook)

  
![168598703737461727](https://github.com/microb1t/microbit-model-smart-home/assets/125515183/7640dbbe-2bd6-429d-8719-7a1c7ff67059)

 ### Week Two
 
 On the second week of this project I focused on adding more lights to the first floor of the house and coming up with a way to use Micro:bits to control the lights remotely. I think I should mention that I made many iterations of this code. I had to make more versions of the code for many reasons- some of which being a feature that I wanted to add, some being issues with the code itself, and some being compatibility issues with the micro:bit. There was also the occasional simple screw-up on my part, which happened more times than I want to admit.
 
 In the first iteration of my code, I focused on trying to control a servo that physically bridged a positively charged wire in order to control the lights to the house. I also tried to make this code as simple as possible, just in case something didn't work correctly. So I started my code off by setting the radio channel and defining and setting the "angle" variable to measure the servo angle. By the way, this code is in python.
 
```py
angle = 0
radio.set_group(1)
angle = 90
```
  
Then, I set what would happen if I pressed the A and B buttons. I wanted it so if I pressed the A button, it would decrease the servo angle by 10, but not go past 0 so the displayed angle would stay accurate to the actual servo angle.

```py
      def on_button_pressed_a():
         global angle
         angle = max(0, angle - 10)
         radio.send_number(angle)
         led.stop_animation()
      input.on_button_pressed(Button.A, on_button_pressed_a)
 ```
 
```py
      def on_button_pressed_b():
         global angle
         angle = min(180, angle + 10)
         radio.send_number(angle)
         led.stop_animation()
      input.on_button_pressed(Button.B, on_button_pressed_b)
```     
     
Then, I added a forever loop that would show the servo angle on the microbit LED array.
      
```py    
    def on_forever():
         basic.show_number(angle)
      basic.forever(on_forever)
```

### Code for the 'receiving' Micro:bit

For the other microbit that would be receiving the signal containing the angle change, I used this code:

```py
      # When the microbit receives a radio signal with a number,set the angle variable to that received value and write the servo on pin 0 to the angle variable.
      def on_received_number(receivedNumber):
         global angle
         angle = receivedNumber
         pins.servo_write_pin(AnalogPin.P0, angle)
         led.stop_animation()
      radio.on_received_number(on_received_number)
      
      # Add a variable 'angle' and set it to 90. Set radio group to 1 to match the controller and write the servo to the angle variable to start.
      
      angle = 0
      radio.set_group(1)
      angle = 90
      pins.servo_write_pin(AnalogPin.P0, angle)

      # Keep displaying the angle variable on the screen.

      def on_forever():
         basic.show_number(angle)
      basic.forever(on_forever)
```   
   
But this was only the first version of this code. As I changed things, I had to change the code. I will have all of the code in the files section.
           
### Week Three

On week three, we only had Monday, Tuesday, Wednesday and Thursday because of a no-school day on Friday. My main goal for week three was to continue making and revising the code, and to put the actual 'smart' features in the house. Week 3 was one of the worst weeks for me, not because I didn't get a lot done- because I did- but because of a **major** compatibility issue with the servo motors and the micro:bits. It turns out some of my code wasn't compatible with the micro:bit, but the problem was there was no way to find out which part of the code was the problem. So unfortunately, I had to redo the _entire_ controller code.

The end result after I completely changed everything was, instead of using two micro:bits, it used three. One for the controller, one for the power controlling servo, and the other for a new idea that I decided to add to the mix. I wanted to add a remote controlled window shade, for no particular reason besides being ahead of schedule and having the time to do so. This was one of the main reasons that I had to change the code. The reason I needed the third micro:bit was because they only have **one** 3.3 volt pin, and combined with the servos and the lights drawing power, it was too much for the single micro:bit, so I needed a third one for the second servo.

For the code, I had to have:

1. A way to switch between controlling the power servo and the window servo,
2. A way to monitor both of the servos,
3. A way to control the servos,

 And a way to tell which servo is which.

To be able to control both of the servos from one controller, I had to have an angle variable for both of the servos. So I started off by defining those, as well as setting the starting radio channel and the variable to tell which servo is being controlled.

```py
      radiochannel = 0
      windowangle = 0
      angle = 0
      radio.set_group(1)
      angle = 90
      windowangle = 90
      radiochannel = 1
```

Then I wanted to figure out a way to change between controlling the power and window servos. So I decided to make pressing the A and B buttons at the same time the thing that switches the servo control.

```py
      def on_button_pressed_ab():
         global radiochannel
         if radiochannel == 1:
            radiochannel = 2
         else:
            if radiochannel == 2:
               radiochannel = 1
      input.on_button_pressed(Button.AB, on_button_pressed_ab)
 ```
 
With that, the other things I had to figure out were a way to monitor both of the servos, a way to control them, and a way to be able to tell which is which. So I figured I might as well figure out how to control them. I wanted pressing the A button to decrease the servo angle by 10, and pressing the B button to increase the servo angle by 10.

```py
      def on_button_pressed_a():
         global angle, windowangle
         if radiochannel == 1:
            angle = min(180, angle - 10)
            radio.send_value("power", angle)
            led.stop_animation()
         elif radiochannel == 2:
            windowangle = min(180, windowangle - 10)
            radio.send_value("window", windowangle)
            led.stop_animation()
      input.on_button_pressed(Button.A, on_button_pressed_a)
```

Now for the B button:

```py
      def on_button_pressed_b():
         global angle, windowangle
         if radiochannel == 1:
            angle = max(0, angle + 10)
            radio.send_value("power", angle)
            led.stop_animation()
         elif radiochannel == 2:
            windowangle = max(0, windowangle + 10)
            radio.send_value("window", windowangle)
            led.stop_animation()
      input.on_button_pressed(Button.B, on_button_pressed_b)
```     
     
Now I only had to figure out how to monitor the servos and tell which one is being monitored since the micro:bit can only display one string at a time.

```py
      def on_forever():
         if radiochannel == 1:
            basic.show_string("p" + ("" + str(angle)))
         elif radiochannel == 2:
            basic.show_string("w" + ("" + str(windowangle)))
      basic.forever(on_forever)
```

That takes care of both of those issues, because the 'p' before the angle designates that it's showing the angle of the power servo, and the 'w' before the window angle designates that it's showing the angle of the window servo.

Now maybe you've noticed something wrong at this point, and don't worry, I'm going to adress it. The problem I'm referring to is the fact that I have the variable 'radiochannel', which isn't connected to the command 'radio.set_group()' in any way. So I can control the variable, but I can't switch between radio channels yet. To adress this, I used the 'run in background' feature to solve this problem.

```py
      def on_in_background(): 
         while True:
            radio.set_group(radiochannel)
            basic.pause(750)
      control.in_background(on_in_background)
```
You can decrease or increase the value in the basic.pause, I set it to 750ms because I don't want to overwhelm the micro:bit and have it constantly re-setting the radio group when it might not need to.

In the code above, you might see where it says 'while True:', but it doesn't have anything that can switch between true or false. I did this because in the coding software I used, you can't put a 'forever' loop inside of another loop, and the 'run in background' is a 'loop' according to the software. So anyways, I just used that to make a makeshift forever loop. It works perfectly for me.
      
Now for the receiving end, the code for each of the micro:bits that control their designated servo is basically the same except for a few things:
1. The radio group they are assigned to (the power servo is assigned to group 1, and the window servo is assigned to group 2)
2. The prefix before the number being shown (Yes, the micro:bits on the house each show their servo's current angle)

The power servo receiver code looks like this:

```py
def on_received_value(name, value):
    global angle
    if name == "power":
        angle = value
        pins.servo_write_pin(AnalogPin.P0, angle)
        led.stop_animation()
radio.on_received_value(on_received_value)

angle = 0
radio.set_group(1)
angle = 90
pins.servo_write_pin(AnalogPin.P0, angle)

def on_forever():
    basic.show_string("p" + str(angle))
basic.forever(on_forever)
```

And the window servo receiver code looks like this:
      
```py
def on_received_value(name, value):
    global angle
    if name == "window":
        angle = value
        pins.servo_write_pin(AnalogPin.P0, angle)
        led.stop_animation()
radio.on_received_value(on_received_value)

angle = 0
radio.set_group(2)
angle = 90
pins.servo_write_pin(AnalogPin.P0, angle)

def on_forever():
    basic.show_string("w" + str(angle))
basic.forever(on_forever)
```
      
### Week Four

![image](https://github.com/microb1t/microbit-model-smart-home/assets/125515183/3b284204-17a9-4c6e-b00a-5dcb905c875d)

