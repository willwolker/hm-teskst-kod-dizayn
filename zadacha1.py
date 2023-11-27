from drawbot_skia.drawbot import oval, fill, saveImage
oval(400, 500, 600, 700)
fill(0, 0, 1) 
y = 500
step = 200
for i in range(3):
y = y + step
oval (400, y, 600, 700)
saveImage('zadacha1.pdf')