from PIL import Image, ImageDraw

im = Image.open('C:/Users/student/Pictures/Без имени.png')
# Откроет изображение в новом окне
im.show()
im = Image.new('RGB', (200, 200), color = ('#00BFFF'))
draw_text = ImageDraw.Draw(im)
draw_text.text(
    (80, 90),
    'deb',
    fill = ('#1C0606')
    )
im.show()
