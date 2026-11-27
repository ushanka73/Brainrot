import cairo
import os

UKURAN = 40      

PETA = [
    "################################",
    "#D00000#0000000#0000000#0000000#",
    "#0####0#0#####0#0#####0#0#####0#",
    "#0#0000#0#00000#00000#000#00000#",
    "#0#0####0#0#########0#####0###0#",
    "#0#000000#00000#00000#00000#000#",
    "#0######0#####0#0###0#0#####0#0#",
    "#000000#00000#000#000#0#00000#0#",
    "######0#####0#####0###0#0#####0#",
    "#000000#000#0000000#000#00000#0#",
    "#0######0#0#######0#0#######0#0#",
    "#00000000#00000H0#0#0000000#000#",
    "#0########0#####0#0#######0###0#",
    "#0#00000000#00000#00000#0#00000#",
    "#0#0########0#########0#0#####0#",
    "#0#0000000#0000000B0000#0000000#",
    "#000#####000#####000####0#####0#",
    "##############################E#",
]


BARIS = len(PETA)
KOLOM = len(PETA[0])


for nomor, baris_peta in enumerate(PETA, start=1):
    if len(baris_peta) != KOLOM:
        raise ValueError(
            f"Baris ke-{nomor} panjangnya {len(baris_peta)}, harusnya {KOLOM}"
        )

LANTAI_A = ((1.000, 0.953, 0.839), (1.000, 0.976, 0.919), (0.840, 0.801, 0.705))   #
LANTAI_B = ((0.949, 0.839, 0.667), (0.974, 0.919, 0.834), (0.797, 0.705, 0.560))   

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


def gambar_lantai(ctx, ukuran, warna):
    isi, terang, gelap = warna

    ctx.rectangle(0, 0, ukuran, ukuran)
    ctx.clip()

    # isinya lantai
    ctx.set_source_rgb(*isi)
    ctx.paint()

    # sisi atas & kirinya: agak lebih terang
    ctx.set_source_rgb(*terang)
    ctx.move_to(0, 1)
    ctx.line_to(ukuran, 1)
    ctx.stroke()

    ctx.set_source_rgb(*terang)
    ctx.move_to(1, 0)
    ctx.line_to(1, ukuran)
    ctx.stroke()

    # sisi bawah sama kanan: sedikit lebih gelap (garis antar kotak)
    ctx.set_source_rgb(*gelap)
    ctx.move_to(0, ukuran - 1)
    ctx.line_to(ukuran, ukuran - 1)
    ctx.stroke()

    ctx.set_source_rgb(*gelap)
    ctx.move_to(ukuran - 1, 0)
    ctx.line_to(ukuran - 1, ukuran)
    ctx.stroke()



for baris in range(BARIS):
    for kolom in range(KOLOM):
        karakter = PETA[baris][kolom]

        ctx.save()
        ctx.translate(kolom * UKURAN, baris * UKURAN)   # geser ke kotak yang dituju

        if karakter == "#":
            gambar_tembok(ctx)
        else:
            
            warna = LANTAI_A if (kolom + baris) % 2 == 0 else LANTAI_B
            gambar_lantai(ctx, UKURAN, warna)

        ctx.restore()


surface.write_to_png("labirin1.png")
main_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
asset_folder = os.path.join(main_folder, "asset")
os.makedirs(asset_folder, exist_ok=True)
surface.write_to_png(os.path.join(asset_folder, "labirin1.png"))
print("Hytam")