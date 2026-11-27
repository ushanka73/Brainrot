import cairo
import math
import os

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 40, 40)
ctx = cairo.Context(surface)
ctx.set_antialias(cairo.ANTIALIAS_BEST)

ctx.set_source_rgba(1, 0, 0, 0)
ctx.paint()

ctx.set_source_rgb(0.08, 0.08, 0.08)
ctx.arc(20, 20, 10, 0, 2 * math.pi)
ctx.fill()

ctx.set_source_rgb(0.08, 0.08, 0.08)
ctx.rectangle(19, 2, 2, 36)
ctx.fill()

ctx.set_source_rgb(0.08, 0.08, 0.08)
ctx.rectangle(2, 19, 36, 2)
ctx.fill()

ctx.set_source_rgb(0.08, 0.08, 0.08)
ctx.save()
ctx.translate(20, 20)
ctx.rotate(math.radians(45))
ctx.rectangle(-1, -18, 2, 36)
ctx.fill()

ctx.rotate(math.radians(90))
ctx.rectangle(-1, -18, 2, 36)
ctx.fill()
ctx.restore()

ctx.set_source_rgb(1, 1, 1)
ctx.rectangle(15, 16, 4, 8)
ctx.fill()

ctx.set_source_rgb(1, 1, 1)
ctx.rectangle(21, 16, 4, 8)
ctx.fill()

ctx.set_source_rgb(0.533, 0.000, 0.082)
ctx.rectangle(22, 18, 2, 5)
ctx.fill()

ctx.set_source_rgb(0.533, 0.000, 0.082)
ctx.rectangle(16, 18, 2, 5)
ctx.fill()

main_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
asset_folder = os.path.join(main_folder, "asset")
os.makedirs(asset_folder, exist_ok=True)
surface.write_to_png(os.path.join(asset_folder, "enemy1sprite.png"))
print("Hytam")