import picamera
import time

camera = PiCamera()
camera.resolution = (1024, 768)

def closeCamera():
	camera.close()

def startPreview():
	camera.start_preview()

def stopPreview():
	camera.stop_preview()

def takePicture():
	camera.capture('foo.jpg')

startPreview()
sleep(5)
takePicture()
stopPreview()
