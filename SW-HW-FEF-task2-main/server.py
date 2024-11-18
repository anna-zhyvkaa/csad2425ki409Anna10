import serial

uart_server = serial.Serial('COM4', 9600, timeout=1)

while True:
    message = uart_server.readline().decode()
    if message:
        print(f"Server received: {message}")

       
        modified_message = f"Server: {message}"
        uart_server.write(modified_message.encode())
        print(f"Server sent: {modified_message}")
