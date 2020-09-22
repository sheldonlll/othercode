from PIL import Image
def transparent_back():
    img = Image.open('logo.ico')

    # 图片转换为四通道。第四个通道就是我们要修改的透明度。返回新的对象
    img = img.convert('RGBA')  
    # 获取图片像素尺寸
    width, height = img.size 
    pixel_data = img.load()
    for h in range(height):
        for w in range(width):
            pixel = pixel_data[w, h]
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            a = pixel[3]
            # 四通道，色彩值大于浅灰色，则将像素点变为透明块
            if r > 220 and g > 220 and b > 220 and a > 220:
                pixel_data[w, h] = (255, 255, 255, 0)
    img.save('newlogo.ico')  # 保存新图片
transparent_back()
