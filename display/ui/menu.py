import os
import cairo

GELAP = (0.157, 0.098, 0.133)
TERANG = (1.000, 0.945, 0.961)

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1280, 720)
ctx = cairo.Context(surface)

# panel
ctx.set_source_rgb(*TERANG)
ctx.rectangle(240, 70, 800, 580)
ctx.fill_preserve()
ctx.set_source_rgb(*GELAP)
ctx.set_line_width(2)
ctx.stroke()

# judul + subjudul
ctx.select_font_face("Liberation Sans", 0, 1)
teks = "MAZE RUNNER"
ctx.set_font_size(42)
ctx.set_source_rgb(*GELAP)
ctx.move_to(surface.get_width() / 2 - ctx.text_extents(teks).x_advance / 2, 148)
ctx.show_text(teks)

teks = "Temukan pintu keluar. Hindari pengejar."
ctx.set_font_size(20)
ctx.move_to(surface.get_width() / 2 - ctx.text_extents(teks).x_advance / 2, 204)
ctx.show_text(teks)

# tombol
ctx.set_font_size(21)
for i, nama in enumerate(["Mulai Main", "Rekor Terbaik", "Keluar"]):
    y = 282 + i * 84
    utama = i == 0
    ctx.set_source_rgb(*(GELAP if utama else TERANG))
    ctx.rectangle(420, y, 440, 60)
    ctx.fill_preserve()
    ctx.set_source_rgb(*GELAP)
    ctx.stroke()

    teks = nama
    ctx.set_source_rgb(*(TERANG if utama else GELAP))
    ctx.move_to(surface.get_width() / 2 - ctx.text_extents(teks).x_advance / 2, y + 37)
    ctx.show_text(teks)

main_folder = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
asset_folder = os.path.join(main_folder, "asset", "menu")
os.makedirs(asset_folder, exist_ok=True)
surface.write_to_png(os.path.join(asset_folder, "menu_utama.png"))
