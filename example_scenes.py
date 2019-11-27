#!/usr/bin/env python

from manimlib.imports import *

# To watch one of these scenes, run the following:
# python -m manim example_scenes.py SquareToCircle -pl
#
# Use the flat -l for a faster rendering at a lower
# quality.
# Use -s to skip to the end and just save the final frame
# Use the -p to have the animation (or image, if -s was
# used) pop up once done.
# Use -n <number> to skip ahead to the n'th animation of a scene.
# Use -r <number> to specify a resolution (for example, -r 1080
# for a 1920x1080 video)


class OpeningManimExample(Scene):
    def construct(self):
        title = TextMobject("This is some \\LaTeX")
        basel = TexMobject(
            "\\sum_{n=1}^\\infty "
            "\\frac{1}{n^2} = \\frac{\\pi^2}{6}"
        )
        VGroup(title, basel).arrange(DOWN)
        self.play(
            Write(title),
            FadeInFrom(basel, UP),
        )
        self.wait()

        transform_title = TextMobject("That was a transform")
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
            LaggedStart(*map(FadeOutAndShiftDown, basel)),
        )
        self.wait()

        grid = NumberPlane()
        grid_title = TextMobject("This is a grid")
        grid_title.scale(1.5)
        grid_title.move_to(transform_title)

        self.add(grid, grid_title)  # Make sure title is on top of grid
        self.play(
            FadeOut(title),
            FadeInFromDown(grid_title),
            ShowCreation(grid, run_time=3, lag_ratio=0.1),
        )
        self.wait()

        grid_transform_title = TextMobject(
            "That was a non-linear function \\\\"
            "applied to the grid"
        )
        grid_transform_title.move_to(grid_title, UL)
        grid.prepare_for_nonlinear_transform()
        self.play(
            grid.apply_function,
            lambda p: p + np.array([
                np.sin(p[1]),
                np.sin(p[0]),
                0,
            ]),
            run_time=3,
        )
        self.wait()
        self.play(
            Transform(grid_title, grid_transform_title)
        )
        self.wait()


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(ShowCreation(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))


class WarpSquare(Scene):
    def construct(self):
        square = Square()
        self.play(ApplyPointwiseFunction(
            lambda point: complex_to_R3(np.exp(R3_to_complex(point))),
            square
        ))
        self.wait()


class WriteStuff(Scene):
    def construct(self):
        example_text = TextMobject(
            "This is a some text",
            tex_to_color_map={"text": YELLOW}
        )
        example_tex = TexMobject(
            "\\sum_{k=1}^\\infty {1 \\over k^2} = {\\pi^2 \\over 6}",
        )
        group = VGroup(example_text, example_tex)
        group.arrange(DOWN)
        group.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)

        self.play(Write(example_text))
        self.play(Write(example_tex))
        self.wait()


class UpdatersExample(Scene):
    def construct(self):
        decimal = DecimalNumber(
            0,
            show_ellipsis=True,
            num_decimal_places=3,
            include_sign=True,
        )
        square = Square().to_edge(UP)

        decimal.add_updater(lambda d: d.next_to(square, RIGHT))
        decimal.add_updater(lambda d: d.set_value(square.get_center()[1]))
        self.add(square, decimal)
        self.play(
            square.to_edge, DOWN,
            #rate_func=there_and_back,
            rate_func=linear,
            run_time=5,
        )
        self.wait()

# See old_projects folder for many, many more

