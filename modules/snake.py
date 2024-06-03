from turtle import Turtle
MOVE_DISTANCE = 20
# TURN_DEGREES = 90
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.x_axis = 0
        self.y_axis = 0
        self.starting_positions = []
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for snake_index in range(0, 3):
            point_instance = (self.x_axis, self.y_axis)
            self.starting_positions.append(point_instance)
            self.add_segment(point_instance)
            self.x_axis -= 20

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.up()
        point_instance = (self.x_axis, self.y_axis)
        new_segment.goto(point_instance)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):  # (start, stop, step)
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        # self.head.left(TURN_DEGREES)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
