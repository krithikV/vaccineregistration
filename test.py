from multiprocessing import Process

server = Process(target=app.run)# ...
server.terminate()
