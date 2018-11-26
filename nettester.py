import RPi.GPIO as gpio
import time

def init():
	"""
	set pins output
	"""
	gpio.setmode(gpio.BCM)
	gpio.setup(2,gpio.IN)
	gpio.setup(4,gpio.OUT)
	gpio.setup(14,gpio.OUT)
	gpio.setup(15,gpio.OUT)
	gpio.setup(17,gpio.OUT)
	gpio.setup(18,gpio.OUT)
	animation(0.1)
	for i in range(3)
		animation(0)
		time.sleep(0.1)


def animation(duration):
	gpio.output(4,1)
	time.sleep(duration)
	gpio.output(14,1)
	time.sleep(duration)
	gpio.output(15,1)
	time.sleep(duration)
	gpio.output(17,1)
	time.sleep(duration)
	gpio.output(18,1)
	time.sleep(duration)

	if duration==0:
		time.sleep(0.1)
		
	gpio.output(4,0)
	time.sleep(duration)
	gpio.output(14,0)
	time.sleep(duration)
	gpio.output(15,0)
	time.sleep(duration)
	gpio.output(17,0)
	time.sleep(duration)
	gpio.output(18,0)	
	time.sleep(duration)

def main():
	init():


if __name__ == '__main__':
    main()