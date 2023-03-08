import socket

def sever():
	host =socket.gethostname()
	port =6000

	server_socket =socket.socket()
	server_socket.blind((host, port))
	server_socket.listen(1)
	conn, address =server_socket.accept()
	print(f"Connection from {str(address)}")
	while(True):
		data =conn.recv(1024).decode()
		if (not data):
			break
		print(f"from connected user {str(data)}")
		data =input(">_")
		conn.send(data.encode())
	conn.close()

	if __name__ =='__main__':
		server()