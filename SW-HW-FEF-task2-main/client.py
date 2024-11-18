import serial
import time

uart_client = serial.Serial('COM3', 9600, timeout=1)

message = "Hello from Client"
uart_client.write(message.encode())
print(f"Sent to server: {message}")

time.sleep(1)  
response = uart_client.readline().decode()
print(f"Received from server: {response}")

uart_client.close()
