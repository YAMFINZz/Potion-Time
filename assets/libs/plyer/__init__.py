'''
Plyer
=====

'''

__all__ = (
    'accelerometer', 'audio', 'barometer', 'battery', 'bluetooth',
    'brightness', 'call', 'camera', 'compass', 'cpu', 'email', 'filechooser',
    'flash', 'gps', 'gravity', 'gyroscope', 'humidity', 'irblaster',
    'keystore', 'light', 'notification', 'orientation', 'processors',
    'proximity', 'screenshot', 'sms', 'spatialorientation', 'storagepath',
    'stt', 'temperature', 'tts', 'uniqueid', 'vibrator', 'wifi', 'devicename'
)

__version__ = '2.1.0'


from facades import *
from utils import Proxy

#: Accelerometer proxy to :class:`plyer.facades.Accelerometer`
accelerometer = Proxy('accelerometer', Accelerometer)

#: Keyring proxy to :class::`plyer.facades.Keystore`
keystore = Proxy('keystore', Keystore)

#: Audio proxy to :class:`plyer.facades.Audio`
audio = Proxy('audio', Audio)

#: Barometer proxy to :class:`plyer.facades.Barometer`
barometer = Proxy('barometer', Barometer)

#: Battery proxy to :class:`plyer.facades.Battery`
battery = Proxy('battery', Battery)

#: Call proxy to  :class `plyer.facades.Call`
call = Proxy('call', Call)

#: Compass proxy to :class:`plyer.facades.Compass`
compass = Proxy('compass', Compass)

#: Camera proxy to :class:`plyer.facades.Camera`
camera = Proxy('camera', Camera)

#: Email proxy to :class:`plyer.facades.Email`
email = Proxy('email', Email)

#: FileChooser proxy to :class:`plyer.facades.FileChooser`
filechooser = Proxy('filechooser', FileChooser)

#: GPS proxy to :class:`plyer.facades.GPS`
gps = Proxy('gps', GPS)

#: Gravity proxy to :class:`plyer.facades.Gravity`
gravity = Proxy('gravity', Gravity)

#: Gyroscope proxy to :class:`plyer.facades.Gyroscope`
gyroscope = Proxy('gyroscope', Gyroscope)

#: IrBlaster proxy to :class:`plyer.facades.IrBlaster`
irblaster = Proxy('irblaster', IrBlaster)

#: Light proxy to :class:`plyer.facades.Light`
light = Proxy('light', Light)

#: Orientation proxy to :class:`plyer.facades.Orientation`
orientation = Proxy('orientation', Orientation)

#: Notification proxy to :class:`plyer.facades.Notification`
notification = Proxy('notification', Notification)

#: Proximity proxy to :class:`plyer.facades.Proximity`
proximity = Proxy('proximity', Proximity)

#: Sms proxy to :class:`plyer.facades.Sms`
sms = Proxy('sms', Sms)

#: Speech proxy to :class:`plyer.facades.STT`
stt = Proxy('stt', STT)

#: TTS proxy to :class:`plyer.facades.TTS`
tts = Proxy('tts', TTS)

#: UniqueID proxy to :class:`plyer.facades.UniqueID`
uniqueid = Proxy('uniqueid', UniqueID)

#: Vibrator proxy to :class:`plyer.facades.Vibrator`
vibrator = Proxy('vibrator', Vibrator)

#: Flash proxy to :class:`plyer.facades.Flash`
flash = Proxy('flash', Flash)

#: Wifi proxy to :class:`plyer.facades.Wifi`
wifi = Proxy('wifi', Wifi)

#: Temperature proxy to :class:`plyer.facades.Temperature`
temperature = Proxy('temperature', Temperature)

#: Humidity proxy to :class:`plyer.facades.Humidity`
humidity = Proxy('humidity', Humidity)
#: SpatialOrientation proxy to :class:`plyer.facades.SpatialOrientation`
spatialorientation = Proxy('spatialorientation', SpatialOrientation)

#: Brightness proxy to :class:`plyer.facades.Brightness`
brightness = Proxy('brightness', Brightness)

#: StoragePath proxy to :class:`plyer.facades.StoragePath`
storagepath = Proxy('storagepath', StoragePath)

#: Bluetooth proxy to :class:`plyer.facades.Bluetooth`
bluetooth = Proxy('bluetooth', Bluetooth)

#: Processors proxy to :class:`plyer.facades.Processors`
processors = Proxy('processors', Processors)

#: Processors proxy to :class:`plyer.facades.CPU`
cpu = Proxy('cpu', CPU)

#: Screenshot proxy to :class:`plyer.facades.Screenshot`
screenshot = Proxy('screenshot', Screenshot)

#: devicename proxy to :class:`plyer.facades.DeviceName`
devicename = Proxy('devicename', DeviceName)
