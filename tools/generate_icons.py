"""Genera iconos PNG nativos para la instalación PWA (sin dependencias)."""
from pathlib import Path
import struct
import zlib

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets"

def png(path, size):
    rows = []
    radius = size * .20
    cx = cy = size / 2
    for y in range(size):
        row = bytearray([0])
        for x in range(size):
            # Fondo azul redondeado con una suave diagonal luminosa.
            dcorner = min((x*x+y*y)**.5, ((size-x)**2+y*y)**.5, (x*x+(size-y)**2)**.5, ((size-x)**2+(size-y)**2)**.5)
            a = 255 if dcorner >= radius else int(max(0, min(1, (radius-dcorner)/2)) * 255)
            t = (x + y) / (2 * size)
            r, g, b = int(9 + 26*t), int(119 + 74*t), int(207 + 28*t)
            # Globo claro.
            dx, dy = x-cx, y-(size*.47)
            globe = (dx*dx + dy*dy) ** .5
            if globe < size*.285:
                r, g, b = 146, 225, 250
                if globe > size*.262: r, g, b = 255, 255, 255
                # continentes estilizados
                if (-.20 < dx/size < .03 and -.12 < dy/size < .03) or (.02 < dx/size < .16 and -.01 < dy/size < .15): r, g, b = 58, 164, 77
            # Ruta amarilla en la base.
            if abs(y - (size*.73 - .12*(x-size*.5))) < size*.018 and size*.17 < x < size*.82:
                r, g, b = 255, 188, 54
            # Pin naranja arriba a la derecha.
            px, py = x-size*.69, y-size*.25
            if px*px + py*py < (size*.09)**2 or (abs(px) < size*.045 and 0 < py < size*.13):
                r, g, b = 248, 146, 36
            row.extend((r, g, b, a))
        rows.append(bytes(row))
    raw = b"".join(rows)
    def chunk(tag, body):
        return struct.pack(">I", len(body)) + tag + body + struct.pack(">I", zlib.crc32(tag+body)&0xffffffff)
    body = b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", size, size, 8, 6, 0, 0, 0)) + chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b"")
    path.write_bytes(body)

for pixels in (180, 192, 512):
    png(OUT / f"icon-{pixels}.png", pixels)
