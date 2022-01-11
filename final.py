
from manim import *

class Introduction(Scene):
    def construct(self):
        font = "Calibri"
        authors = Text ("P.T. Shattuck et al.",font_size=30,font = font, color=BLUE)
        Journal = Text ("Pediatrics, vol. 126(6), 2012\nAmerican Academy Of Pediatrics",
                        font = font,font_size=30,color=BLUE)
        text1 = Text("Post-Secondary Education and Employment".upper(),font = font,font_size=45, weight=BOLD)
        text2 = Text("Among Youth With an".upper(),font = font,font_size=38, weight=BOLD)
        text3 = Text("Autism Spectrum Disorder".upper(),font = font,font_size=45, weight=BOLD)

        Title = VGroup(authors,text1,text2,text3, Journal).arrange(DOWN, buff=MED_LARGE_BUFF)
        [self.play(Write(t),run_time=0.8) for t in Title[1:4]]
        self.play(Write(Title[0]),Write(Title[4]))
        self.wait(2)
        self.play(FadeOut(Title),FadeOut(Journal),FadeOut(authors))

        # Create Decimal Number and add it to scene
        number = DecimalNumber().set_color(RED).scale(5).shift(LEFT)
        # Add an updater to keep the DecimalNumber centered as its value changes
        #number.add_updater(lambda number: number.move_to(ORIGIN))
        self.addmob = Text('%', color=WHITE).next_to(number, RIGHT, buff=0.5)


        arrows = [Arrow(ORIGIN, 2.3 * LEFT),
                 Arrow(ORIGIN, UL ),
                 Arrow(ORIGIN, 1.5*DL ),
                 Arrow(ORIGIN, 2.5*UR ),
                 Arrow(ORIGIN,1.4*RIGHT ),
                 Arrow(ORIGIN, DR*2.1 )]
        e1=Text("Social Skills",font_size=20,color=BLUE).next_to(arrows[0],LEFT,buff=0.5)
        e2=Text("Communication Skills",font_size=20,color=RED).next_to(arrows[3],UP+RIGHT,buff=0.5)
        e3=Text("Emotion Regulation",font_size=20,color = GREEN).next_to(arrows[5],DOWN+RIGHT,buff=0.5)
        e = VGroup(e1,e2,e3)
        DD=Dot(point=ORIGIN,color=BLUE)
        self.play(Create(DD))
        for i in range(6):
            self.play(GrowArrow(arrows[i]),run_time=0.3)
        self.play(Write(e))
        self.wait(2)
        for i in range(6):
            self.play(FadeOut(arrows[i]),run_time=0.1)
        self.play(FadeOut(e))
        self.play(FadeOut(DD))
        self.wait(2)

        self.add(number)
        

        self.wait()

        # Play the Count Animation to count from 0 to 100 in 4 seconds
        
        self.play(Count(number, 0, 80), run_time=4, rate_func=linear)
        p= Text('%', color=WHITE,font_size=85).next_to(number, RIGHT, buff=0.5)
        self.play(Write(p))
        self.wait()
        self.play(number.animate.shift(UP),p.animate.shift(UP))
        tt1 = Text("Either Unemployed", font_size=40, color=BLUE)
        tt2 = Text("or",font_size=40)
        tt3 = Text("Under-Employed (phD Janitor)",font_size=40, color=BLUE)
        ttt = VGroup(tt1,tt2,tt3).arrange(DOWN, buff=MED_LARGE_BUFF).next_to(number,DOWN)
        self.play(Write(ttt),run_time=0.5)
        self.wait(2)
        self.play(FadeOut(ttt))
        self.play(FadeOut(p))
        self.play(FadeOut(number))

        aim = Text("Aim of Study:",font_size=45,color=BLUE).shift(UP)
        a1 = Text("1. Comparison with other Disability Groups\n\n2. Identify subsets of youth at particularly high risk\n\n3. Help clinicians and policy makers to make better plans",font_size=35)
        aa= VGroup(aim,a1).arrange(DOWN, buff=MED_LARGE_BUFF)
        self.play(Write(aa))
        self.wait(5)
        self.play(FadeOut(aa))
        self.wait(2)
        font = "Calibri"
        formula1 = Tex(r"$\frac{P(Employment|Disability)}{1-P(Employment|Disability)}$")
        formula2 = Tex(r"$=$")
        formula3 = Tex(r"$e^{\beta_0 + \beta_1 x_1+ \beta_2 x_2+\beta_3 x_3}$")
        formula = VGroup(formula1,formula2,formula3).arrange(DOWN, buff=MED_LARGE_BUFF)
        formula.shift(LEFT*4)
        data = Table(
            [[" ethnicity,\n gender,\n race,\n guardian’s income,\n number of years passed\n since leaving high school,\n health,\n motor and conversation skills,\n and functional independence",
             " education,\n\n paid employment,\n\n both of them\n\n no participation\n in any of these"]],
            col_labels=[Text("Predictors"), Text("Outomes")]).scale(0.5)
        
        
        data.add_highlighted_cell((1,1),color=BLUE)
        data.add_highlighted_cell((1,2),color=RED)
        self.play(Create(data))
        self.wait(5)
        self.play(FadeOut(data))
        self.wait(2)

        t0 = Table(
            [["1","0","0"],["0","1","0"],["0","0","1"],["0","0","0"]],
            row_labels=[Text('Autism'),
                        Text("Speech/Language Impairment"),
                        Text('Intellectual Disability'),
                        Text("Learning Disability")],
            col_labels=[Tex("$x_1$"),Tex("$x_2$"),Tex("$x_3$")],
            top_left_entry=Text("Disability Groups")).scale(0.6)

        t2 = Table(
            [["1","0","0","1","0"],["0","1","0","0","1"],
            ["0","0","1","1","1"],["0","0","0","1","0"]],
            row_labels=[Text('1'),
                        Text("2"),
                        Text('3'),
                        Text("4")],
            col_labels=[Tex("$x_1$"),Tex("$x_2$"),Tex("$x_3$"),
                        Text("Employment"),Text("Education")],
            top_left_entry=Text("Example No.")).scale(0.6)

        t3 = Table(
            [["1","0","0","1","0"],["0","1","0","0","1"],
            ["0","1","0","1","1"],["0","1","0","1","0"],
            ["0","0","1","0","0"],["0","0","0","1","0"],
            ["0","1","0","1","1"],[":",":",":",":",":"]],
            row_labels=[Text('1'),Text("2"),Text('3'),
                        Text("4"),Text("5"),Text("6"),Text("7"),Text(":")],
            col_labels=[Tex("$x_1$"),Tex("$x_2$"),Tex("$x_3$"),
                        Text("Employment"),Text("Education")],
            top_left_entry=Text("Example No.")).scale(0.6)

        t5 = Table(
            [["1","0","0","1","0"],["0","1","0","1","1"],
            ["0","1","0","1","1"],["0","1","0","1","0"],
            ["0","0","1","0","0"],["0","0","0","1","0"],
            ["0","1","0","1","1"],[":",":",":",":",":"]],
            row_labels=[Text('1'),Text("2"),Text('3'),
                        Text("4"),Text("5"),Text("6"),Text("7"),Text(":")],
            col_labels=[Tex("$x_1$"),Tex("$x_2$"),Tex("$x_3$"),
                        Text("Employment"),Text("Education")],
            top_left_entry=Text("Example No.")).scale(0.6)

        for i in range(1,10):
            for j in range(2,6):
                t5.add_highlighted_cell((i,j), color=BLUE)
        for i in range(1,10):
            t5.add_highlighted_cell((i,5), color=GREEN)

        t4 = Table(
            [["1","0","0","1"],["0","1","0","1"],
            ["0","1","0","0"],["0","1","0","1"],
            ["0","0","1","0"],["0","0","0","0"],
            ["0","1","0","1"],[":",":",":",":"]],
            col_labels=[Tex("$x_1$"),Tex("$x_2$"),Tex("$x_3$"),
                        Text("Employment")],
            ).scale(0.6)



        self.play(t0.create())
        self.wait(5)
        self.play(Transform(t0,t2))
        self.wait(5)
        self.play(t0.animate.shift(UP))
        self.play(FadeTransform(t0,t3))
        self.play(FadeTransform(t3,t5))
        self.wait(4)
        self.play(FadeTransform(t5,t3))
        self.wait(2)
        self.play(FadeTransform(t3,t4))
        #self.play(ScaleInPlace(t4,0.5))
        self.play(t4.animate.shift(RIGHT*4))
        self.play(Write(formula))
        #framebox1 = SurroundingRectangle(t4.get_rows()[1])
        #
        dot = Dot(LEFT*4)
        self.wait(3)
        self.play(t4.animate.scale(0.4))
        self.play(FadeOut(t4,target_position = dot))

        formula4 = Tex(r"$\frac{P(Employment|Disability)}{1-P(Employment|Disability)}$")
        formula5 = Tex(r"$=$")
        formula6 = Tex(r"$e^{\beta_0 + \beta_1 x_1+ \beta_2 x_2+\beta_3 x_3}$")
        newformula = VGroup(formula4,formula5,formula6).arrange(RIGHT, buff=MED_LARGE_BUFF)
        self.play(Transform(formula,newformula))
        # self.play(FadeOut(formula))
        # self.play(FadeIn(newformula))
        framebox1 = SurroundingRectangle(newformula[0])
        self.play(Create(framebox1))
        self.wait(5)
        self.play(Uncreate(framebox1))
        self.play(Unwrite(formula))
        r = Table(
            [["Predictors", "College Education", "Employment", "None"],
            ["Male", "3", "1.2", "0.6"],
            ["Female","0.7", "1.3", "1"],
            ["Hispanic","0.5", "0.5", "2.7"],
            ["Little Trouble\nin Conversation" ,"1.2", "0.8", "1.2"],
            ["No Conversation\n    at all","0.3", "0.5", "1.7"]],
            include_outer_lines=True).scale(0.5)
        r.get_horizontal_lines()[:3].set_color(BLUE)
        r.get_vertical_lines()[:3].set_color(BLUE)
        r.get_horizontal_lines()[:3].set_z_index(1)

        c1 = Text("Autism",color=RED)
        c2 = Text(">")
        c3 = Text("Other Disability Groups")
        c = VGroup(c1,c2,c3).arrange(RIGHT,buff=MED_LARGE_BUFF)
        self.wait(2)
        self.play(Write(c))
        self.play(ScaleInPlace(c1,2),ScaleInPlace(c3,0.8),c2.animate.shift(RIGHT))
        self.wait(3)
        self.play(Unwrite(c))


        self.play(Create(r))
        self.wait(5)
        self.play(Uncreate(r))
        r.add_highlighted_cell((1,1), color=BLUE)
        self.wait(1)

        d1 = Dot(point=(UP*2+RIGHT),color='#bc5090')
        d2 = Dot(color = '#ff6361').next_to(d1,DOWN,buff=0.1)
        i1 = Text("income < $25 k",font_size=15).next_to(d1,RIGHT,buff=0.1)
        i2 = Text("income > $75 k",font_size=15).next_to(d2,RIGHT,buff=0.1)



        vals = [79, 45, 13, 3]
        colors = ['#bc5090', '#ff6361', '#bc5090', '#ff6361']
        bar = BarChart(
            vals,
            max_value=100,
            bar_colors=colors,
            bar_label_scale_val=1,
            label_y_axis=True
        )
        self.play(GrowFromEdge(bar, DOWN))
        xlab = Text("low functioning                  high functionaing",font_size=20).next_to(bar,DOWN)
        ylabel = Text("       Rates of\nno particiation",font_size=20).next_to(bar,LEFT)
        self.play(Write(xlab),Write(ylabel),Create(d1),Create(i2),Create(i1),Create(d2))
        self.wait(5)

