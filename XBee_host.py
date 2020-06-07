import matplotlib.pyplot as plt
import numpy as np
import serial
import time

# XBee setting
serdev = '/dev/ttyUSB0'
s = serial.Serial(serdev, 9600)

s.write("+++".encode())
char = s.read(2)
print("Enter AT mode.")
print(char.decode())

s.write("ATMY 0x167\r\n".encode())
char = s.read(3)
print("Set MY 0x167.")
print(char.decode())

s.write("ATDL 0x267\r\n".encode())
char = s.read(3)
print("Set DL 0x267.")
print(char.decode())

s.write("ATID 0x1\r\n".encode())
char = s.read(3)
print("Set PAN ID 0x1.")
print(char.decode())

s.write("ATWR\r\n".encode())
char = s.read(3)
print("Write config.")
print(char.decode())

s.write("ATMY\r\n".encode())
char = s.read(4)
print("MY :")
print(char.decode())

s.write("ATDL\r\n".encode())
char = s.read(4)
print("DL : ")
print(char.decode())

s.write("ATCN\r\n".encode())
char = s.read(3)
print("Exit AT mode.")
print(char.decode())

print("start sending RPC")
#for i in range(0, int(10)):
    # send RPC to remote

    #s.write("print:\n\r".encode())
    #time.sleep(0.5)

s.write("print:\n\r".encode())
time.sleep(1.0)  
s.write("print:\n\r".encode())
time.sleep(1.0)
s.write("print:\n\r".encode())
time.sleep(1.0)
s.write("print:\n\r".encode())
time.sleep(1.0)
s.write("print:\n\r".encode())
time.sleep(1.0)
s.write("print:\n\r".encode())
time.sleep(1.0)
s.write("print:\n\r".encode())
time.sleep(1.0)
s.write("print:\n\r".encode())
time.sleep(1.0)
s.write("print:\n\r".encode())
time.sleep(1.0)
s.write("print:\n\r".encode())
time.sleep(1.0)

# draw
t = np.arange(0,10,0.5) 
x = np.arange(0,10,0.5) 
y = np.arange(0,10,0.5)
z = np.arange(0,10,0.5)
tilt = np.arange(0,10,0.5)

#line=s.readline() # Read an echo string from K66F terminated with '\n'
for i in range(0, int(10)):
    line=s.readline()
    #line=s.readline() # Read an echo string from K66F terminated with '\n'
    #xbee_string=''
    #while(s.readable()):
    #    c=s.read(1)
    #    xbee_string+=c
    # print line
    x[i] = float(line)
    line=s.readline() # Read an echo string from K66F terminated with '\n'
    
    # print line
    y[i] = float(line)
    line=s.readline() # Read an echo string from K66F terminated with '\n'
    
    # print line
    z[i] = float(line)

plt.plot(t,x, color = "blue", linewidth = 1, linestyle = "-", label = "x")
plt.plot(t,y, color = "red", linewidth = 1, linestyle = "-", label = "y")
plt.plot(t,z, color = "green", linewidth = 1, linestyle = "-", label = "z")
# Show legend
plt.legend(loc='lower left', frameon=False)
#plt.set_xlabel('Time')
#plt.set_ylabel('Acc vector')
plt.show()

s.close()