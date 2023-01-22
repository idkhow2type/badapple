from PIL import Image, ImageDraw

class QuadTree:
    def __init__(
        self,
        x: int,
        y: int,
        s: int,
        image: Image.Image,
        name: str,
        color_nodes: list,
        canvas: Image.Image,
        gif: list[Image.Image],
    ) -> None:
        self.x = x
        self.y = y
        self.s = s
        self.bound = (self.x, self.y, self.x + self.s, self.y + self.s)
        self.name = name
        self.image = image
        self.color = self.get_color()
        self.color_nodes = color_nodes
        self.gif = gif
        self.canvas = canvas

        if self.color == None:
            self.divide()
        else:
            self.color_nodes.append(self)
            draw = ImageDraw.Draw(self.canvas)
            # if self.color == 255:
            draw.rectangle(self.bound, fill=self.color)
            self.gif.append(self.canvas.copy())

    def get_color(self) -> int:
        image = self.image.crop(self.bound)
        data = image.getdata()
        return data[0] if all(pixel == data[0] for pixel in data) else None

    def divide(self):
        self.nw = QuadTree(
            self.x,
            self.y,
            self.s // 2,
            self.image,
            self.name + "-" + "nw",
            self.color_nodes,
            self.canvas,
            self.gif,
        )
        self.ne = QuadTree(
            self.x + self.s // 2,
            self.y,
            self.s // 2,
            self.image,
            self.name + "-" + "ne",
            self.color_nodes,
            self.canvas,
            self.gif,
        )
        self.sw = QuadTree(
            self.x,
            self.y + self.s // 2,
            self.s // 2,
            self.image,
            self.name + "-" + "sw",
            self.color_nodes,
            self.canvas,
            self.gif,
        )
        self.se = QuadTree(
            self.x + self.s // 2,
            self.y + self.s // 2,
            self.s // 2,
            self.image,
            self.name + "-" + "se",
            self.color_nodes,
            self.canvas,
            self.gif,
        )
