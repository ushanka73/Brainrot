import os
import cairo

GELAP = (0.157, 0.098, 0.133)
TERANG = (1.000, 0.945, 0.961)
MERAH = (0.700, 0.100, 0.150)

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1280, 720)
ctx = cairo.Context(surface)

# panel
ctx.set_source_rgb(*TERANG)
ctx.rectangle(300, 180, 680, 360)
ctx.fill_preserve()
ctx.set_source_rgb(*GELAP)
ctx.set_line_width(2)
ctx.stroke()

# judul + subjudul
ctx.select_font_face("Liberation Sans", 0, 1)
teks = "Dava tertangkap"
ctx.set_font_size(42)
ctx.set_source_rgb(*MERAH)
ctx.move_to(surface.get_width() / 2 - ctx.text_extents(teks).x_advance / 2, 258)
ctx.show_text(teks)

ctx.select_font_face("Liberation Sans", 0, 0)
teks = "Coba lagi dari awal lantai ini."
ctx.set_font_size(20)
ctx.set_source_rgb(*GELAP)
ctx.move_to(surface.get_width() / 2 - ctx.text_extents(teks).x_advance / 2, 329)
ctx.show_text(teks)

# tombol
ctx.select_font_face("Liberation Sans", 0, 1)
ctx.set_font_size(21)
for i, nama in enumerate(["Ulangi Lantai", "Menu Utama"]):
    x = 340 + i * 310
    utama = i == 0
    ctx.set_source_rgb(*(GELAP if utama else TERANG))
    ctx.rectangle(x, 416, 290, 60)
    ctx.fill_preserve()
    ctx.set_source_rgb(*GELAP)
    ctx.stroke()
    ctx.set_source_rgb(*(TERANG if utama else GELAP))
    ctx.move_to(x + 145 - ctx.text_extents(nama).x_advance / 2, 453)
    ctx.show_text(nama)

main_folder = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
asset_folder = os.path.join(main_folder, "asset", "menu")
os.makedirs(asset_folder, exist_ok=True)
surface.write_to_png(os.path.join(asset_folder, "menu_gagal.png"))
