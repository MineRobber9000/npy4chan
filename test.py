import npy4chan,time
print("IMPORTS OK")
api = npy4chan.load()
print("PRIMARY LOAD OK")
for board in api.boards:
	print(u"Successful read of /{}/ - {} from table".format(board,api.boards[board]))
vr = api.getPosts("vr")
print("PAGE GRAB OK")
time.sleep(10)
thread = api.getThread("vr",vr["threads"][1]["posts"][1]["resto"])
print("THREAD GRAB OK")

