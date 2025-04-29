'''Prints true/false if car headlights are on.Headlights of a car automatically turn on when daylight outside is below a certain threshold. 
If  the sensor is below 8, then headlights are on, otherwise they are off '''

sensor = 7

if sensor < 8:
    print('Headlights On')
else:
    print("Headlights Off")
