import cairo
import math
import os

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 40, 40)
ctx = cairo.Context(surface)
ctx.set_antialias(cairo.ANTIALIAS_BEST)

ctx.set_source_rgba(1, 0, 0, 0)
ctx.paint()

ctx.set_source_rgb(0.439, 0.573, 0.745)
ctx.arc(20, 17, 12, math.pi, 2 * math.pi)
ctx.fill()

ctx.set_source_rgb(0.439, 0.573, 0.745)
ctx.rectangle(8, 17, 24, 16)
ctx.fill()

ctx.set_source_rgb(0.439, 0.573, 0.745)
ctx.arc(12, 33, 4, 0,  math.pi)
ctx.fill()

ctx.set_source_rgb(0.439, 0.573, 0.745)
ctx.arc(20, 33, 4, 0,  math.pi)
ctx.fill()

ctx.set_source_rgb(0.439, 0.573, 0.745)
ctx.arc(28, 33, 4, 0,  math.pi)
ctx.fill()

ctx.set_source_rgb(1, 1, 1)
ctx.rectangle(15, 16, 4, 8)
ctx.fill()

ctx.set_source_rgb(1, 1, 1)
ctx.rectangle(21, 16, 4, 8)
ctx.fill()

ctx.set_source_rgb(0.339, 0.473, 0.645)
ctx.rectangle(22, 18, 2, 5)
ctx.fill()

ctx.set_source_rgb(0.339, 0.473, 0.645)
ctx.rectangle(16, 18, 2, 5)
ctx.fill()

main_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
asset_folder = os.path.join(main_folder, "asset")
os.makedirs(asset_folder, exist_ok=True)
surface.write_to_png(os.path.join(asset_folder, "enemy2sprite.png"))
print("Hytam")