#class Analysis(Scene):
    def construct(self):
        font = "Calibri"
        formula1 = Tex(r"$\frac{P(Employment|Disability)}{1-P(Employment|Disability)}$")
        formula2 = Tex(r"$=$")
        formula3 = Tex(r"$e^{\beta_0 + \beta_1 x_1+ \beta_2 x_2+\beta_3 x_3}$")
        formula = VGroup(formula1,formula2,formula3).arrange(DOWN, buff=MED_LARGE_BUFF)
        formula.shift(LEFT*4)
        data = Table(
            [[" ethnicity,\n gender,\n race,\n guardian’s income,\n number of years passed\n since leaving high school,\n health,\n motor and conversation skills,\n and functional independence",
             " education,\n paid employment,\n both of them\n no participation\n in any of these"]],
            col_labels=[Text("Predictors"), Text("Outomes")]).scale(0.5)
        
        
        data.add_highlighted_cell((1,1),color=BLUE)
        data.add_highlighted_cell((1,2),color=RED)
        self.play(Create(data))
        self.wait(5)
        self.play(FadeOut(data))
        self.wait(2)

        t0 = Table(
            [["1","0","0"],["0","1","0"],["0","0","1"],["0","0","0"]],
            row_labels=[Text('Autism'),
                        Text("Speech/Language Impairment"),
                        Text('Intellectual Disability'),
                        Text("Learning Disability")],
            col_labels=[Tex("$x_1$"),Tex("$x_2$"),Tex("$x_3$")],
            top_left_entry=Text("Disability Groups")).scale(0.6)

        t2 = Table(
            [["1","0","0","1","0"],["0","1","0","1","0"],
            ["0","0","1","1","0"],["0","0","0","1","0"]],
            row_labels=[Text('1'),
                        Text("2"),
                        Text('3'),
                        Text("4")],
            col_labels=[Tex("$x_1$"),Tex("$x_2$"),Tex("$x_3$"),
                        Text("Employment"),Text("Education")],
            top_left_entry=Text("Example No.")).scale(0.6)

        t3 = Table(
            [["1","0","0","1","0"],["0","1","0","1","0"],
            ["0","1","0","1","0"],["0","1","0","1","0"],
            ["0","0","1","1","0"],["0","0","0","1","0"],
            ["0","1","0","1","0"],[":",":",":",":",":"]],
            row_labels=[Text('1'),Text("2"),Text('3'),
                        Text("4"),Text("5"),Text("6"),Text("7"),Text(":")],
            col_labels=[Tex("$x_1$"),Tex("$x_2$"),Tex("$x_3$"),
                        Text("Employment"),Text("Education")],
            top_left_entry=Text("Example No.")).scale(0.6)

        t5 = Table(
            [["1","0","0","1","0"],["0","1","0","1","0"],
            ["0","1","0","1","0"],["0","1","0","1","0"],
            ["0","0","1","1","0"],["0","0","0","1","0"],
            ["0","1","0","1","0"],[":",":",":",":",":"]],
            row_labels=[Text('1'),Text("2"),Text('3'),
                        Text("4"),Text("5"),Text("6"),Text("7"),Text(":")],
            col_labels=[Tex("$x_1$"),Tex("$x_2$"),Tex("$x_3$"),
                        Text("Employment"),Text("Education")],
            top_left_entry=Text("Example No.")).scale(0.6)

        for i in range(1,10):
            for j in range(2,6):
                t5.add_highlighted_cell((i,j), color=BLUE)
        for i in range(1,10):
            t5.add_highlighted_cell((i,5), color=GREEN)

        t4 = Table(
            [["1","0","0","1"],["0","1","0","1"],
            ["0","1","0","1"],["0","1","0","1"],
            ["0","0","1","1"],["0","0","0","1"],
            ["0","1","0","1"],[":",":",":",":"]],
            col_labels=[Tex("$x_1$"),Tex("$x_2$"),Tex("$x_3$"),
                        Text("Employment")],
            ).scale(0.6)



        self.play(t0.create())
        self.wait(5)
        self.play(Transform(t0,t2))
        self.wait(5)
        self.play(t0.animate.shift(UP))
        self.play(FadeTransform(t0,t3))
        self.wait(5)
        self.play(FadeTransform(t3,t5))
        self.wait(5)
        self.play(FadeTransform(t5,t3))
        self.wait(5)
        self.play(FadeTransform(t3,t4))
        #self.play(ScaleInPlace(t4,0.5))
        self.play(t4.animate.shift(RIGHT*4))
        self.play(Write(formula))
        #framebox1 = SurroundingRectangle(t4.get_rows()[1])
        #
        dot = Dot(LEFT*4)
        self.play(t4.animate.scale(0.4))
        self.play(FadeOut(t4,target_position = dot))

        formula4 = Tex(r"$\frac{P(Employment|Disability)}{1-P(Employment|Disability)}$")
        formula5 = Tex(r"$=$")
        formula6 = Tex(r"$e^{\beta_0 + \beta_1 x_1+ \beta_2 x_2+\beta_3 x_3}$")
        newformula = VGroup(formula4,formula5,formula6).arrange(RIGHT, buff=MED_LARGE_BUFF)
        self.play(Transform(formula,newformula))
        # self.play(FadeOut(formula))
        # self.play(FadeIn(newformula))
        framebox1 = SurroundingRectangle(newformula[0])
        self.play(Create(framebox1))
        self.wait(3)
        self.play(Uncreate(framebox1))
        self.play(Unwrite(newformula))

