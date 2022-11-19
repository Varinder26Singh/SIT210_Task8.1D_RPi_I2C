# Name - Varinder Singh
# Roll Number - 2110994796
# Task - SIT210_Task8.1D_RPi_I2C

# To use I2c devices we use a library - Smbus
import smbus

# To give delay in the program --- time.sleep()
import time

# I2C Address of GY-30 (BH-1750 FVI) -- https://i2cdevices.org/addresses -- i2cdetect -y 0
address = 0x23

# To use smbus library we need an instance variable which have a single parameter ID -- 0 = Old Raspberry Pi Model's with 26 pind ; 1 = For Models having 40 pins 
bus = smbus.SMBus(1)

#Function - lightIntensity_Value = To read the data values from the sensor, (here from GY-30)
def lightIntensity_Value():
    
    # Read the data values
    data = bus.read_i2c_block_data(address, address)
    
    # Converting the reading / data value's to decimal number
    Value = ((data[1] + (256 * data[0]))/1.2)
    
    return Value

# Main program function
def main():
    #Run
    try:
        # while 1 --- to run this loop infinite number of times
        while 1:

            # Reading the value and displaying on the serial monitor
            Value = lightIntensity_Value()
            
            print ("Light Intensity Data Value (Readings) Given By Sensor Is = : " + str(Value) + " Lux")

            # Printing the status on to the serial monitor according to the light conditions
            if(Value >= 2500):
                print("Too bright")
                            
            elif(Value >= 1000 and Value < 2500):
                print("Bright")
                            
            elif(Value >= 200 and Value < 1000):
                print("Medium")
                            
            elif(Value > 70 and Value < 200):
                print("Dark")
                            
            else:
                print("Too dark")

            # to give a delay before taking the next reading / data value 
            time.sleep(1)


    # in case of keyboard interruption close the program
    except KeyboardInterrupt:
        print("Exiting")


if __name__ == "__main__":
    main()
