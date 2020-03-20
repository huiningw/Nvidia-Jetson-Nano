import smbus
import time

bus = smbus.SMBus(1)
address = 0x69
power_mgmt=0x6c

acc_z_15_8=0x17
acc_z_7_0=0x16
acc_y_15_8=0x15
acc_y_7_0=0x14
acc_x_15_8=0x13
acc_x_7_0=0x12

bus.write_byte_data(address,power_mgmt,0)

def read_acc_z_15_8(acc_z_15_8):
     return bus.read_byte_data(address,acc_z_15_8)

def read_acc_z_7_0(acc_z_7_0):
     return bus.read_byte_data(address,acc_z_7_0)

while True:
        high_byte = read_acc_z_15_8(acc_z_15_8)     
        low_byte = read_acc_z_7_0(acc_z_7_0)   
        twobytes = (high_byte << 8) + low_byte
        print twobytes
        time.sleep(0.5) 