import cairo
import os

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 40, 40)
ctx = cairo.Context(surface)

ctx.set_source_rgb(0.992, 0.565, 0.718)
ctx.paint()

ctx.set_source_rgb(1.000, 0.682, 0.788)
ctx.move_to(0, 1)
ctx.line_to(38, 1)
ctx.stroke()

ctx.set_source_rgb(0.7922, 0.2314, 0.3647)
ctx.move_to(0, 39)
ctx.line_to(40, 39)
ctx.stroke()

ctx.set_source_rgb(0.7922, 0.2314, 0.3647)
ctx.move_to(0, 20)
ctx.line_to(40, 20)
ctx.stroke()

ctx.set_source_rgb(0.7922, 0.2314, 0.3647)
ctx.move_to(39, 0)
ctx.line_to(39, 20)
ctx.stroke()

ctx.set_source_rgb(1.000, 0.682, 0.788)
ctx.move_to(1, 0)
ctx.line_to(1, 19)
ctx.stroke()

ctx.set_source_rgb(1.000, 0.682, 0.788)
ctx.move_to(22, 21)
ctx.line_to(22, 38)
ctx.stroke()

ctx.set_source_rgb(1.000, 0.682, 0.788)
ctx.move_to(0, 22)
ctx.line_to(40, 22)
ctx.stroke()

ctx.set_source_rgb(0.969, 0.376, 0.600)
ctx.move_to(0, 18)
ctx.line_to(38, 18)
ctx.stroke()

ctx.set_source_rgb(0.969, 0.376, 0.600)
ctx.move_to(0, 37)
ctx.line_to(40, 37)
ctx.stroke()

ctx.set_source_rgb(0.7922, 0.2314, 0.3647)
ctx.move_to(20, 20)
ctx.line_to(20, 40)
ctx.stroke()

ctx.set_source_rgb(0.7922, 0.2314, 0.3647)
ctx.rectangle(8, 5, 24, 40)
ctx.fill()

ctx.set_source_rgb(0.369, 0.208, 0.067)
ctx.rectangle(10, 7 , 20, 40)
ctx.fill()

ctx.set_source_rgb(0.529, 0.294, 0.106)
ctx.move_to(13, 7)
ctx.line_to(13, 40)
ctx.stroke()
ctx.close_path()

ctx.set_source_rgb(0.529, 0.294, 0.106)
ctx.move_to(17, 7)
ctx.line_to(17, 40)
ctx.stroke()
ctx.close_path()

ctx.set_source_rgb(0.529, 0.294, 0.106)
ctx.move_to(21, 7)
ctx.line_to(21, 40)
ctx.stroke()
ctx.close_path()

ctx.set_source_rgb(0.529, 0.294, 0.106)
ctx.move_to(25, 7)
ctx.line_to(25, 40)
ctx.stroke()
ctx.close_path()

ctx.set_source_rgb(0.529, 0.294, 0.106)
ctx.move_to(29, 7)
ctx.line_to(29, 40)
ctx.stroke()
ctx.close_path()

ctx.set_source_rgb(0.559, 0.371, 0.292)
ctx.move_to(10, 14)
ctx.line_to(30, 14)
ctx.set_line_width(4)
ctx.stroke()
ctx.close_path()

ctx.set_source_rgb(0.559, 0.371, 0.292)
ctx.move_to(10, 34)
ctx.line_to(30, 34)
ctx.set_line_width(4)
ctx.stroke()
ctx.close_path()

ctx.set_source_rgb(0.502, 0.502, 0.502)
ctx.rectangle(25, 22, 4, 4)
ctx.fill()

main_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
asset_folder = os.path.join(main_folder, "asset")
os.makedirs(asset_folder, exist_ok=True)
surface.write_to_png(os.path.join(asset_folder, "pintu.png"))
print("Hytam")