# Label Library

The label library allows us to publish certain 
text into a display. There are different label 
parameters that allow us to set up the font, 
position, background characteristics among others.

A Label is an artifact of an organized set of 
tilegrids.

There are two types of labels. The standard one
and the bitmap_label. The bitmap_label will allow you ta save
a little bit of memory.

## Label position

There are different ways to set up the label 
position in the display. This includes:
- x, y coordinates
- Anchor point
- Anchor position coordinates


### x, y coordinates

x, y  coordinates allows to define the label 
position. When setting text location using 
the x and y properties, you are setting the 
origin point. It is located relative to the 
text as shown below.


![](https://cdn-learn.adafruit.com/assets/assets/000/075/027/original/circuitpython_text_origin.png?1556377258)


### Anchor Points
The anchor_point property of the 
label is a (x, y) tuple. The values 
range from 0 to 1 with x being the horizontal 
and y being the vertical. The origin is in 
the upper left corner. A value of 0 is at 
the origin. A value of 1 is all the way to 
the right/down.

![](https://cdn-learn.adafruit.com/assets/assets/000/088/115/original/adabox_text_bound.png?1580936146)


### Anchor Position
The label position on the display could be 
located using the anchored_position property. 
The values are actual screen coordinates 
in pixels and defined by a tuple 
representing (x, y) coordinates

![](https://cdn-learn.adafruit.com/assets/assets/000/088/116/original/adabox_heart_labels.png?1580936428)

 

## TileGrid Position
When you create a text label, the library 
will create an imaginary box that encloses 
all the glyphs in the text. All the glyphs 
present within the text will be located inside 
this box.
This box is calculated inside the library 
taking into account the glyphs ascent and 
descent values in a particular text.
When no text is provided the library will use
the characters "M j ' " to calculate the 
boundingbox. This limits of the bounding box will 
define the background applied to the text.


### Ascend
Is a value in pixels of the upper portion 
that extends from the median of a particular 
glyph

![](https://upload.wikimedia.org/wikipedia/commons/e/e3/Typographic_ascenders.png)


### Descend
Is a value in pixels of the bottom portion 
that extends from the median of a particular 
glyph

![](https://upload.wikimedia.org/wikipedia/commons/6/6f/Descender.png)


# Adavanced text positioning
Label text positioning is calculated inside 
the private function

```def _update_text()```

Positioning in the y-axis is calculated as 
follows:

```position_y = y - glyph.height - glyph.dy + y_offset```

* glyph.height: glyph height value
* glyph.dy: glyph distance in the y axe from 
  the glyph origin
* y_offset: Bounding box middle point. This is 
calculated with the Label library function ```def _get_ascent_descent```

## Label Background
Label background is an imaginary box that enclose
the label. We can define the color and size of this box
to create different cool effects.
This library allows defining different characteristics
for the label background:
* ```background_tight```
* ```padding_top (bottom|left|right)```

### Background tight
When we declare ```background_tight``` as ```True```
 the background box will correspond exactly to the label boundingbox
When ```False``` the ascent and descent will be added to 
the boundingbox dimensions. When False, the limits of each limit 
top/bottom/left/right
could be defined with the padding parameter.

### Padding
Value in pixels of the background shift to the boundingbox
dimensions values.

### Scale
When you need your font bigger you could setup this parameter to scale
the label. This value only takes integers.

### Base_Alignment
When defined to true, this parameters will align the label
to the base line. This could be helpful with you are working with
different fonts type or font sizes and you want them to to be aligned at
a certain position.

## Other Topics
### Builtin Font
When a font is not specified in Label parameters,
CircuitPython uses the default font builtin. This
is included in the core libraries terminalio and fontio. 

    import fontio
    from adafruit_display_text import label
    
    display = board.DISPLAY
    main_group = displayio.Group()
    
    text = "CircuitPython"
    text_area = label.Label(fontio.BuiltinFont(), text=text, color=0x0000FF, background_color=0xFFAA00)

### Optimize Font File Size (Manually)
You could use a text editor to remove glyphs 
from a .bdf file. BDF files are just text!

Open a BDF file and search for “asciitilde” — 
this is usually the highest plain-ASCII-value 
glyph we want to preserve. A few lines down 
there will be an “ENDCHAR” line.

Delete everything after the ENDCHAR line, then 
add a line containing ENDFONT. That’s it! Save 
the file, which is usually just a small fraction
of the original size.

![](https://cdn-learn.adafruit.com/assets/assets/000/097/160/original/circuitpython_fontforge-edit.png?1605820922)

You won’t get any accented characters or special
punctuation this way, so it’s not always the 
right thing for every situation. For the 
majority of plain-text programs though, this 
can really help stretch your CIRCUITPY drive 
space!

### CAVEATS
Some fonts does not include all the characters. So be sure
that the font used includes the characters needed.