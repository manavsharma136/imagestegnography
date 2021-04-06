from PIL import Image
import stepic
m = Image.open('aa1.png')
 
m1 = stepic.encode(im, b'Hello manav')
m1.save('aa1.png', 'PNG')


m1 = Image.open('aa1.png')
m1.show()
m.show()

im2 = Image.open('aa1.png')
stegoImage = stepic.decode(im2)
stegoImage
