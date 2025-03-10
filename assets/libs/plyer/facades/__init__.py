'''
Facades
=======

Interface of all the features available.

'''
 
__all__ = ('Accelerometer', 'Audio', 'Barometer', 'Battery', 'Call', 'Camera',
            'Compass', 'Email', 'FileChooser', 'GPS', 'Gravity', 'Gyroscope',
            'IrBlaster', 'Light', 'Orientation', 'Notification', 'Proximity',
            'Sms', 'TTS', 'UniqueID', 'Vibrator', 'Wifi', 'Flash', 'CPU',
            'Temperature', 'Humidity', 'SpatialOrientation', 'Brightness',
            'Processors', 'StoragePath', 'Keystore', 'Bluetooth', 'Screenshot',
            'STT', 'DeviceName')

from accelerometer import Accelerometer
from audio import Audio
from barometer import Barometer
from battery import Battery
from call import Call
from camera import Camera
from compass import Compass
from email import Email
from filechooser import FileChooser
from flash import Flash
from gps import GPS
from gravity import Gravity
from gyroscope import Gyroscope
from irblaster import IrBlaster
from light import Light
from proximity import Proximity
from orientation import Orientation
from notification import Notification
from sms import Sms
from stt import STT
from tts import TTS
from uniqueid import UniqueID
from vibrator import Vibrator
from wifi import Wifi
from temperature import Temperature
from humidity import Humidity
from spatialorientation import SpatialOrientation
from brightness import Brightness
from keystore import Keystore
from storagepath import StoragePath
from bluetooth import Bluetooth
from processors import Processors
from cpu import CPU
from screenshot import Screenshot
from devicename import DeviceName 
