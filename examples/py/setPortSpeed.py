import sys
import os
sys.path.append(os.path.abspath('../../py'))
from flexswitchV2 import FlexSwitch

"""This program demonstrates 
   simple update APIs supported by FlexSwitch SDK. 
   This specific example modifies speed of a port
   All the update APIs follow similar pattern.
   for object 'OBJ_X" the update API would be
   updateOBJ_X (key, parameter= value)
   """

if __name__ == '__main__':
    swtch = FlexSwitch ('10.1.10.240', 8080)  # Instantiate object to talk to flexSwitch
<<<<<<< HEAD
    response, error = swtch.updatePort(1, Speed=1003) 
=======
    response, error = swtch.updatePort(1, Speed=1000) 
>>>>>>> aa409bbcf278d49546c1dfd7147b94a787430c98
    if error != None: #Error not being None implies there is some problem
        print error
    else :
        print 'Updated port speed successfully' 
