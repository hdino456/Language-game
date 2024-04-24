from shapes import Paper, Rectangle, Oval, Triangle

paper = Paper()

rect1 = Rectangle()
tria1 = Triangle(20, 20, 400, 20, 400, 400)
oval = Oval()

rect1.set_color("blue")
rect1.set_height(100)
rect1.set_width(200)

tria1.set_color("Red")

oval.randomize()

rect1.draw()
tria1.draw()
oval.draw()

paper.display()