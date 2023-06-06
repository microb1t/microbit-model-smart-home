# microbit-smart-home
This is the code repository for the code I used for the microbits to make my 'smart home.' This is a project for school that I did.

I made the project in Microsoft's MakeCode platform (https://makecode.microbit.org). I'm going to link the files somewhere, maybe I'll use the feature built in to MakeCode where you can export your code as a Github repository, and then I'll just have a link to that.

## **My Adventure**

This project was a lot more than I thought it was going to be. It was a five week long project, so five days a week. Two of the weeks were only 4 school days because of Memorial Day. Plus, class periods are, on average, about 35-40 minutes long depending on wether or not we had Advisory that day. Plus, getting the materials out at the start of the period and putting them back at the end leaves about 30 minutes for working on the project. The classroom wasn't exactly the best place for concentrating on working to make the project, as there were lots of people messing around on the other side of the classroom. So if it seems like this project took way longer than it should've, it's because of the short work time per day and the destractions in the classroom.

## **Timeline**

   ### Week 1
   
   On the first week of this project I focused on building the physical model of the house and putting the lights in. To do that, I had limited materials and the wires I chose to connect to the LEDs were alligator clips on one side and the male pin on the other so I could connect them to a breadboard. The following image was the result of Week 1. 
  
  PS: I know the picture looks like it was taken on a potato that's been left out in a field for 39 years, that's because it was. (It was taken on a chromebook)

  
![168598703737461727](https://github.com/microb1t/microbit-model-smart-home/assets/125515183/7640dbbe-2bd6-429d-8719-7a1c7ff67059)

 ### Week 2
 
 On the second week of this project I focused on adding more lights to the first floor of the house and coming up with a way to use Micro:bits to control the lights remotely. I think I should mention that I made many iterations of this code. I had to make more versions of the code for many reasons- some of which being a feature that I wanted to add, some being issues with the code itself, and some being compatibility issues with the micro:bit. There was also the occasional simple screw-up on my part, which happened more times than I want to admit.
 
 In the first iteration of my code, I focused on trying to control a servo that physically bridged a positively charged wire in order to control the lights to the house. I also tried to make this code as simple as possible, just in case something didn't work correctly. So I started my code off by setting the radio channel and defining and setting the "angle" variable to measure the servo angle. By the way, this code is in python.
 
      angle = 0
      radio.set_group(1)
      angle = 90 
  
Then, I set what would happen if I pressed the A and B buttons. I wanted it so if I pressed the A button, it would decrease the servo angle by 10, but not go past 0 so the displayed angle would stay accurate to the actual servo angle.

      def on_button_pressed_a():
         global angle
         angle = max(0, angle - 10)
         radio.send_number(angle)
         led.stop_animation()
      input.on_button_pressed(Button.A, on_button_pressed_a)
      
      def on_button_pressed_b():
         global angle
         angle = min(180, angle + 10)
         radio.send_number(angle)
         led.stop_animation()
      input.on_button_pressed(Button.B, on_button_pressed_b)
      
Then, I added a forever loop that would show the servo angle on the microbit LED array.
      
      def on_forever():
         basic.show_number(angle)
      basic.forever(on_forever)

### Code for the 'receiving' Micro:bit

For the other microbit that would be receiving the signal containing the angle change, I used this code:

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
      
But this was only the first version of this code. As I changed things, I had to change the code. I will have all of the code in the files section.
      


      
      
