import cairo
import os

UKURAN = 40      
BARIS = 18       
KOLOM = 32       
UKURAN_LANTAI = 40
TEBAL_TEMBOK = 1     

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, UKURAN * KOLOM, UKURAN * BARIS)
ctx = cairo.Context(surface)


def gambar_tembok(ctx):
    
    
    ctx.rectangle(0, 0, UKURAN, UKURAN)
    ctx.clip()

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


def gambar_lantai(ctx, ukuran):
    
    ctx.rectangle(0, 0, ukuran, ukuran)
    ctx.clip()

    # isinya lantai: pink agak putihan dikit
    ctx.set_source_rgb(1.000, 0.776, 0.851)
    ctx.paint()

    # sisi atas & kirinya: agak lebih terang
    ctx.set_source_rgb(1.000, 0.855, 0.906)
    ctx.move_to(0, 1)
    ctx.line_to(ukuran, 1)
    ctx.stroke()

    ctx.set_source_rgb(1.000, 0.855, 0.906)
    ctx.move_to(1, 0)
    ctx.line_to(1, ukuran)
    ctx.stroke()

    # ini yang sisi bawah sama kanan: sedikit lebih gelappp (garis antar kotak)
    ctx.set_source_rgb(1.000, 0.675, 0.784)
    ctx.move_to(0, ukuran - 1)
    ctx.line_to(ukuran, ukuran - 1)
    ctx.stroke()

    ctx.set_source_rgb(1.000, 0.675, 0.784)
    ctx.move_to(ukuran - 1, 0)
    ctx.line_to(ukuran - 1, ukuran)
    ctx.stroke()


# ini lantai: isi bagian tengahnya 
area_x = TEBAL_TEMBOK * UKURAN
area_y = TEBAL_TEMBOK * UKURAN
area_lebar = (KOLOM - 2 * TEBAL_TEMBOK) * UKURAN
area_tinggi = (BARIS - 2 * TEBAL_TEMBOK) * UKURAN

ctx.save()
ctx.rectangle(area_x, area_y, area_lebar, area_tinggi)
ctx.clip()   
for y in range(area_y, area_y + area_tinggi, UKURAN_LANTAI):
    for x in range(area_x, area_x + area_lebar, UKURAN_LANTAI):
        ctx.save()
        ctx.translate(x, y)
        gambar_lantai(ctx, UKURAN_LANTAI)
        ctx.restore()
ctx.restore()

# ini tembok: di pinggir (atas, bawah, kiri, kanan), tebalnya TEBAL_TEMBOK tile
for kolom in range(KOLOM):
    for baris in range(BARIS):
        di_pinggir = (
            baris < TEBAL_TEMBOK or baris >= BARIS - TEBAL_TEMBOK or
            kolom < TEBAL_TEMBOK or kolom >= KOLOM - TEBAL_TEMBOK
        )
        if not di_pinggir:
            continue

        ctx.save()
        ctx.translate(kolom * UKURAN, baris * UKURAN)   # geser ke kanan & ke bawah
        gambar_tembok(ctx)
        ctx.restore()



surface.write_to_png("tembokcoba.png")
main_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
asset_folder = os.path.join(main_folder, "asset")
os.makedirs(asset_folder, exist_ok=True)
surface.write_to_png(os.path.join(asset_folder, "tembok.png"))
print("Hytam")