#class Results(Scene):
    def construct(self):
        r = Table(
            [["Predictors", "College Education", "Employment", "None"],
            ["Male", "3", "1.2", "0.6"],
            ["Female","0.7", "1.3", "1"],
            ["Hispanic","0.5", "0.5", "2.7"],
            ["Little Trouble\nin Conversation" ,"1.2", "0.8", "1.2"],
            ["No Conversation\n    at all","0.3", "0.5", "1.7"]],
            include_outer_lines=True).scale(0.5)
        r.get_horizontal_lines()[:3].set_color(BLUE)
        r.get_vertical_lines()[:3].set_color(BLUE)
        r.get_horizontal_lines()[:3].set_z_index(1)

        c1 = Text("Autism",color=RED)
        c2 = Text(">")
        c3 = Text("Other Disability Groups")
        c = VGroup(c1,c2,c3).arrange(RIGHT,buff=MED_LARGE_BUFF)
        self.play(Write(c))
        self.play(ScaleInPlace(c1,2),ScaleInPlace(c3,0.8),c2.animate.shift(RIGHT))
        self.wait(3)
        self.play(Unwrite(c))


        self.play(Create(r))
        self.wait(5)
        self.play(Uncreate(r))
        r.add_highlighted_cell((1,1), color=BLUE)
        self.wait(1)

        d1 = Dot(point=(UP*2+RIGHT),color='#bc5090')
        d2 = Dot(color = '#ff6361').next_to(d1,DOWN,buff=0.1)
        i1 = Text("income < $25 k",font_size=15).next_to(d1,RIGHT,buff=0.1)
        i2 = Text("income > $75 k",font_size=15).next_to(d2,RIGHT,buff=0.1)



        vals = [79, 45, 13, 3]
        colors = ['#bc5090', '#ff6361', '#bc5090', '#ff6361']
        bar = BarChart(
            vals,
            max_value=100,
            bar_colors=colors,
            bar_label_scale_val=1,
            label_y_axis=True
        )
        self.play(GrowFromEdge(bar, DOWN))
        xlab = Text("low functioning                  high functionaing",font_size=20).next_to(bar,DOWN)
        ylabel = Text("       Rates of\nno particiation",font_size=20).next_to(bar,LEFT)
        self.play(Write(xlab),Write(ylabel),Create(d1),Create(i2),Create(i1),Create(d2))
        self.wait(5)

class Count(Animation):
    def __init__(self, number: DecimalNumber, start: float, end: float, **kwargs) -> None:
        # Pass number as the mobject of the animation
        super().__init__(number,  **kwargs)
        # Set start and end
        self.start = start
        self.end = end

    def interpolate_mobject(self, alpha: float) -> None:
        # Set value of DecimalNumber according to alpha
        value = self.start + (alpha * (self.end - self.start))
        self.mobject.set_value(value)



