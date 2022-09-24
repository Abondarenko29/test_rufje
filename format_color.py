def format_color (color, a = 0):
    def dillevnnva (czyslo):
        return czyslo / 255
    color = list(map(dillevnnva, color))
    color.append (a)
    return tuple(color)

LightBlue = format_color ((0, 255, 255))
Red = format_color ((255, 0, 0))
Blue = format_color ((0, 0, 255))
Green = format_color ((0, 170, 0))
White = format_color ((255, 255, 255))
Black = format_color ((0, 0, 0))
Yellow = format_color ((255, 255, 0))
Purple = format_color ((155, 0, 255))
Pink = format_color ((255, 0, 105))
Orange = format_color ((255, 100, 0))
Grey = format_color ((50, 50, 50))
Beige = format_color ((255, 255, 230))
Lime = format_color ((0, 255, 0))
Brown = format_color ((130, 0, 0))