class Shapes(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        line = Line(np.array([-5,0,0]), np.array([5,0,0]))
        triangle = Polygon(np.array([0,0,0]),np.array([1,1,0]), np.array([1,-1,0]))

        self.play(ShowCreation(circle))
        self.play(FadeOut(circle))
        self.play(GrowFromCenter(square))
        self.play(Transform(square, triangle)) 
        self.add(line)
        self.wait()
        self.remove(line)
        self.wait()
        self.remove(square)
        self.wait()

class MoreShapes(Scene):
    def construct(self):
        circle = Circle(color=PURPLE_A)
        square = Square(fill_color=GOLD_B, fill_opacity = 1, color = GOLD_A)
        square.move_to(UP+LEFT)
        circle.surround(square)
        rectangle = Rectangle(height=2, width = 3)
        ellipse = Ellipse(width=3, height=1, color=RED)
        ellipse.shift(2*DOWN+2*RIGHT)
        pointer = CurvedArrow(2*RIGHT,5*RIGHT,color=MAROON_C)
        arrow = Arrow(RIGHT, UP)
        arrow.next_to(circle, DOWN+LEFT)
        rectangle.next_to(arrow, DOWN+LEFT)
        ring = Annulus(inner_radius=.5, outer_radius=1, color=BLUE)
        ring.next_to(ellipse, RIGHT)

        self.add(pointer)
        self.play(FadeIn(square))
        self.play(Rotating(square), FadeIn(circle))
        self.play(GrowArrow(arrow))
        self.play(GrowFromCenter(rectangle), GrowFromCenter(ellipse), GrowFromCenter(ring))

class AddingText(Scene):
    def construct(self):
        my_first_text=TextMobject("Writing with manim is fun")
        second_line = TextMobject("and easy to to!")
        second_line.next_to(my_first_text, DOWN)
        third_line=TextMobject("for me and you!")
        third_line.next_to(my_first_text, DOWN)
        
        self.add(my_first_text, second_line)
        self.wait(2)
        self.play(Transform(second_line, third_line))
        self.wait(2)
        second_line.shift(3*DOWN)
        self.play(ApplyMethod(my_first_text.shift, 3*UP))

class AddingMoreText(Scene):
    def construct(self):
        quote = TextMobject("Imagination is more important than knowledge")
        quote.set_color(RED)
        quote.to_edge(UP)
        quote2 = TextMobject("A person who never made a mistake never tried anything new")
        quote2.set_color(YELLOW)
        author=TextMobject("Albert Einstein")
        author.scale(0.75)
        author.next_to(quote.get_corner(DR), DOWN)
        quote2.to_edge(DOWN)

        self.add(quote)
        self.add(author)
        self.wait(2)
        self.play(Transform(quote, quote2), ApplyMethod(author.move_to, quote2.get_corner(DR)+DOWN+2*LEFT))

        self.play(ApplyMethod(author.scale, 1.5))
        author.match_color(quote2)
        self.play(FadeOut(quote))

class RotateAndHighlight(Scene):
    def construct(self):
        square=Square(side_length = 5, fill_color=YELLOW, fill_opacity=1)
        square.rotate(TAU/8)
        label=TextMobject("Text at an angle")
        label.bg=BackgroundRectangle(label, fill_opacity=.5)
        label_group=VGroup(label.bg,label)
        label_group.rotate(TAU/8)
        label2=TextMobject("Boxed text", color=BLACK)
        label2.bg=SurroundingRectangle(label2, color=BLUE, fill_color=RED, fill_opacity=.5)
        label2_group=VGroup(label2, label2.bg)
        label2_group.next_to(label_group, DOWN)
        label3=TextMobject("Rainbow")
        label3.scale(2)
        label3.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        label3.to_edge(DL)

        self.add(square)
        self.play(FadeIn(label_group))
        self.play(FadeIn(label2_group))
        self.play(FadeIn(label3))

class BasicEquations(Scene):
    def construct(self):
        eq1=TextMobject("$\\vec{X}_0 \\cdot \\vec{Y}_1 = 3$")
        eq1.shift(2*UP)
        eq2=TexMobject(r"\vec{F}_{net} = \sum_i \vec{F}_i")
        eq2.shift(2*DOWN)

        self.play(Write(eq1))
        self.play(Write(eq2))

class ColoringEquations(Scene):
    def construct(self):
        line1=TexMobject(r"\text{The vector } \vec{F}_{net} \text{ is the net }", r"\text{force }", r"\text{on object of mass }")
        line1.set_color_by_tex("is the net force on object of mass", BLUE)
        line2=TexMobject("m", "\\text{ and acceleration }", "\\vec{a}", ". ")
        line2.set_color_by_tex_to_color_map({
            "m": YELLOW,
            "{a}": RED
        })
        sentence=VGroup(line1, line2)
        sentence.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        self.play(Write(sentence))

class UsingBraces(Scene):
    def construct(self):
        eq1A = TextMobject("4x + 3y")
        eq1B = TextMobject("=")
        eq1C = TextMobject("0")
        eq2A = TextMobject("5x - 2y")
        eq2B = TextMobject("=")
        eq2C = TextMobject("3")
        eq1B.next_to(eq1A,RIGHT)
        eq1C.next_to(eq1B,RIGHT)
        eq2A.shift(DOWN)
        eq2B.shift(DOWN)
        eq2C.shift(DOWN)
        eq2A.align_to(eq1A,LEFT)
        eq2B.align_to(eq1B,LEFT)
        eq2C.align_to(eq1C,LEFT)

        eq_group = VGroup(eq1A, eq2A)
        braces = Brace(eq_group, LEFT)
        eq_text = braces.get_text("A pair of equations")

        self.add(eq1A, eq1B, eq1C)
        self.add(eq2A, eq2B, eq2C)
        self.play(GrowFromCenter(braces), Write(eq_text))

class UsingBracesConcise(Scene):
    def construct(self):
        eq1_text=["4","x","+","3","y","=","0"]
        eq2_text=["5","x","-","2","y","=","3"]
        eq1_mob=TexMobject(*eq1_text)
        eq2_mob=TexMobject(*eq2_text)
        eq1_mob.set_color_by_tex_to_color_map({
            "x":RED_B,
            "y":GREEN_C
            })
        eq2_mob.set_color_by_tex_to_color_map({
            "x":RED_B,
            "y":GREEN_C
            })
        for i,item in enumerate(eq2_mob):
            item.align_to(eq1_mob[i],LEFT)
        eq1=VGroup(*eq1_mob)
        eq2=VGroup(*eq2_mob)
        eq2.shift(DOWN)
        eq_group=VGroup(eq1,eq2)
        braces=Brace(eq_group,LEFT)
        eq_text = braces.get_text("A pair of equations")

        self.play(Write(eq1), Write(eq2))
        self.play(GrowFromCenter(braces), Write(eq_text))

class PlotFunctions(GraphScene):
    CONFIG = {
        "x_min" : -10,
        "x_max" : 10.3,
        "y_min" : -1.5,
        "y_max" : 1.5,
        "graph_origin" : ORIGIN ,
        "function_color" : RED ,
        "axes_color" : GREEN,
        "x_labeled_nums" :range(-10,12,2),
    }   

    def construct(self):
        self.setup_axes(animate = True)
        func_graph = self.get_graph(self.func_to_graph, self.function_color)
        func_graph2 = self.get_graph(self.func_to_graph2)
        vert_line = self.get_vertical_line_to_graph(TAU, func_graph, color = YELLOW)
        graph_lab = self.get_graph_label(func_graph, label = "\\cos(x)")
        graph_lab2 = self.get_graph_label(func_graph2, label = "\\sin(x)", x_val= -10, direction = UP/2)
        two_pi = TexMobject("x = 2 \\pi")
        label_coord = self.input_to_graph_point(TAU, func_graph)
        two_pi.next_to(label_coord, RIGHT + UP)

        self.play(ShowCreation(func_graph), ShowCreation(func_graph2))
        self.play(ShowCreation(vert_line), ShowCreation(graph_lab), ShowCreation(graph_lab2), ShowCreation(two_pi))

    def func_to_graph(self, x):
        return np.cos(x)

    def func_to_graph2(self, x):
        return np.sin(x)

class nDistribution(GraphScene):
    CONFIG = {
        "y_max" : 0.5,
        "y_min" : 0,
        "x_min" : -5,
        "x_max" : 5,
        "y_tick_frequency": 0.1,
        #"graph_origin": 3*RIGHT + 0.5*UP,
        "graph_origin" : [2, -1, 0],
        "x_axis_width": 10,
        "y_axis_height" : 2,
        "x_labeled_nums": [-5, -4, -3, -2, -1, 1, 0, 1, 2, 3, 4, 5],
        "num_rects": 100,
    }
    def construct(self):
        
        self.setup_axes(animate = True)
        func_graph = self.get_graph(self.func_to_graph)
        func_graph_2 = self.get_graph(self.func_to_graph_2)
        #graph_lab = self.get_graph_label(func_graph, label = "\\cos(x)")
        #riemann = self.get_riemann_rectangles(func_graph)
        area = self.get_area(func_graph, 0, 1)
        text1 = TextMobject("Distribución Normal")
        
        eq1 = TexMobject(
            r"X \sim N(\mu, \sigma) ",
        )
        eq1.shift(2*LEFT+3*UP)
        text1.shift(3*UP)

        self.play(ShowCreation(text1))
        self.wait(3)
        self.remove(text1)
        self.play(ShowCreation(func_graph))
        self.add(eq1)
        self.wait(2)
        self.play(ShowCreation(area))
        self.play(Transform(func_graph, func_graph_2))


    def func_to_graph(self, x):
        return norm.pdf(x, 0, 1)
    def func_to_graph_2(self, x):
        return norm.pdf(x, 0, 2)    
    
class normalDistribution(Scene):
    def construct(self):
        x_line = NumberLine()
        self.add(x_line)
        self.play