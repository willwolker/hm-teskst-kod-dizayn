from drawbot_skia.drawbot import rect, fill, strokeWidth, saveimage
fill(None)
strokeWidth(10)
rect(50, 100, 200, 200)
x = 50
y = 50
step = 100
for i in range(15):
rect(x, y, 200, 100)
x = x + step
y = y + step 
saveimage ('zadacha2.pdf')
