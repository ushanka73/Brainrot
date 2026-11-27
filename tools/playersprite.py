import cairo
import math
import os

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 40, 40)
ctx = cairo.Context(surface)

ctx.set_source_rgba(1, 1, 0, 0)
ctx.paint()

#Head
ctx.set_source_rgb(0.961, 0.816, 0.773)
ctx.rectangle(13, 6, 18, 16)
ctx.fill()

ctx.set_source_rgb(0.533, 0.000, 0.082)
ctx.rectangle(13, 18, 18, 4)
ctx.fill()

#Matah
ctx.set_source_rgb(1, 1, 1)
ctx.rectangle(27, 11, 3, 6)
ctx.fill()

ctx.set_source_rgb(1, 1, 1)
ctx.rectangle(22, 11, 3, 6)
ctx.fill()

ctx.set_source_rgb(0.439, 0.573, 0.745)
ctx.rectangle(23, 13, 2, 4)
ctx.fill()

ctx.set_source_rgb(0.439, 0.573, 0.745)
ctx.rectangle(28, 13, 2, 4)
ctx.fill()

#rambut
ctx.set_source_rgb(0.08, 0.08, 0.08)
ctx.rectangle(13, 6, 18, 4)
ctx.fill()

ctx.set_source_rgb(0.08, 0.08, 0.08)
ctx.rectangle(13, 10, 4, 4)
ctx.fill()

ctx.set_source_rgb(0.08, 0.08, 0.08)
ctx.rectangle(17, 10, 2, 2)
ctx.fill()

#Body

ctx.set_source_rgb(0.533, 0.000, 0.082)
ctx.rectangle(13, 22, 17, 10)
ctx.fill()

ctx.set_source_rgb(0.3, 0.3, 0.3)
ctx.rectangle(13, 27, 17, 5)
ctx.fill()

#feet
ctx.set_source_rgb(0.3, 0.3, 0.3)
ctx.rectangle(13, 32, 7, 4)
ctx.fill()

ctx.set_source_rgb(0.602, 0.602, 0.780)
ctx.rectangle(13, 33, 8, 2)
ctx.fill()

ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.rectangle(13, 35, 8, 1)
ctx.fill()

ctx.set_source_rgb(0.3, 0.3, 0.3)
ctx.rectangle(24, 32, 6, 4)
ctx.fill()

ctx.set_source_rgb(0.602, 0.602, 0.780)
ctx.rectangle(24, 33, 7, 2)
ctx.fill()

ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.rectangle(24, 35, 7, 1)
ctx.fill()

#backpack
ctx.set_source_rgb(0.439, 0.573, 0.745)
ctx.rectangle(8, 16, 5, 11)
ctx.fill()

ctx.set_source_rgb(0.439, 0.573, 0.745)
ctx.rectangle(13, 16, 5, 2)
ctx.fill()

ctx.set_source_rgb(0.439, 0.573, 0.745)
ctx.rectangle(16, 16, 2, 7)
ctx.fill()

ctx.set_source_rgb(0.439, 0.573, 0.745)
ctx.rectangle(13, 23, 5, 1)
ctx.fill()

main_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
asset_folder = os.path.join(main_folder, "asset")
os.makedirs(asset_folder, exist_ok=True)
surface.write_to_png(os.path.join(asset_folder, "playersprite.png"))
print("Hytam")