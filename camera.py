from picamera import PiCamera
from time import sleep

camera = PiCamera()

def startPreview():
	camera.start_preview()

def stopPreview():
	camera.stop_preview()

startPreview()
sleep(10)
stopPreview()