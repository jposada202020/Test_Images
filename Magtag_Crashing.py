import displayio
import terminalio


font = terminalio.FONT
glyph= font.get_glyph(ord('A'))
letter = displayio.TileGrid(glyph.bitmap, pixel_shader=displayio.Palette(1), default_tile=glyph.tile_index, tile_width=glyph.width, tile_height=glyph.height)
letter.transpose_xy = True
