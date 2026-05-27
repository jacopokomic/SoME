import manim as m # type: ignore
import numpy as np # type: ignore
# ---------------------------------------------------------------------------
np.random.seed(42)
c = m.BLACK

m.Tex.set_default(
    color = c,
    font_size = 40
)
m.MathTex.set_default(
    color = c,
    font_size = 40
)
m.DecimalNumber.set_default(
    color = c,
    font_size = 40,
    num_decimal_places = 0,
    group_with_commas = False
)
m.Table.set_default(
    element_to_mobject = m.MathTex,
    line_config = {"color": c},
    h_buff = 0.5,
    v_buff = 0.3
)
m.Line.set_default(
    color = c
)
# ---------------------------------------------------------------------------
class Cell1(m.Scene):
    def construct(self):
        sw = 10
        m.ArcBetweenPoints.set_default(
            color = c,
            stroke_width = sw
        )

        r = 4
        h = r - np.sin(np.pi/4)*r
        d = np.cos(np.pi/4)*r

        arcUL = m.ArcBetweenPoints(
            start = d*m.LEFT + h*m.UP,
            end = m.ORIGIN,
            radius = -r
        )
        arcUR = m.ArcBetweenPoints(
            start = m.ORIGIN,
            end = d*m.RIGHT + h*m.UP,
            radius = -r
        )
        arcDL = m.ArcBetweenPoints(
            start = d*m.LEFT + h*m.DOWN,
            end = m.ORIGIN,
            radius = r
        )
        arcDR = m.ArcBetweenPoints(
            start = m.ORIGIN,
            end = d*m.RIGHT + h*m.DOWN,
            radius = r
        )
        atU = m.Triangle(
            color = c,
            fill_opacity = 1.0
        ).rotate(np.pi/6).scale(0.5)
        atD = m.Triangle(
            color = c,
            fill_opacity = 1.0
        ).rotate(np.pi/6).scale(0.5)
        n42 = m.DecimalNumber(42, font_size = 200).move_to(2*m.UP)
        n42copy = n42.copy().set_fill_opacity(0.5)
        seed = m.Dot(
            color = c,
            fill_opacity = 0.5
        )

        self.play(
            m.Create(arcUL, rate_func = m.rate_functions.ease_in_cubic),
            m.Create(arcDL, rate_func = m.rate_functions.ease_in_cubic)
        )
        self.play(
            m.Create(arcUR, rate_func = m.rate_functions.ease_out_cubic),
            m.Create(arcDR, rate_func = m.rate_functions.ease_out_cubic),
            m.Create(atU),
            m.Create(atD),
            m.MoveAlongPath(atU, arcUR, rate_func = m.rate_functions.ease_out_cubic),
            m.MoveAlongPath(atD, arcDR, rate_func = m.rate_functions.ease_out_cubic)
        )
        self.play(
            m.Write(n42)
        )
        self.add(n42copy, seed)
        self.play(
            m.Transform(n42copy, seed)
        )
        self.wait()
# ---------------------------------------------------------------------------
class Cell2(m.Scene):
    def construct(self):

        training = m.Tex("TRAINING").move_to(2.42*m.UP + 4.46*m.LEFT)
        traintab = m.Table(
            [["1", "45", "9120", "0.3241", "\\dots"],
            ["2", "52", "2600", "0.8544", "\\dots"],
            ["\\vdots", "\\vdots", "\\vdots", "\\vdots", "\\ddots"]],
            top_left_entry = m.Tex("TRAINING", fill_opacity = 0.0),
            col_labels = [m.Tex("Id"),
                          m.Tex("Age"),
                          m.Tex("Monthly Income"),
                          m.Tex("Debt Ratio"),
                          m.MathTex("\\dots")],
            row_labels = [m.MathTex("1"), m.MathTex("2"), m.MathTex("\\vdots")]
        ).move_to(1.5*m.UP)
        testing = m.Tex("TEST").move_to(0.58*m.DOWN + 4.46*m.LEFT)
        testtab = m.Table(
            [["1", "23", "12508", "0.0865", "\\dots"],
            ["2", "68", "8760", "0.2219", "\\dots"],
            ["\\vdots", "\\vdots", "\\vdots", "\\vdots", "\\ddots"]],
            top_left_entry = m.Tex("TRAINING", fill_opacity = 0.0),
            col_labels = [m.Tex("Id"),
                          m.Tex("Age"),
                          m.Tex("Monthly Income"),
                          m.Tex("Debt Ratio"),
                          m.MathTex("\\dots")],
            row_labels = [m.MathTex("1"), m.MathTex("2"), m.MathTex("\\vdots")]
        ).move_to(1.5*m.DOWN)
        lU = m.Line(
            start = 2.75*m.UP + 5.75*m.LEFT,
            end = 2.75*m.UP + 5.75*m.RIGHT
        )
        lUL = m.Line(
            start = 2.75*m.UP + 5.75*m.LEFT,
            end = 0.25*m.UP + 5.75*m.LEFT
        )
        lD = m.Line(
            start = 0.25*m.DOWN + 5.75*m.LEFT,
            end = 0.25*m.DOWN + 5.75*m.RIGHT
        )
        lDL = m.Line(
            start = 0.25*m.DOWN + 5.75*m.LEFT,
            end = 2.75*m.DOWN + 5.75*m.LEFT
        )

        train = m.VGroup(training, traintab, lU, lUL)
        test = m.VGroup(testing, testtab, lD, lDL)

        self.play(
            m.Create(train),
            m.Create(test),
            run_time = 5
        )
        self.wait()
# ---------------------------------------------------------------------------
class Cell3(m.Scene):
    def construct(self):

        training = m.Tex("TRAINING").move_to(2.38*m.UP + 4*m.LEFT)
        traintL = m.Table(
            [[],
            [],
            []],
            top_left_entry = m.Tex("TRAINING", fill_opacity = 0.0),
            col_labels = [],
            row_labels = [m.MathTex("1"), m.MathTex("2"), m.MathTex("\\vdots")],
            v_buff = 0.31
        ).move_to(1.46*m.UP + 4*m.LEFT)
        idU = m.Tex("Id").move_to(2.38*m.UP + 2.78*m.LEFT)
        traintId = m.Table(
            [[],
            [],
            []],
            top_left_entry = m.Tex("Id", fill_opacity = 0.0),
            col_labels = [],
            row_labels = [m.MathTex("1"), m.MathTex("2"), m.MathTex("\\vdots")],
            v_buff = 0.31
        ).move_to(1.45*m.UP + 2.78*m.LEFT)
        traintR = m.Table(
            [["9120", "0.3241", "\\dots"],
            ["2600", "0.8544", "\\dots"],
            ["\\vdots", "\\vdots", "\\ddots"]],
            top_left_entry = m.Tex("Age"),
            col_labels = [m.Tex("Monthly Income"),
                          m.Tex("Debt Ratio"),
                          m.MathTex("\\dots")],
            row_labels = [m.MathTex("45"), m.MathTex("52"), m.MathTex("\\vdots")]
        ).move_to(1.5*m.UP + 1.2*m.RIGHT)
        trainL = m.Line(
            start = 2.75*m.UP + 5.3*m.LEFT,
            end = 2.75*m.UP + 2.7*m.LEFT
        )
        trainIdU = m.Line(
            start = 2.75*m.UP + 3.3*m.LEFT,
            end = 2.75*m.UP + 2.2*m.LEFT
        )
        trainR = m.Line(
            start =  2.75*m.UP + 2.8*m.LEFT,
            end = 2.75*m.UP + 5.2*m.RIGHT
        )
        trainS = m.Line(
            start = 2.75*m.UP + 5.3*m.LEFT,
            end = 0.25*m.UP + 5.3*m.LEFT
        )
        trainIdL = m.Line(
            start = 2.75*m.UP + 3.2*m.LEFT,
            end = 0.25*m.UP + 3.2*m.LEFT
        )
        trainIdR = m.Line(
            start = 2.75*m.UP + 2.34*m.LEFT,
            end = 0.25*m.UP + 2.34*m.LEFT
        )
        trainM = m.Line(
            start = 2.75*m.UP + 2.75*m.LEFT,
            end = 0.25*m.UP + 2.75*m.LEFT
        )
        trainL = m.VGroup(training, traintL, trainL, trainS).shift(0.5*m.LEFT)
        trainId = m.VGroup(idU, traintId, trainIdU, trainIdL, trainIdR)
        trainR = m.VGroup(traintR, trainR).shift(0.5*m.RIGHT)

        testing = m.Tex("TEST").move_to(0.63*m.DOWN + 4*m.LEFT)
        testtL = m.Table(
            [[],
            [],
            []],
            top_left_entry = m.Tex("TRAINING", fill_opacity = 0.0),
            col_labels = [],
            row_labels = [m.MathTex("1"), m.MathTex("2"), m.MathTex("\\vdots")],
            v_buff = 0.31
        ).move_to(1.54*m.DOWN + 4*m.LEFT)
        idD = m.Tex("Id").move_to(0.63*m.DOWN + 2.78*m.LEFT)
        testtId = m.Table(
            [[],
            [],
            []],
            top_left_entry = m.Tex("Id", fill_opacity = 0.0),
            col_labels = [],
            row_labels = [m.MathTex("1"), m.MathTex("2"), m.MathTex("\\vdots")],
            v_buff = 0.31
        ).move_to(1.55*m.DOWN + 2.78*m.LEFT)
        testtR = m.Table(
            [["12508", "0.0865", "\\dots"],
            ["8760", "0.2219", "\\dots"],
            ["\\vdots", "\\vdots", "\\ddots"]],
            top_left_entry = m.Tex("Age"),
            col_labels = [m.Tex("Monthly Income"),
                          m.Tex("Debt Ratio"),
                          m.MathTex("\\dots")],
            row_labels = [m.MathTex("23"), m.MathTex("68"), m.MathTex("\\vdots")]
        ).move_to(1.5*m.DOWN + 1.2*m.RIGHT)
        testL = m.Line(
            start = 0.25*m.DOWN + 5.3*m.LEFT,
            end = 0.25*m.DOWN + 2.7*m.LEFT
        )
        testIdU = m.Line(
            start = 0.25*m.DOWN + 3.3*m.LEFT,
            end = 0.25*m.DOWN + 2.2*m.LEFT
        )
        testR = m.Line(
            start =  0.25*m.DOWN + 2.8*m.LEFT,
            end = 0.25*m.DOWN + 5.2*m.RIGHT
        )
        testS = m.Line(
            start = 0.25*m.DOWN + 5.3*m.LEFT,
            end = 2.75*m.DOWN + 5.3*m.LEFT
        )
        testIdL = m.Line(
            start = 0.25*m.DOWN + 3.2*m.LEFT,
            end = 2.75*m.DOWN + 3.2*m.LEFT
        )
        testIdR = m.Line(
            start = 0.25*m.DOWN + 2.34*m.LEFT,
            end = 2.75*m.DOWN + 2.34*m.LEFT
        )
        testM = m.Line(
            start = 0.25*m.DOWN + 2.75*m.LEFT,
            end = 2.75*m.DOWN + 2.75*m.LEFT
        )
        testL = m.VGroup(testing, testtL, testL, testS).shift(0.5*m.LEFT)
        testId = m.VGroup(idD, testtId, testIdU, testIdL, testIdR)
        testR = m.VGroup(testtR, testR).shift(0.5*m.RIGHT)

        self.play( 
            m.FadeIn(trainL, trainId, trainR, testL, testId, testR)
        )
        self.wait()
        self.play(
            m.Transform(trainId, trainM),
            m.Transform(testId, testM),
            trainL.animate.shift(0.46*m.RIGHT),
            testL.animate.shift(0.46*m.RIGHT),
            trainR.animate.shift(0.46*m.LEFT),
            testR.animate.shift(0.46*m.LEFT)
        )
        self.wait()
# ---------------------------------------------------------------------------
class Cell4(m.Scene):
    def construct(self):

        emptyU = m.Table(
            [["", "", "", "\\dots"],
            ["", "", "", "\\dots"],
            ["\\vdots", "\\vdots", "\\vdots", "\\ddots"]],
            top_left_entry = m.Tex("TRAINING", fill_opacity = 0.0),
            col_labels = [m.Tex("Age", fill_opacity = 0.0),
                          m.Tex("Monthly Income", fill_opacity = 0.0),
                          m.Tex("Debt Ratio", fill_opacity = 0.0),
                          m.MathTex("\\dots")],
            row_labels = [m.DecimalNumber(1, fill_opacity = 0.0),
                          m.DecimalNumber(2, fill_opacity = 0.0),
                          m.Tex("\\vdots")]
        ).move_to(1.5*m.UP)
        emptyD = m.Table(
            [["", "", "", "\\dots"],
            ["", "", "", "\\dots"],
            ["\\vdots", "\\vdots", "\\vdots", "\\ddots"]],
            top_left_entry = m.Tex("TRAINING", fill_opacity = 0.0),
            col_labels = [m.Tex("Age", fill_opacity = 0.0),
                          m.Tex("Monthly Income", fill_opacity = 0.0),
                          m.Tex("Debt Ratio", fill_opacity = 0.0),
                          m.MathTex("\\dots")],
            row_labels = [m.DecimalNumber(1, fill_opacity = 0.0),
                          m.DecimalNumber(2, fill_opacity = 0.0),
                          m.MathTex("\\vdots")]
        ).move_to(1.5*m.DOWN)
        lU = m.Line(
            start = 2.75*m.UP + 5.3*m.LEFT,
            end = 2.75*m.UP + 5.3*m.RIGHT
        )
        lUL = m.Line(
            start = 2.75*m.UP + 5.3*m.LEFT,
            end = 0.25*m.UP + 5.3*m.LEFT
        )
        lD = m.Line(
            start = 0.25*m.DOWN + 5.3*m.LEFT,
            end = 0.25*m.DOWN + 5.3*m.RIGHT
        )
        lDL = m.Line(
            start = 0.25*m.DOWN + 5.3*m.LEFT,
            end = 2.75*m.DOWN + 5.3*m.LEFT
        )
        training = m.Tex("TRAINING").move_to(2.42*m.UP + 4.02*m.LEFT)
        ageU = m.Tex("Age").move_to(2.42*m.UP + 2.11*m.LEFT)
        incomeU = m.Tex("Monthly Income").move_to(2.42*m.UP + 0.2*m.RIGHT)
        debtU = m.Tex("Debt Ratio").move_to(2.42*m.UP + 3.17*m.RIGHT)
        testing = m.Tex("TEST").move_to(0.58*m.DOWN + 4.02*m.LEFT)
        ageD = m.Tex("Age").move_to(0.58*m.DOWN + 2.11*m.LEFT)
        incomeD = m.Tex("Monthly Income").move_to(0.58*m.DOWN + 0.2*m.RIGHT)
        debtD = m.Tex("Debt Ratio").move_to(0.58*m.DOWN + 3.17*m.RIGHT)
        train1 = m.DecimalNumber(1).move_to(1.78*m.UP + 4.02*m.LEFT)
        train2 = m.DecimalNumber(2).move_to(1.21*m.UP + 4.02*m.LEFT)
        test1 = m.DecimalNumber(1).move_to(1.21*m.DOWN + 4.02*m.LEFT)
        test2 = m.DecimalNumber(2).move_to(1.8*m.DOWN + 4.02*m.LEFT)
        ageU1 = m.DecimalNumber(45).move_to(1.78*m.UP + 2.11*m.LEFT)
        ageU2 = m.DecimalNumber(52).move_to(1.21*m.UP + 2.11*m.LEFT)
        ageD1 = m.DecimalNumber(23).move_to(1.21*m.DOWN + 2.11*m.LEFT)
        ageD2 = m.DecimalNumber(68).move_to(1.8*m.DOWN + 2.11*m.LEFT)
        incomeU1 = m.DecimalNumber(9120).move_to(1.78*m.UP + 0.2*m.RIGHT)
        incomeU2 = m.DecimalNumber(2600).move_to(1.21*m.UP + 0.2*m.RIGHT)
        incomeD1 = m.DecimalNumber(12508).move_to(1.21*m.DOWN + 0.2*m.RIGHT)
        incomeD2 = m.DecimalNumber(8760).move_to(1.8*m.DOWN + 0.2*m.RIGHT)
        debtU1 = m.DecimalNumber(0.3241, num_decimal_places = 4).move_to(1.78*m.UP + 3.17*m.RIGHT)
        debtU2 = m.DecimalNumber(0.8544, num_decimal_places = 4).move_to(1.21*m.UP + 3.17*m.RIGHT)
        debtD1 = m.DecimalNumber(0.0865, num_decimal_places = 4).move_to(1.21*m.DOWN + 3.17*m.RIGHT)
        debtD2 = m.DecimalNumber(0.2219, num_decimal_places = 4).move_to(1.8*m.DOWN + 3.17*m.RIGHT)

        train = m.VGroup(emptyU, lU, lUL, training, ageU, incomeU, debtU)
        test = m.VGroup(emptyD, lD, lDL, testing, ageD, incomeD, debtD)
        lU1 = m.VGroup(train1, ageU1, incomeU1, debtU1)
        lU2 = m.VGroup(train2, ageU2, incomeU2, debtU2)
        lD1 = m.VGroup(test1, ageD1, incomeD1, debtD1)
        lD2 = m.VGroup(test2, ageD2, incomeD2, debtD2)

        dU = lU1.get_y() - lU2.get_y()
        dD = lD1.get_y() - lD2.get_y()

        train3 = m.DecimalNumber(12).move_to(1.21*m.UP + 4.02*m.LEFT)
        ageU3 = m.DecimalNumber(33).move_to(1.21*m.UP + 2.11*m.LEFT)
        incomeU3 = m.DecimalNumber(4570).move_to(1.21*m.UP + 0.2*m.RIGHT)
        debtU3 = m.DecimalNumber(0.2179, num_decimal_places = 4).move_to(1.21*m.UP + 3.17*m.RIGHT)
        train4 = m.DecimalNumber(13).move_to((1.21 - dU)*m.UP + 4.02*m.LEFT)
        ageU4 = m.DecimalNumber(72).move_to((1.21 - dU)*m.UP + 2.11*m.LEFT)
        incomeU4 = m.Tex("NA").move_to((1.21 - dU)*m.UP + 0.2*m.RIGHT)
        debtU4 = m.DecimalNumber(0.1562, num_decimal_places = 4).move_to((1.21 - dU)*m.UP + 3.17*m.RIGHT)

        lU3 = m.VGroup(train3, ageU3, incomeU3, debtU3).set_opacity(0.0)
        lU4 = m.VGroup(train4, ageU4, incomeU4, debtU4).set_opacity(0.0)

        test3 = m.DecimalNumber(46).move_to(1.8*m.DOWN + 4.02*m.LEFT)
        ageD3 = m.DecimalNumber(28).move_to(1.8*m.DOWN + 2.11*m.LEFT)
        incomeD3 = m.DecimalNumber(25680).move_to(1.8*m.DOWN + 0.2*m.RIGHT)
        debtD3 = m.DecimalNumber(0.6233, num_decimal_places = 4).move_to(1.8*m.DOWN + 3.17*m.RIGHT)
        test4 = m.DecimalNumber(47).move_to((1.8 + dD)*m.DOWN + 4.02*m.LEFT)
        ageD4 = m.DecimalNumber(59).move_to((1.8 + dD)*m.DOWN + 2.11*m.LEFT)
        incomeD4 = m.Tex("NA").move_to((1.8 + dD)*m.DOWN + 0.2*m.RIGHT)
        debtD4 = m.DecimalNumber(0.0489, num_decimal_places = 4).move_to((1.8 + dD)*m.DOWN + 3.17*m.RIGHT)

        lD3 = m.VGroup(test3, ageD3, incomeD3, debtD3).set_opacity(0.0)
        lD4 = m.VGroup(test4, ageD4, incomeD4, debtD4).set_opacity(0.0)

        rectangleU = m.Rectangle(
            width = 3.4,
            height = 2.5,
            color = m.BLUE,
            fill_opacity = 0.5
        ).move_to(1.48*m.UP + 0.2*m.RIGHT)
        medianU = m.Tex("median(\\,\\,\\,\\,\\,\\,)").move_to(1.21*m.UP + 0.2*m.RIGHT)

        rectangleD = m.Rectangle(
            width = 3.4,
            height = 2.5,
            color = m.BLUE,
            fill_opacity = 0.5
        ).move_to(1.52*m.DOWN + 0.2*m.RIGHT)
        medianD = m.Tex("median(\\,\\,\\,\\,\\,\\,)").move_to(1.8*m.DOWN + 0.2*m.RIGHT)

        self.play(
            m.FadeIn(train, test, lU1, lU2, lD1, lD2)
        )
        self.wait()
        self.play(
            lU1.animate.shift(dU*m.UP).set_opacity(0.0),
            lU2.animate.shift(dU*m.UP).set_opacity(0.0),
            lU3.animate.shift(dU*m.UP).set_opacity(1.0),
            lU4.animate.shift(dU*m.UP).set_opacity(1.0),
            lD1.animate.shift(dD*m.UP).set_opacity(0.0),
            lD2.animate.shift(dD*m.UP).set_opacity(0.0),
            lD3.animate.shift(dD*m.UP).set_opacity(1.0),
            lD4.animate.shift(dD*m.UP).set_opacity(1.0)
        )
        self.wait()
        self.play(
            m.Wiggle(incomeU4,
                     scale_value = 2,
                     rotation_angle = 0.1,
                     scale_about_point = incomeU4.get_center()
            ),
            m.Wiggle(incomeD4,
                     scale_value = 2,
                     rotation_angle = 0.1,
                     scale_about_point = incomeD4.get_center()
            )
        )
        self.wait()
        self.play(
            m.FadeIn(rectangleU),
            m.FadeIn(rectangleD)
        )
        self.wait()
        self.play(
            m.Transform(incomeU4, medianU),
            m.Transform(incomeD4, medianD),
            rectangleU.animate.scale(0.1).move_to(medianU.get_center() + 0.675*m.RIGHT),
            rectangleD.animate.scale(0.1).move_to(medianD.get_center() + 0.675*m.RIGHT)
        )
        self.wait()
# ---------------------------------------------------------------------------
class Cell5(m.Scene):
    def construct(self):

        tabU = m.Table(
            [["45", "9120", "0.3241"],
            ["52", "2600", "0.8544"],
            ["\\vdots", "\\vdots", "\\vdots"]],
            top_left_entry = m.Tex("TRAINING"),
            col_labels = [m.Tex("Age"),
                          m.Tex("Monthly Income"),
                          m.Tex("Debt Ratio")],
            row_labels = [m.DecimalNumber(1),
                          m.DecimalNumber(2),
                          m.MathTex("\\vdots")]
        ).move_to(1.5*m.UP + 0.46*m.LEFT)

        lU = m.Line(
            start = 2.75*m.UP + 5.3*m.LEFT,
            end = 2.75*m.UP + 4.4*m.RIGHT
        )
        lUL = m.Line(
            start = 2.75*m.UP + 5.32*m.LEFT,
            end = 0.25*m.UP + 5.32*m.LEFT
        )
        lUR = m.Line(
            start = 2.75*m.UP + 4.4*m.RIGHT,
            end = 0.25*m.UP + 4.4*m.RIGHT
        )

        tabD = m.Table(
            [["23", "12508", "0.0865"],
            ["68", "8760", "0.2219"],
            ["\\vdots", "\\vdots", "\\vdots"]],
            top_left_entry = m.Tex("TRAINING", fill_opacity = 0.0),
            col_labels = [m.Tex("Age"),
                          m.Tex("Monthly Income"),
                          m.Tex("Debt Ratio")],
            row_labels = [m.DecimalNumber(1),
                          m.DecimalNumber(2),
                          m.MathTex("\\vdots")]
        ).move_to(1.5*m.DOWN + 0.46*m.LEFT)

        testing = m.Tex("TEST").move_to(0.58*m.DOWN + 4.02*m.LEFT)

        lD = m.Line(
            start = 0.25*m.DOWN + 5.3*m.LEFT,
            end = 0.25*m.DOWN + 4.4*m.RIGHT
        )
        lDL = m.Line(
            start = 0.25*m.DOWN + 5.32*m.LEFT,
            end = 2.75*m.DOWN + 5.32*m.LEFT
        )
        lDR = m.Line(
            start = 0.25*m.DOWN + 4.4*m.RIGHT,
            end = 2.75*m.DOWN + 4.4*m.RIGHT
        )

        tabUL = m.VGroup(tabU, lU, lUL)
        tabDL = m.VGroup(testing, tabD, lD, lDL)

        lU1 = m.Line(
            start = 2.75*m.UP + 4.4*m.RIGHT,
            end = 2.75*m.UP + 5.3*m.RIGHT
        )
        lU2 = lU1.copy().shift(0.67*m.DOWN)
        lU3 = lU1.copy().shift(1.25*m.DOWN)
        lU4 = lU1.copy().shift(1.84*m.DOWN)

        dU1 = m.MathTex("\\dots").move_to(2.4*m.UP + 4.85*m.RIGHT)
        dU2 = dU1.copy().shift(0.63*m.DOWN)
        dU3 = dU1.copy().shift(1.21*m.DOWN)
        dU4 = m.MathTex("\\ddots").move_to(0.57*m.UP + 4.85*m.RIGHT)

        lD1 = m.Line(
            start = 0.25*m.DOWN + 4.4*m.RIGHT,
            end = 0.25*m.DOWN + 5.3*m.RIGHT
        )
        lD2 = lD1.copy().shift(0.67*m.DOWN)
        lD3 = lD1.copy().shift(1.25*m.DOWN)
        lD4 = lD1.copy().shift(1.84*m.DOWN)

        dD1 = m.MathTex("\\dots").move_to(0.57*m.DOWN + 4.85*m.RIGHT)
        dD2 = dD1.copy().shift(0.63*m.DOWN)
        dD3 = dD1.copy().shift(1.21*m.DOWN)
        dD4 = m.MathTex("\\ddots").move_to(2.43*m.DOWN + 4.85*m.RIGHT)

        tabUR = m.VGroup(lU1, lU2, lU3, lU4, dU1, dU2, dU3, dU4)
        tabDR = m.VGroup(lD1, lD2, lD3, lD4, dD1, dD2, dD3, dD4)

        tabdebtU = m.Table(
            [[],
            [],
            []],
            top_left_entry = m.Tex("Total Debt"),
            col_labels = [],
            row_labels = [m.DecimalNumber(2955.79, num_decimal_places = 2),
                          m.DecimalNumber(2221.44, num_decimal_places = 2),
                          m.MathTex("\\vdots")]
        ).move_to(lUR.get_center() + 0.05*m.DOWN)

        tlU = m.Line(
            start = 2.75*m.UP + 3.2*m.RIGHT,
            end = 2.75*m.UP + 5.6*m.RIGHT
        )
        tlUL = m.Line(
            start = 2.75*m.UP + 3.2*m.RIGHT,
            end = 0.25*m.UP + 3.2*m.RIGHT
        )
        tlUR = m.Line(
            start = 2.75*m.UP + 5.6*m.RIGHT,
            end = 0.25*m.UP + 5.6*m.RIGHT
        )

        tabdebtD = m.Table(
            [[],
            [],
            []],
            top_left_entry = m.Tex("Total Debt"),
            col_labels = [],
            row_labels = [m.DecimalNumber(1081.94, num_decimal_places = 2),
                          m.DecimalNumber(1943.84, num_decimal_places = 2),
                          m.MathTex("\\vdots")]
        ).move_to(lDR.get_center() + 0.05*m.DOWN)

        tlD = m.Line(
            start = 0.25*m.DOWN + 3.2*m.RIGHT,
            end = 0.25*m.DOWN + 5.6*m.RIGHT
        )
        tlDL = m.Line(
            start = 0.25*m.DOWN + 3.2*m.RIGHT,
            end = 2.75*m.DOWN + 3.2*m.RIGHT
        )
        tlDR = m.Line(
            start = 0.25*m.DOWN + 5.6*m.RIGHT,
            end = 2.75*m.DOWN + 5.6*m.RIGHT
        )

        debtU = m.VGroup(tabdebtU, tlU, tlUL, tlUR)
        debtD = m.VGroup(tabdebtD, tlD, tlDL, tlDR)

        bU = m.Rectangle(
            width = 3.4,
            height = 2.5,
            color = m.BLUE,
            fill_opacity = 0.5
        ).move_to(1.48*m.UP + 0.2*m.RIGHT)
        yU = m.Rectangle(
            width = 2.41,
            height = 2.5,
            color = m.YELLOW,
            fill_opacity = 0.5
        ).move_to(1.48*m.UP + 3.15*m.RIGHT)
        gU = m.Rectangle(
            width = 2.4,
            height = 2.5,
            color = m.GREEN,
            fill_opacity = 0.5
        ).move_to(lUR.get_center() + 0.02*m.DOWN)
        bD = m.Rectangle(
            width = 3.4,
            height = 2.5,
            color = m.BLUE,
            fill_opacity = 0.5
        ).move_to(1.52*m.DOWN + 0.2*m.RIGHT)
        yD = m.Rectangle(
            width = 2.41,
            height = 2.5,
            color = m.YELLOW,
            fill_opacity = 0.5
        ).move_to(1.52*m.DOWN + 3.15*m.RIGHT)
        gD = m.Rectangle(
            width = 2.4,
            height = 2.5,
            color = m.GREEN,
            fill_opacity = 0.5
        ).move_to(lDR.get_center() + 0.02*m.DOWN)

        bUc = bU.copy().scale(0.1).move_to(bU.get_center() + 1.8*m.UP + 1.2*m.LEFT)
        yUc = yU.copy().scale(0.1).move_to(yU.get_center() + 1.8*m.UP + 1.2*m.LEFT)
        gUc = gU.copy().scale(0.1).move_to(gU.get_center() + 1.8*m.UP)
        dot = m.MathTex("\\cdot").move_to(3.28*m.UP + 0.48*m.RIGHT)
        equal = m.MathTex("=").move_to(3.28*m.UP + 3.18*m.RIGHT)

        eq = m.VGroup(bUc, dot, yUc, equal, gUc)

        self.play(
            m.FadeIn(tabUL, lUR, tabUR, tabDL, lDR, tabDR)
        )
        self.wait()
        self.play(
            m.FadeIn(bU, yU, bD, yD)
        )
        self.wait()
        self.play(
            m.Transform(lUR, debtU),
            m.Transform(lDR, debtD),
            tabUL.animate.shift(1.2*m.LEFT),
            tabDL.animate.shift(1.2*m.LEFT),
            bU.animate.shift(1.2*m.LEFT),
            bD.animate.shift(1.2*m.LEFT),
            yU.animate.shift(1.2*m.LEFT),
            yD.animate.shift(1.2*m.LEFT),
            tabUR.animate.shift(1.2*m.RIGHT),
            tabDR.animate.shift(1.2*m.RIGHT),
            m.FadeIn(gU, gD)
        )
        self.wait()
        self.play(
            m.Create(eq)
        )
        self.wait()
# ---------------------------------------------------------------------------
class Cell6(m.Scene):
    def construct(self):

        title = m.Tex("Monthly Income, Debt Ratio").move_to(3.5*m.UP)
        lin = m.Tex("lin").move_to(3.5*m.UP + 5*m.RIGHT)
        log = m.Tex("log").move_to(3.5*m.UP + 6*m.RIGHT)

        select = m.RoundedRectangle(
            width = 0.8,
            height = 0.6,
            corner_radius = 0.1,
            color = c,
            fill_opacity = 0.5
        ).move_to(3.5*m.UP + 5*m.RIGHT)

        base = m.RoundedRectangle(
            width = 2.0,
            height = 0.8,
            corner_radius = 0.2,
            color = c
        ).move_to(3.5*m.UP + 5.5*m.RIGHT)

        toggle = m.VGroup(base, select, lin, log)

        size = 1000
        x = np.linspace(1, size, size)
        y = np.random.lognormal(3, 1, size)

        ax = m.Axes(
            x_range = [0, size],
            y_range = [0, np.max(y)],
            tips = False,
            axis_config = {"include_ticks": False}
        )

        xlab = ax.get_x_axis_label(m.Tex("index"), edge = m.DOWN, direction = m.DOWN, buff = 0.3)
        ylab = ax.get_y_axis_label(m.Tex("value"), edge = m.LEFT, direction = m.LEFT, buff = 0.3).rotate(np.pi/2)

        scatter = ax.plot_line_graph(
            x_values = x,
            y_values = y + 1,
            add_vertex_dots = True,
            stroke_width = 0,
            vertex_dot_radius = 0.05,
            vertex_dot_style = {"color": c}
        )

        ax_log = m.Axes(
            x_range = [0, size],
            y_range = [0, np.log10(np.max(y))],
            tips = False,
            axis_config = {"include_ticks": False},
            y_axis_config = {"scaling": m.LogBase(base = 10)}
        )

        scatter_log = ax_log.plot_line_graph(
            x_values = x,
            y_values = y + 1,
            add_vertex_dots = True,
            stroke_width = 0,
            vertex_dot_radius = 0.05,
            vertex_dot_style = {"color": c}
        )

        self.play(
            m.Write(title),
            m.Create(ax)
        )
        self.play(
            m.Write(xlab)
        )
        self.play(
            m.Write(ylab)
        )
        self.play(
            m.Create(toggle),
            m.Create(scatter)
        )
        self.wait()
        self.play(
            m.Transform(ax, ax_log),
            m.Transform(scatter, scatter_log),
            select.animate.move_to(3.5*m.UP + 6*m.RIGHT)
        )
        self.wait()
# ---------------------------------------------------------------------------
class Cell7(m.Scene):
    def construct(self):

        title = m.Tex("Number Of Times X Days Pas Due").move_to(3.5*m.UP)

        size = 1000
        out = 50
        x = np.linspace(1, size, size)
        y1 = np.round(20*np.random.beta(1, 5, size - out))
        y2 = 98*np.ones(out)
        y = np.hstack((y1, y2))
        np.random.shuffle(y)

        ax = m.Axes(
            x_range = [0, size],
            y_range = [0, np.max(y), 20],
            tips = False,
            x_axis_config = {"include_ticks": False},
            y_axis_config = {"include_numbers": True}
        )

        xlab = ax.get_x_axis_label(m.Tex("index"), edge = m.DOWN, direction = m.DOWN, buff = 0.3)
        dummy = ax.get_y_axis_label(m.Tex("value", fill_opacity = 0.0), edge = m.LEFT, direction = m.LEFT, buff = 0.3).rotate(np.pi/2)
        ylab = dummy.copy().set_opacity(1.0).shift(0.5*m.LEFT)

        scatter = ax.plot_line_graph(
            x_values = x,
            y_values = y,
            add_vertex_dots = True,
            stroke_width = 0,
            vertex_dot_radius = 0.05,
            vertex_dot_style = {"color": c}
        )

        new_y = np.clip(y, 0, 20)

        new_ax = m.Axes(
            x_range = [0, size],
            y_range = [0, np.max(new_y), 20],
            tips = False,
            x_axis_config = {"include_ticks": False},
            y_axis_config = {"include_numbers": True}
        )

        new_scatter = new_ax.plot_line_graph(
            x_values = x,
            y_values = new_y,
            add_vertex_dots = True,
            stroke_width = 0,
            vertex_dot_radius = 0.05,
            vertex_dot_style = {"color": c}
        )

        self.play(
            m.Write(title),
            m.Create(ax)
        )
        self.play(
            m.Write(xlab)
        )
        self.play(
            m.Write(ylab)
        )
        self.play(
            m.Create(scatter)
        )
        self.wait()
        self.play(
            m.Transform(ax, new_ax),
            m.Transform(scatter, new_scatter),
            ylab.animate.shift(0.5*m.RIGHT)
        )
        self.wait()
# ---------------------------------------------------------------------------
class Cell8(m.Scene):
    def construct(self):

        title = m.Tex("Revolving Utilization Of Unsecured Lines").move_to(3.5*m.UP)

        size = 1000
        x = np.linspace(1, size, size)
        y = 2*np.random.beta(1, 5, size)

        ax = m.Axes(
            x_range = [0, size],
            y_range = [0, np.max(y), 1.0],
            tips = False,
            x_axis_config = {"include_ticks": False},
            y_axis_config = {"include_numbers": True}
        )

        xlab = ax.get_x_axis_label(m.Tex("index"), edge = m.DOWN, direction = m.DOWN, buff = 0.3)
        ylab = ax.get_y_axis_label(m.Tex("value"), edge = m.LEFT, direction = m.LEFT, buff = 0.3).rotate(np.pi/2)

        scatter = ax.plot_line_graph(
            x_values = x,
            y_values = y,
            add_vertex_dots = True,
            stroke_width = 0,
            vertex_dot_radius = 0.05,
            vertex_dot_style = {"color": c}
        )

        new_y = np.clip(y, 0, 1)

        new_ax = m.Axes(
            x_range = [0, size],
            y_range = [0, np.max(new_y), 1.0],
            tips = False,
            x_axis_config = {"include_ticks": False},
            y_axis_config = {"include_numbers": True}
        )

        new_scatter = new_ax.plot_line_graph(
            x_values = x,
            y_values = new_y,
            add_vertex_dots = True,
            stroke_width = 0,
            vertex_dot_radius = 0.05,
            vertex_dot_style = {"color": c}
        )

        self.play(
            m.Write(title),
            m.Create(ax)
        )
        self.play(
            m.Write(xlab)
        )
        self.play(
            m.Write(ylab)
        )
        self.play(
            m.Create(scatter)
        )
        self.wait()
        self.play(
            m.Transform(ax, new_ax),
            m.Transform(scatter, new_scatter)
        )
        self.wait()
# ---------------------------------------------------------------------------
class Cell9(m.Scene):
    def construct(self):

        tabU = m.Table(
            [["45", "9120", "0.3241", "\\dots"],
            ["52", "2600", "0.8544", "\\dots"]],
            top_left_entry = m.Tex("TRAINING"),
            col_labels = [m.Tex("Age"),
                          m.Tex("Monthly Income"),
                          m.Tex("Debt Ratio"),
                          m.MathTex("\\dots")],
            row_labels = [m.DecimalNumber(1),
                          m.DecimalNumber(2)]
        ).move_to(1.82*m.UP)

        lU = m.Line(
            start = 2.75*m.UP + 5.32*m.LEFT,
            end = 2.75*m.UP + 5.32*m.RIGHT
        )
        lUL = m.Line(
            start = 2.75*m.UP + 5.32*m.LEFT,
            end = 0.9*m.UP + 5.32*m.LEFT
        )

        tabD = m.Table(
            [["23", "12508", "0.0865", "\\dots"],
            ["68", "8760", "0.2219", "\\dots"],
            ["\\vdots", "\\vdots", "\\vdots", "\\ddots"]],
            top_left_entry = m.Tex("TRAINING", fill_opacity = 0.0),
            col_labels = [m.Tex("Age"),
                          m.Tex("Monthly Income"),
                          m.Tex("Debt Ratio"),
                          m.MathTex("\\dots")],
            row_labels = [m.DecimalNumber(1),
                          m.DecimalNumber(2),
                          m.MathTex("\\vdots")]
        ).move_to(1.5*m.DOWN)

        testing = m.Tex("TEST").move_to(0.58*m.DOWN + 4.02*m.LEFT)

        lD = m.Line(
            start = 0.25*m.DOWN + 5.32*m.LEFT,
            end = 0.25*m.DOWN + 5.32*m.RIGHT
        )
        lDL = m.Line(
            start = 0.25*m.DOWN + 5.32*m.LEFT,
            end = 2.75*m.DOWN + 5.32*m.LEFT
        )

        tab = m.VGroup(tabU, lU, lUL)
        tabDL = m.VGroup(testing, tabD, lD, lDL)

        low = m.Line(
            start = 0.9*m.UP + 5.32*m.LEFT,
            end = 0.9*m.UP + 5.32*m.RIGHT
        )

        vline1 = m.Line(
            start = 0.9*m.UP + 5.32*m.LEFT,
            end = 0.25*m.UP + 5.32*m.LEFT
        )
        vline2 = m.Line(
            start = 0.9*m.UP + 2.7*m.LEFT,
            end = 0.25*m.UP + 2.7*m.LEFT
        )
        vline3 = m.Line(
            start = 0.9*m.UP + 1.52*m.LEFT,
            end = 0.25*m.UP + 1.52*m.LEFT
        )
        vline4 = m.Line(
            start = 0.9*m.UP + 1.92*m.RIGHT,
            end = 0.25*m.UP + 1.92*m.RIGHT
        )
        vline5 = m.Line(
            start = 0.9*m.UP + 4.42*m.RIGHT,
            end = 0.25*m.UP + 4.42*m.RIGHT
        )
        vlines = m.VGroup(vline1, vline2, vline3, vline4, vline5)

        vdots1 = m.MathTex("\\vdots").move_to(0.58*m.UP + 4.02*m.LEFT)
        vdots2 = m.MathTex("\\vdots").move_to(0.58*m.UP + 2.11*m.LEFT)
        vdots3 = m.MathTex("\\vdots").move_to(0.58*m.UP + 0.2*m.RIGHT)
        vdots4 = m.MathTex("\\vdots").move_to(0.58*m.UP + 3.16*m.RIGHT)
        ddots = m.MathTex("\\ddots").move_to(0.58*m.UP + 4.87*m.RIGHT)
        vdots = m.VGroup(vdots1, vdots2, vdots3, vdots4, ddots)

        lowtab = m.VGroup(vlines, vdots)

        mid = m.Table(
            [["77", "4062", "0.3674"],
            ["32", "13985", "0.8612"],
            ["24", "6210", "0.5143"],
            ["63", "3375", "0.9412"]],
            top_left_entry = m.Tex("TRAINING", fill_opacity = 0.0),
            col_labels = [m.Tex("Age", fill_opacity = 0.0),
                          m.Tex("Monthly Income", fill_opacity = 0.0),
                          m.Tex("Debt Ratio", fill_opacity = 0.0)],
            row_labels = [m.DecimalNumber(4),
                          m.DecimalNumber(5),
                          m.DecimalNumber(6),
                          m.DecimalNumber(7)]
        ).move_to(0.525*m.DOWN + 0.455*m.LEFT)

        midU = m.Line(
            start = 0.9*m.UP + 5.32*m.LEFT,
            end = 0.9*m.UP + 5.32*m.RIGHT
        )
        midD = m.Line(
            start = 2.05*m.DOWN + 5.32*m.LEFT,
            end = 2.05*m.DOWN + 5.32*m.RIGHT
        )
        midL = m.Line(
            start = 0.9*m.UP + 5.32*m.LEFT,
            end = 2.05*m.DOWN + 5.32*m.LEFT
        )
        midR = m.Line(
            start = 0.9*m.UP + 4.42*m.RIGHT,
            end = 2.05*m.DOWN + 4.42*m.RIGHT
        )

        h1 = m.Line(
            start = 0.31*m.UP + 4.42*m.RIGHT,
            end = 0.31*m.UP + 5.32*m.RIGHT
        )
        h2 = h1.copy().shift(0.585*m.DOWN)
        h3 = h2.copy().shift(0.585*m.DOWN)
        h4 = h3.copy().shift(0.585*m.DOWN)
        h = m.VGroup(h1, h2, h3, h4)

        d1 = m.MathTex("\\dots").move_to(0.59*m.UP + 4.87*m.RIGHT)
        d2 = d1.copy().shift(0.585*m.DOWN)
        d3 = d2.copy().shift(0.585*m.DOWN)
        d4 = d3.copy().shift(0.585*m.DOWN)
        d5 = d4.copy().shift(0.585*m.DOWN)
        d = m.VGroup(d1, d2, d3, d4, d5)

        t1 = m.DecimalNumber(3).move_to(0.59*m.UP + 4.02*m.LEFT)
        t2 = m.DecimalNumber(85).move_to(0.59*m.UP + 2.11*m.LEFT)
        t3 = m.DecimalNumber(18540).move_to(0.59*m.UP + 0.2*m.RIGHT)
        t4 = m.DecimalNumber(0.0812, num_decimal_places = 4).move_to(0.59*m.UP + 3.16*m.RIGHT)
        t = m.VGroup(t1, t2, t3, t4)

        midtab = m.VGroup(mid, midU, midD, midL, midR, h, d, t)

        deltab = m.Table(
            [[],
            [],
            [],
            [],
            [],
            [],
            [],
            []],
            top_left_entry = m.Tex("Delinquency"),
            col_labels = [],
            row_labels = [m.DecimalNumber(0),
                          m.DecimalNumber(1),
                          m.DecimalNumber(0),
                          m.DecimalNumber(1),
                          m.DecimalNumber(1),
                          m.DecimalNumber(0),
                          m.DecimalNumber(1),
                          m.MathTex("\\vdots")],
            v_buff = 0.305
        ).move_to(0.02*m.UP + 5.24*m.RIGHT)

        delU = m.Line(
            start = 2.75*m.UP + 3.87*m.RIGHT,
            end = 2.75*m.UP + 6.6*m.RIGHT
        )

        delL = m.Line(
            start = 2.75*m.UP + 3.87*m.RIGHT,
            end = 2.7*m.DOWN + 3.87*m.RIGHT
        )

        delR = m.Line(
            start = 2.75*m.UP + 6.6*m.RIGHT,
            end = 2.7*m.DOWN + 6.6*m.RIGHT
        )

        delinquency = m.VGroup(deltab, delU, delL, delR)

        valX1 = tabU.get_entries_without_labels().copy()
        valX2 = t.copy()
        valX2.remove(valX2[0])
        valX3 = mid.get_entries_without_labels().copy()
        valX4 = d.copy()
        valX5 = vdots.copy()
        valX5.remove(valX5[0]).shift(2.95*m.DOWN)
        valX = m.VGroup(valX1, valX2, valX3, valX4, valX5).shift(1.65*m.LEFT)
        valy = deltab.get_row_labels().copy().shift(0.2*m.RIGHT)

        col1 = m.VGroup(valX1[0::4], valX2[0], valX3[0::3], valX5[0])
        col2 = m.VGroup(valX1[1::4], valX2[1], valX3[1::3], valX5[1])
        col3 = m.VGroup(valX1[2::4], valX2[2], valX3[2::3], valX5[2])
        col4 = m.VGroup(valX1[3::4], valX4, valX5[3])

        X = m.MathTex("X").move_to(valX1[0].get_center() + 2*m.LEFT)
        eqX = m.MathTex("=").move_to(X.get_center() + 0.5*m.RIGHT)
        bX1 = m.MathTex("[").move_to(col1[0][0].get_center() + 0.9*m.LEFT)
        bX0 = bX1.copy().shift(0.2*m.LEFT)
        bX2 = m.MathTex("]").move_to(col4[0][0].get_center() + 2.6*m.LEFT)
        bX3 = bX1.copy().move_to(col1[0][1].get_center() + 0.9*m.LEFT)
        bX4 = bX2.copy().move_to(col4[0][1].get_center() + 2.6*m.LEFT)
        bX5 = bX1.copy().move_to(col1[1].get_center() + 0.9*m.LEFT)
        bX6 = bX2.copy().move_to(col4[1][0].get_center() + 2.6*m.LEFT)
        bX7 = bX1.copy().move_to(col1[2][0].get_center() + 0.9*m.LEFT)
        bX8 = bX2.copy().move_to(col4[1][1].get_center() + 2.6*m.LEFT)
        bX9 = bX1.copy().move_to(col1[2][1].get_center() + 0.9*m.LEFT)
        bX10 = bX2.copy().move_to(col4[1][2].get_center() + 2.6*m.LEFT)
        bX11 = bX1.copy().move_to(col1[2][2].get_center() + 0.9*m.LEFT)
        bX12 = bX2.copy().move_to(col4[1][3].get_center() + 2.6*m.LEFT)
        bX13 = bX1.copy().move_to(col1[2][3].get_center() + 0.9*m.LEFT)
        bX14 = bX2.copy().move_to(col4[1][4].get_center() + 2.6*m.LEFT)
        bX15 = bX1.copy().move_to(col1[3].get_center() + 0.9*m.LEFT)
        bX16 = bX2.copy().move_to(col4[2].get_center() + 2.6*m.LEFT)
        bX17 = bX16.copy().shift(0.2*m.RIGHT)
        bX = m.VGroup(X, eqX, bX0, bX1, bX2, bX3, bX4, bX5, bX6, bX7, bX8,
                      bX9, bX10, bX11, bX12, bX13, bX14, bX15, bX16, bX17)

        y = m.MathTex("y").move_to(valy[0].get_center() + 1.5*m.LEFT)
        eqy = m.MathTex("=").move_to(y.get_center() + 0.5*m.RIGHT)
        by1 = m.MathTex("[").move_to(valy[0].get_center() + 0.4*m.LEFT)
        by0 = by1.copy().shift(0.2*m.LEFT)
        by2 = m.MathTex("]").move_to(valy[0].get_center() + 0.4*m.RIGHT)
        by3 = by1.copy().move_to(valy[1].get_center() + 0.4*m.LEFT)
        by4 = by2.copy().move_to(valy[1].get_center() + 0.4*m.RIGHT)
        by5 = by1.copy().move_to(valy[2].get_center() + 0.4*m.LEFT)
        by6 = by2.copy().move_to(valy[2].get_center() + 0.4*m.RIGHT)
        by7 = by1.copy().move_to(valy[3].get_center() + 0.4*m.LEFT)
        by8 = by2.copy().move_to(valy[3].get_center() + 0.4*m.RIGHT)
        by9 = by1.copy().move_to(valy[4].get_center() + 0.4*m.LEFT)
        by10 = by2.copy().move_to(valy[4].get_center() + 0.4*m.RIGHT)
        by11 = by1.copy().move_to(valy[5].get_center() + 0.4*m.LEFT)
        by12 = by2.copy().move_to(valy[5].get_center() + 0.4*m.RIGHT)
        by13 = by1.copy().move_to(valy[6].get_center() + 0.4*m.LEFT)
        by14 = by2.copy().move_to(valy[6].get_center() + 0.4*m.RIGHT)
        by15 = by1.copy().move_to(valy[7].get_center() + 0.4*m.LEFT)
        by16 = by2.copy().move_to(valy[7].get_center() + 0.4*m.RIGHT)
        by17 = by16.copy().shift(0.2*m.RIGHT)
        by = m.VGroup(y, eqy, by0, by1, by2, by3, by4, by5, by6, by7, by8,
                      by9, by10, by11, by12, by13, by14, by15, by16, by17)

        self.play(
            m.FadeIn(tab, low, lowtab, tabDL)
        )
        self.wait()
        self.play(
            m.FadeOut(tabDL)
        )
        self.play(
            lowtab.animate.shift(2.95*m.DOWN),
            m.Transform(low, midtab)
        )
        self.wait()
        self.play(
            tab.animate.shift(1.45*m.LEFT),
            low.animate.shift(1.45*m.LEFT),
            lowtab.animate.shift(1.45*m.LEFT),
            m.FadeIn(delinquency)
        )
        self.wait()
        self.play(
            tab.animate.shift(0.2*m.LEFT),
            low.animate.shift(0.2*m.LEFT),
            lowtab.animate.shift(0.2*m.LEFT),
            delinquency.animate.shift(0.2*m.RIGHT)
        )
        self.wait()
        self.add(valX, valy)
        self.play(
            m.FadeOut(tab, low, lowtab, delinquency)
        )
        self.play(
            col1.animate.shift(0.5*m.LEFT),
            col2.animate.shift(1.5*m.LEFT),
            col3.animate.shift(2.7*m.LEFT),
            col4.animate.shift(3*m.LEFT),
            m.Create(bX),
            m.Create(by)
        )
        self.wait()
# ---------------------------------------------------------------------------
class Cell10(m.Scene):
    def construct(self):

        tabU = m.Table(
            [["45", "9120", "0.3241", "\\dots"],
            ["52", "2600", "0.8544", "\\dots"]],
            top_left_entry = m.Tex("TRAINING"),
            col_labels = [m.Tex("Age"),
                          m.Tex("Monthly Income"),
                          m.Tex("Debt Ratio"),
                          m.MathTex("\\dots")],
            row_labels = [m.DecimalNumber(1),
                          m.DecimalNumber(2)]
        ).move_to(1.82*m.UP)

        lU = m.Line(
            start = 2.75*m.UP + 5.32*m.LEFT,
            end = 2.75*m.UP + 5.32*m.RIGHT
        )
        lUL = m.Line(
            start = 2.75*m.UP + 5.32*m.LEFT,
            end = 0.9*m.UP + 5.32*m.LEFT
        )

        tabD = m.Table(
            [["23", "12508", "0.0865", "\\dots"],
            ["68", "8760", "0.2219", "\\dots"],
            ["\\vdots", "\\vdots", "\\vdots", "\\ddots"]],
            top_left_entry = m.Tex("TRAINING", fill_opacity = 0.0),
            col_labels = [m.Tex("Age"),
                          m.Tex("Monthly Income"),
                          m.Tex("Debt Ratio"),
                          m.MathTex("\\dots")],
            row_labels = [m.DecimalNumber(1),
                          m.DecimalNumber(2),
                          m.MathTex("\\vdots")]
        ).move_to(1.5*m.DOWN)

        testing = m.Tex("TEST").move_to(0.58*m.DOWN + 4.02*m.LEFT)

        lD = m.Line(
            start = 0.25*m.DOWN + 5.32*m.LEFT,
            end = 0.25*m.DOWN + 5.32*m.RIGHT
        )
        lDL = m.Line(
            start = 0.25*m.DOWN + 5.32*m.LEFT,
            end = 2.75*m.DOWN + 5.32*m.LEFT
        )

        tab = m.VGroup(tabU, lU, lUL)
        tabDL = m.VGroup(testing, tabD, lD, lDL)

        low = m.Line(
            start = 0.9*m.UP + 5.32*m.LEFT,
            end = 0.9*m.UP + 5.32*m.RIGHT
        )

        vline1 = m.Line(
            start = 0.9*m.UP + 5.32*m.LEFT,
            end = 0.25*m.UP + 5.32*m.LEFT
        )
        vline2 = m.Line(
            start = 0.9*m.UP + 2.7*m.LEFT,
            end = 0.25*m.UP + 2.7*m.LEFT
        )
        vline3 = m.Line(
            start = 0.9*m.UP + 1.52*m.LEFT,
            end = 0.25*m.UP + 1.52*m.LEFT
        )
        vline4 = m.Line(
            start = 0.9*m.UP + 1.92*m.RIGHT,
            end = 0.25*m.UP + 1.92*m.RIGHT
        )
        vline5 = m.Line(
            start = 0.9*m.UP + 4.42*m.RIGHT,
            end = 0.25*m.UP + 4.42*m.RIGHT
        )
        vlines = m.VGroup(vline1, vline2, vline3, vline4, vline5)

        vdots1 = m.MathTex("\\vdots").move_to(0.58*m.UP + 4.02*m.LEFT)
        vdots2 = m.MathTex("\\vdots").move_to(0.58*m.UP + 2.11*m.LEFT)
        vdots3 = m.MathTex("\\vdots").move_to(0.58*m.UP + 0.2*m.RIGHT)
        vdots4 = m.MathTex("\\vdots").move_to(0.58*m.UP + 3.16*m.RIGHT)
        ddots = m.MathTex("\\ddots").move_to(0.58*m.UP + 4.87*m.RIGHT)
        vdots = m.VGroup(vdots1, vdots2, vdots3, vdots4, ddots)

        lowtab = m.VGroup(vlines, vdots)

        mid = m.Table(
            [["77", "4062", "0.3674"],
            ["32", "13985", "0.8612"],
            ["24", "6210", "0.5143"],
            ["63", "3375", "0.9412"]],
            top_left_entry = m.Tex("TRAINING", fill_opacity = 0.0),
            col_labels = [m.Tex("Age", fill_opacity = 0.0),
                          m.Tex("Monthly Income", fill_opacity = 0.0),
                          m.Tex("Debt Ratio", fill_opacity = 0.0)],
            row_labels = [m.DecimalNumber(4),
                          m.DecimalNumber(5),
                          m.DecimalNumber(6),
                          m.DecimalNumber(7)]
        ).move_to(0.525*m.DOWN + 0.455*m.LEFT)

        midU = m.Line(
            start = 0.9*m.UP + 5.32*m.LEFT,
            end = 0.9*m.UP + 5.32*m.RIGHT
        )
        midD = m.Line(
            start = 2.05*m.DOWN + 5.32*m.LEFT,
            end = 2.05*m.DOWN + 5.32*m.RIGHT
        )
        midL = m.Line(
            start = 0.9*m.UP + 5.32*m.LEFT,
            end = 2.05*m.DOWN + 5.32*m.LEFT
        )
        midR = m.Line(
            start = 0.9*m.UP + 4.42*m.RIGHT,
            end = 2.05*m.DOWN + 4.42*m.RIGHT
        )

        h1 = m.Line(
            start = 0.31*m.UP + 4.42*m.RIGHT,
            end = 0.31*m.UP + 5.32*m.RIGHT
        )
        h2 = h1.copy().shift(0.585*m.DOWN)
        h3 = h2.copy().shift(0.585*m.DOWN)
        h4 = h3.copy().shift(0.585*m.DOWN)
        h = m.VGroup(h1, h2, h3, h4)

        d1 = m.MathTex("\\dots").move_to(0.59*m.UP + 4.87*m.RIGHT)
        d2 = d1.copy().shift(0.585*m.DOWN)
        d3 = d2.copy().shift(0.585*m.DOWN)
        d4 = d3.copy().shift(0.585*m.DOWN)
        d5 = d4.copy().shift(0.585*m.DOWN)
        d = m.VGroup(d1, d2, d3, d4, d5)

        t1 = m.DecimalNumber(3).move_to(0.59*m.UP + 4.02*m.LEFT)
        t2 = m.DecimalNumber(85).move_to(0.59*m.UP + 2.11*m.LEFT)
        t3 = m.DecimalNumber(18540).move_to(0.59*m.UP + 0.2*m.RIGHT)
        t4 = m.DecimalNumber(0.0812, num_decimal_places = 4).move_to(0.59*m.UP + 3.16*m.RIGHT)
        t = m.VGroup(t1, t2, t3, t4)

        midtab = m.VGroup(mid, midU, midD, midL, midR, h, d, t)

        deltab = m.Table(
            [[],
            [],
            [],
            [],
            [],
            [],
            [],
            []],
            top_left_entry = m.Tex("Delinquency"),
            col_labels = [],
            row_labels = [m.DecimalNumber(0),
                          m.DecimalNumber(1),
                          m.DecimalNumber(0),
                          m.DecimalNumber(1),
                          m.DecimalNumber(1),
                          m.DecimalNumber(0),
                          m.DecimalNumber(1),
                          m.MathTex("\\vdots")],
            v_buff = 0.305
        ).move_to(0.02*m.UP + 5.24*m.RIGHT)

        delU = m.Line(
            start = 2.75*m.UP + 3.87*m.RIGHT,
            end = 2.75*m.UP + 6.6*m.RIGHT
        )

        delL = m.Line(
            start = 2.75*m.UP + 3.87*m.RIGHT,
            end = 2.7*m.DOWN + 3.87*m.RIGHT
        )

        delinquency = m.VGroup(deltab, delU, delL)

        valX1 = tabU.get_entries_without_labels().copy()
        valX2 = t.copy()
        valX2.remove(valX2[0])
        valX3 = mid.get_entries_without_labels().copy()
        valX4 = d.copy()
        valX5 = vdots.copy()
        valX5.remove(valX5[0]).shift(2.95*m.DOWN)
        valX = m.VGroup(valX1, valX2, valX3, valX4, valX5).shift(1.65*m.LEFT)
        valy = deltab.get_row_labels().copy().shift(0.2*m.RIGHT)

        col1 = m.VGroup(valX1[0::4], valX2[0], valX3[0::3], valX5[0])
        col2 = m.VGroup(valX1[1::4], valX2[1], valX3[1::3], valX5[1])
        col3 = m.VGroup(valX1[2::4], valX2[2], valX3[2::3], valX5[2])
        col4 = m.VGroup(valX1[3::4], valX4, valX5[3])

        X = m.MathTex("X").move_to(valX1[0].get_center() + 2*m.LEFT)
        eqX = m.MathTex("=").move_to(X.get_center() + 0.5*m.RIGHT)
        bX1 = m.MathTex("[").move_to(col1[0][0].get_center() + 0.9*m.LEFT)
        bX0 = bX1.copy().shift(0.2*m.LEFT)
        bX2 = m.MathTex("]").move_to(col4[0][0].get_center() + 2.6*m.LEFT)
        bX3 = bX1.copy().move_to(col1[0][1].get_center() + 0.9*m.LEFT)
        bX4 = bX2.copy().move_to(col4[0][1].get_center() + 2.6*m.LEFT)
        bX5 = bX1.copy().move_to(col1[1].get_center() + 0.9*m.LEFT)
        bX6 = bX2.copy().move_to(col4[1][0].get_center() + 2.6*m.LEFT)
        bX7 = bX1.copy().move_to(col1[2][0].get_center() + 0.9*m.LEFT)
        bX8 = bX2.copy().move_to(col4[1][1].get_center() + 2.6*m.LEFT)
        bX9 = bX1.copy().move_to(col1[2][1].get_center() + 0.9*m.LEFT)
        bX10 = bX2.copy().move_to(col4[1][2].get_center() + 2.6*m.LEFT)
        bX11 = bX1.copy().move_to(col1[2][2].get_center() + 0.9*m.LEFT)
        bX12 = bX2.copy().move_to(col4[1][3].get_center() + 2.6*m.LEFT)
        bX13 = bX1.copy().move_to(col1[2][3].get_center() + 0.9*m.LEFT)
        bX14 = bX2.copy().move_to(col4[1][4].get_center() + 2.6*m.LEFT)
        bX15 = bX1.copy().move_to(col1[3].get_center() + 0.9*m.LEFT)
        bX16 = bX2.copy().move_to(col4[2].get_center() + 2.6*m.LEFT)
        bX17 = bX16.copy().shift(0.2*m.RIGHT)
        bX = m.VGroup(X, eqX, bX0, bX1, bX2, bX3, bX4, bX5, bX6, bX7, bX8,
                      bX9, bX10, bX11, bX12, bX13, bX14, bX15, bX16, bX17)

        y = m.MathTex("y").move_to(valy[0].get_center() + 1.5*m.LEFT)
        eqy = m.MathTex("=").move_to(y.get_center() + 0.5*m.RIGHT)
        by1 = m.MathTex("[").move_to(valy[0].get_center() + 0.4*m.LEFT)
        by0 = by1.copy().shift(0.2*m.LEFT)
        by2 = m.MathTex("]").move_to(valy[0].get_center() + 0.4*m.RIGHT)
        by3 = by1.copy().move_to(valy[1].get_center() + 0.4*m.LEFT)
        by4 = by2.copy().move_to(valy[1].get_center() + 0.4*m.RIGHT)
        by5 = by1.copy().move_to(valy[2].get_center() + 0.4*m.LEFT)
        by6 = by2.copy().move_to(valy[2].get_center() + 0.4*m.RIGHT)
        by7 = by1.copy().move_to(valy[3].get_center() + 0.4*m.LEFT)
        by8 = by2.copy().move_to(valy[3].get_center() + 0.4*m.RIGHT)
        by9 = by1.copy().move_to(valy[4].get_center() + 0.4*m.LEFT)
        by10 = by2.copy().move_to(valy[4].get_center() + 0.4*m.RIGHT)
        by11 = by1.copy().move_to(valy[5].get_center() + 0.4*m.LEFT)
        by12 = by2.copy().move_to(valy[5].get_center() + 0.4*m.RIGHT)
        by13 = by1.copy().move_to(valy[6].get_center() + 0.4*m.LEFT)
        by14 = by2.copy().move_to(valy[6].get_center() + 0.4*m.RIGHT)
        by15 = by1.copy().move_to(valy[7].get_center() + 0.4*m.LEFT)
        by16 = by2.copy().move_to(valy[7].get_center() + 0.4*m.RIGHT)
        by17 = by16.copy().shift(0.2*m.RIGHT)
        by = m.VGroup(y, eqy, by0, by1, by2, by3, by4, by5, by6, by7, by8,
                      by9, by10, by11, by12, by13, by14, by15, by16, by17)

        col1.shift(0.5*m.LEFT)
        col2.shift(1.5*m.LEFT)
        col3.shift(2.7*m.LEFT)
        col4.shift(3*m.LEFT)

        r1 = m.DecimalNumber(1).move_to(bX2.get_center() + 1*m.RIGHT)
        r2 = m.DecimalNumber(2).move_to(bX4.get_center() + 1*m.RIGHT)
        r3 = m.DecimalNumber(3).move_to(bX6.get_center() + 1*m.RIGHT)
        r4 = m.DecimalNumber(4).move_to(bX8.get_center() + 1*m.RIGHT)
        r5 = m.DecimalNumber(5).move_to(bX10.get_center() + 1*m.RIGHT)
        r6 = m.DecimalNumber(6).move_to(bX12.get_center() + 1*m.RIGHT)
        r7 = m.DecimalNumber(7).move_to(bX14.get_center() + 1*m.RIGHT)
        r8 = m.MathTex("\\vdots").move_to(bX16.get_center() + 1*m.RIGHT)
        r = m.VGroup(r1, r2, r3, r4, r5, r6, r7, r8)

        r8h = m.MathTex("\\dots").move_to(3.5*m.RIGHT)

        r1r = m.DecimalNumber(364).move_to(3.5*m.LEFT)
        r2r = m.DecimalNumber(992).move_to(2.5*m.LEFT)
        r3r = m.DecimalNumber(846).move_to(1.5*m.LEFT)
        r4r = m.DecimalNumber(752).move_to(0.5*m.LEFT)
        r5r = m.DecimalNumber(926).move_to(0.5*m.RIGHT)
        r6r = m.DecimalNumber(71).move_to(1.5*m.RIGHT)
        r7r = m.DecimalNumber(106).move_to(2.5*m.RIGHT)

        r9 = m.MathTex("\\dots").move_to(0.5*m.RIGHT)

        it = m.VGroup(r1, r2, r3, r4, r5, r9)
        iv = m.VGroup(r6, r7, r8)

        sw = 10
        m.ArcBetweenPoints.set_default(
            color = c,
            stroke_width = sw
        )

        rad = 4
        h = rad - np.sin(np.pi/4)*rad
        d = np.cos(np.pi/4)*rad

        arcUL = m.ArcBetweenPoints(
            start = d*m.LEFT + h*m.UP,
            end = m.ORIGIN,
            radius = -rad
        )
        arcUR = m.ArcBetweenPoints(
            start = m.ORIGIN,
            end = d*m.RIGHT + h*m.UP,
            radius = -rad
        )
        arcDL = m.ArcBetweenPoints(
            start = d*m.LEFT + h*m.DOWN,
            end = m.ORIGIN,
            radius = rad
        )
        arcDR = m.ArcBetweenPoints(
            start = m.ORIGIN,
            end = d*m.RIGHT + h*m.DOWN,
            radius = rad
        )
        atU = m.Triangle(
            color = c,
            fill_opacity = 1.0
        ).rotate(np.pi/6).scale(0.5).move_to(d*m.RIGHT + h*m.UP)
        atD = m.Triangle(
            color = c,
            fill_opacity = 1.0
        ).rotate(np.pi/6).scale(0.5).move_to(d*m.RIGHT + h*m.DOWN)

        perm = m.VGroup(arcUL, arcUR, arcDL, arcDR, atU, atD).scale(0.3).move_to(1.5*m.UP)

        rect80 = m.Rectangle(
            width = 6.0,
            height = 1.0,
            color = m.BLUE,
            fill_opacity = 0.5
        ).move_to(2*m.LEFT)
        tex80 = m.MathTex("80\\%").move_to(1*m.UP + 2*m.LEFT)

        rect20 = m.Rectangle(
            width = 3.0,
            height = 1.0,
            color = m.YELLOW,
            fill_opacity = 0.5
        ).move_to(3.5*m.RIGHT)
        tex20 = m.MathTex("20\\%").move_to(1*m.UP + 3.5*m.RIGHT)
        
        self.play(
            m.FadeIn(valX, valy, bX, by)
        )
        self.wait()
        self.play(
            m.Create(r)
        )
        self.wait()
        self.play(
            m.FadeOut(valX, valy, bX, by),
            r1.animate.move_to(3.5*m.LEFT),
            r2.animate.move_to(2.5*m.LEFT),
            r3.animate.move_to(1.5*m.LEFT),
            r4.animate.move_to(0.5*m.LEFT),
            r5.animate.move_to(0.5*m.RIGHT),
            r6.animate.move_to(1.5*m.RIGHT),
            r7.animate.move_to(2.5*m.RIGHT),
            m.Transform(r8, r8h)
        )
        self.wait()
        self.play(
            m.FadeIn(perm, rate_func = m.rate_functions.there_and_back),
            m.Transform(r1, r1r),
            m.Transform(r2, r2r),
            m.Transform(r3, r3r),
            m.Transform(r4, r4r),
            m.Transform(r5, r5r),
            m.Transform(r6, r6r),
            m.Transform(r7, r7r)
        )
        self.wait()
        self.play(
            m.FadeOut(perm),
            it.animate.shift(1*m.LEFT),
            iv.animate.shift(1*m.RIGHT),
            m.Write(r9)
        )
        self.wait()
        self.play(
            m.FadeIn(rect80, rect20),
            m.Write(tex80),
            m.Write(tex20)
        )
        self.wait()
# ---------------------------------------------------------------------------
class Cell11(m.Scene):
    def construct(self):

        tabU = m.Table(
            [["45", "9120", "0.3241", "\\dots"],
            ["52", "2600", "0.8544", "\\dots"]],
            top_left_entry = m.Tex("TRAINING"),
            col_labels = [m.Tex("Age"),
                          m.Tex("Monthly Income"),
                          m.Tex("Debt Ratio"),
                          m.MathTex("\\dots")],
            row_labels = [m.DecimalNumber(1),
                          m.DecimalNumber(2)]
        ).move_to(1.82*m.UP)

        lU = m.Line(
            start = 2.75*m.UP + 5.32*m.LEFT,
            end = 2.75*m.UP + 5.32*m.RIGHT
        )
        lUL = m.Line(
            start = 2.75*m.UP + 5.32*m.LEFT,
            end = 0.9*m.UP + 5.32*m.LEFT
        )

        tabD = m.Table(
            [["23", "12508", "0.0865", "\\dots"],
            ["68", "8760", "0.2219", "\\dots"],
            ["\\vdots", "\\vdots", "\\vdots", "\\ddots"]],
            top_left_entry = m.Tex("TRAINING", fill_opacity = 0.0),
            col_labels = [m.Tex("Age"),
                          m.Tex("Monthly Income"),
                          m.Tex("Debt Ratio"),
                          m.MathTex("\\dots")],
            row_labels = [m.DecimalNumber(1),
                          m.DecimalNumber(2),
                          m.MathTex("\\vdots")]
        ).move_to(1.5*m.DOWN)

        testing = m.Tex("TEST").move_to(0.58*m.DOWN + 4.02*m.LEFT)

        lD = m.Line(
            start = 0.25*m.DOWN + 5.32*m.LEFT,
            end = 0.25*m.DOWN + 5.32*m.RIGHT
        )
        lDL = m.Line(
            start = 0.25*m.DOWN + 5.32*m.LEFT,
            end = 2.75*m.DOWN + 5.32*m.LEFT
        )

        tab = m.VGroup(tabU, lU, lUL)
        tabDL = m.VGroup(testing, tabD, lD, lDL)

        low = m.Line(
            start = 0.9*m.UP + 5.32*m.LEFT,
            end = 0.9*m.UP + 5.32*m.RIGHT
        )

        vline1 = m.Line(
            start = 0.9*m.UP + 5.32*m.LEFT,
            end = 0.25*m.UP + 5.32*m.LEFT
        )
        vline2 = m.Line(
            start = 0.9*m.UP + 2.7*m.LEFT,
            end = 0.25*m.UP + 2.7*m.LEFT
        )
        vline3 = m.Line(
            start = 0.9*m.UP + 1.52*m.LEFT,
            end = 0.25*m.UP + 1.52*m.LEFT
        )
        vline4 = m.Line(
            start = 0.9*m.UP + 1.92*m.RIGHT,
            end = 0.25*m.UP + 1.92*m.RIGHT
        )
        vline5 = m.Line(
            start = 0.9*m.UP + 4.42*m.RIGHT,
            end = 0.25*m.UP + 4.42*m.RIGHT
        )
        vlines = m.VGroup(vline1, vline2, vline3, vline4, vline5)

        vdots1 = m.MathTex("\\vdots").move_to(0.58*m.UP + 4.02*m.LEFT)
        vdots2 = m.MathTex("\\vdots").move_to(0.58*m.UP + 2.11*m.LEFT)
        vdots3 = m.MathTex("\\vdots").move_to(0.58*m.UP + 0.2*m.RIGHT)
        vdots4 = m.MathTex("\\vdots").move_to(0.58*m.UP + 3.16*m.RIGHT)
        ddots = m.MathTex("\\ddots").move_to(0.58*m.UP + 4.87*m.RIGHT)
        vdots = m.VGroup(vdots1, vdots2, vdots3, vdots4, ddots)

        lowtab = m.VGroup(vlines, vdots)

        mid = m.Table(
            [["77", "4062", "0.3674"],
            ["32", "13985", "0.8612"],
            ["24", "6210", "0.5143"],
            ["63", "3375", "0.9412"]],
            top_left_entry = m.Tex("TRAINING", fill_opacity = 0.0),
            col_labels = [m.Tex("Age", fill_opacity = 0.0),
                          m.Tex("Monthly Income", fill_opacity = 0.0),
                          m.Tex("Debt Ratio", fill_opacity = 0.0)],
            row_labels = [m.DecimalNumber(4),
                          m.DecimalNumber(5),
                          m.DecimalNumber(6),
                          m.DecimalNumber(7)]
        ).move_to(0.525*m.DOWN + 0.455*m.LEFT)

        midU = m.Line(
            start = 0.9*m.UP + 5.32*m.LEFT,
            end = 0.9*m.UP + 5.32*m.RIGHT
        )
        midD = m.Line(
            start = 2.05*m.DOWN + 5.32*m.LEFT,
            end = 2.05*m.DOWN + 5.32*m.RIGHT
        )
        midL = m.Line(
            start = 0.9*m.UP + 5.32*m.LEFT,
            end = 2.05*m.DOWN + 5.32*m.LEFT
        )
        midR = m.Line(
            start = 0.9*m.UP + 4.42*m.RIGHT,
            end = 2.05*m.DOWN + 4.42*m.RIGHT
        )

        h1 = m.Line(
            start = 0.31*m.UP + 4.42*m.RIGHT,
            end = 0.31*m.UP + 5.32*m.RIGHT
        )
        h2 = h1.copy().shift(0.585*m.DOWN)
        h3 = h2.copy().shift(0.585*m.DOWN)
        h4 = h3.copy().shift(0.585*m.DOWN)
        h = m.VGroup(h1, h2, h3, h4)

        d1 = m.MathTex("\\dots").move_to(0.59*m.UP + 4.87*m.RIGHT)
        d2 = d1.copy().shift(0.585*m.DOWN)
        d3 = d2.copy().shift(0.585*m.DOWN)
        d4 = d3.copy().shift(0.585*m.DOWN)
        d5 = d4.copy().shift(0.585*m.DOWN)
        d = m.VGroup(d1, d2, d3, d4, d5)

        t1 = m.DecimalNumber(3).move_to(0.59*m.UP + 4.02*m.LEFT)
        t2 = m.DecimalNumber(85).move_to(0.59*m.UP + 2.11*m.LEFT)
        t3 = m.DecimalNumber(18540).move_to(0.59*m.UP + 0.2*m.RIGHT)
        t4 = m.DecimalNumber(0.0812, num_decimal_places = 4).move_to(0.59*m.UP + 3.16*m.RIGHT)
        t = m.VGroup(t1, t2, t3, t4)

        midtab = m.VGroup(mid, midU, midD, midL, midR, h, d, t)

        deltab = m.Table(
            [[],
            [],
            [],
            [],
            [],
            [],
            [],
            []],
            top_left_entry = m.Tex("Delinquency"),
            col_labels = [],
            row_labels = [m.DecimalNumber(0),
                          m.DecimalNumber(1),
                          m.DecimalNumber(0),
                          m.DecimalNumber(1),
                          m.DecimalNumber(1),
                          m.DecimalNumber(0),
                          m.DecimalNumber(1),
                          m.MathTex("\\vdots")],
            v_buff = 0.305
        ).move_to(0.02*m.UP + 5.24*m.RIGHT)

        delU = m.Line(
            start = 2.75*m.UP + 3.87*m.RIGHT,
            end = 2.75*m.UP + 6.6*m.RIGHT
        )

        delL = m.Line(
            start = 2.75*m.UP + 3.87*m.RIGHT,
            end = 2.7*m.DOWN + 3.87*m.RIGHT
        )

        delinquency = m.VGroup(deltab, delU, delL)

        valX1 = tabU.get_entries_without_labels().copy()
        valX2 = t.copy()
        valX2.remove(valX2[0])
        valX3 = mid.get_entries_without_labels().copy()
        valX4 = d.copy()
        valX5 = vdots.copy()
        valX5.remove(valX5[0]).shift(2.95*m.DOWN)
        valX = m.VGroup(valX1, valX2, valX3, valX4, valX5).shift(1.65*m.LEFT)
        valy = deltab.get_row_labels().copy().shift(0.2*m.RIGHT)

        col1 = m.VGroup(valX1[0::4], valX2[0], valX3[0::3], valX5[0])
        col2 = m.VGroup(valX1[1::4], valX2[1], valX3[1::3], valX5[1])
        col3 = m.VGroup(valX1[2::4], valX2[2], valX3[2::3], valX5[2])
        col4 = m.VGroup(valX1[3::4], valX4, valX5[3])

        X = m.MathTex("X").move_to(valX1[0].get_center() + 2*m.LEFT)
        eqX = m.MathTex("=").move_to(X.get_center() + 0.5*m.RIGHT)
        bX1 = m.MathTex("[").move_to(col1[0][0].get_center() + 0.9*m.LEFT)
        bX0 = bX1.copy().shift(0.2*m.LEFT)
        bX2 = m.MathTex("]").move_to(col4[0][0].get_center() + 2.6*m.LEFT)
        bX3 = bX1.copy().move_to(col1[0][1].get_center() + 0.9*m.LEFT)
        bX4 = bX2.copy().move_to(col4[0][1].get_center() + 2.6*m.LEFT)
        bX5 = bX1.copy().move_to(col1[1].get_center() + 0.9*m.LEFT)
        bX6 = bX2.copy().move_to(col4[1][0].get_center() + 2.6*m.LEFT)
        bX7 = bX1.copy().move_to(col1[2][0].get_center() + 0.9*m.LEFT)
        bX8 = bX2.copy().move_to(col4[1][1].get_center() + 2.6*m.LEFT)
        bX9 = bX1.copy().move_to(col1[2][1].get_center() + 0.9*m.LEFT)
        bX10 = bX2.copy().move_to(col4[1][2].get_center() + 2.6*m.LEFT)
        bX11 = bX1.copy().move_to(col1[2][2].get_center() + 0.9*m.LEFT)
        bX12 = bX2.copy().move_to(col4[1][3].get_center() + 2.6*m.LEFT)
        bX13 = bX1.copy().move_to(col1[2][3].get_center() + 0.9*m.LEFT)
        bX14 = bX2.copy().move_to(col4[1][4].get_center() + 2.6*m.LEFT)
        bX15 = bX1.copy().move_to(col1[3].get_center() + 0.9*m.LEFT)
        bX16 = bX2.copy().move_to(col4[2].get_center() + 2.6*m.LEFT)
        bX17 = bX16.copy().shift(0.2*m.RIGHT)
        bX = m.VGroup(X, eqX, bX0, bX1, bX2, bX3, bX4, bX5, bX6, bX7, bX8,
                      bX9, bX10, bX11, bX12, bX13, bX14, bX15, bX16, bX17)

        y = m.MathTex("y").move_to(valy[0].get_center() + 1.5*m.LEFT)
        eqy = m.MathTex("=").move_to(y.get_center() + 0.5*m.RIGHT)
        by1 = m.MathTex("[").move_to(valy[0].get_center() + 0.4*m.LEFT)
        by0 = by1.copy().shift(0.2*m.LEFT)
        by2 = m.MathTex("]").move_to(valy[0].get_center() + 0.4*m.RIGHT)
        by3 = by1.copy().move_to(valy[1].get_center() + 0.4*m.LEFT)
        by4 = by2.copy().move_to(valy[1].get_center() + 0.4*m.RIGHT)
        by5 = by1.copy().move_to(valy[2].get_center() + 0.4*m.LEFT)
        by6 = by2.copy().move_to(valy[2].get_center() + 0.4*m.RIGHT)
        by7 = by1.copy().move_to(valy[3].get_center() + 0.4*m.LEFT)
        by8 = by2.copy().move_to(valy[3].get_center() + 0.4*m.RIGHT)
        by9 = by1.copy().move_to(valy[4].get_center() + 0.4*m.LEFT)
        by10 = by2.copy().move_to(valy[4].get_center() + 0.4*m.RIGHT)
        by11 = by1.copy().move_to(valy[5].get_center() + 0.4*m.LEFT)
        by12 = by2.copy().move_to(valy[5].get_center() + 0.4*m.RIGHT)
        by13 = by1.copy().move_to(valy[6].get_center() + 0.4*m.LEFT)
        by14 = by2.copy().move_to(valy[6].get_center() + 0.4*m.RIGHT)
        by15 = by1.copy().move_to(valy[7].get_center() + 0.4*m.LEFT)
        by16 = by2.copy().move_to(valy[7].get_center() + 0.4*m.RIGHT)
        by17 = by16.copy().shift(0.2*m.RIGHT)
        by = m.VGroup(y, eqy, by0, by1, by2, by3, by4, by5, by6, by7, by8,
                      by9, by10, by11, by12, by13, by14, by15, by16, by17)

        col1.shift(0.5*m.LEFT)
        col2.shift(1.5*m.LEFT)
        col3.shift(2.7*m.LEFT)
        col4.shift(3*m.LEFT)

        r1 = m.DecimalNumber(364).move_to(4.5*m.LEFT)
        r2 = m.DecimalNumber(992).move_to(3.5*m.LEFT)
        r3 = m.DecimalNumber(846).move_to(2.5*m.LEFT)
        r4 = m.DecimalNumber(752).move_to(1.5*m.LEFT)
        r5 = m.DecimalNumber(926).move_to(0.5*m.LEFT)
        r6 = m.DecimalNumber(71).move_to(2.5*m.RIGHT)
        r7 = m.DecimalNumber(106).move_to(3.5*m.RIGHT)
        r8 = m.MathTex("\\dots").move_to(4.5*m.RIGHT)
        r9 = m.MathTex("\\dots").move_to(0.5*m.RIGHT)

        it = m.VGroup(r1, r2, r3, r4, r5, r9)
        iv = m.VGroup(r6, r7, r8)

        rect80 = m.Rectangle(
            width = 6.0,
            height = 1.0,
            color = m.BLUE,
            fill_opacity = 0.5
        ).move_to(2*m.LEFT)
        tex80 = m.MathTex("80\\%").move_to(1*m.UP + 2*m.LEFT)

        rect20 = m.Rectangle(
            width = 3.0,
            height = 1.0,
            color = m.YELLOW,
            fill_opacity = 0.5
        ).move_to(3.5*m.RIGHT)
        tex20 = m.MathTex("20\\%").move_to(1*m.UP + 3.5*m.RIGHT)

        valX.shift(0.5*m.DOWN)
        valy.shift(0.5*m.DOWN)
        bX.shift(0.5*m.DOWN)
        by.shift(0.5*m.DOWN)

        valX80 = m.VGroup(valX1, valX2, valX3[:6], valX4[:3],
                          X, eqX, bX0, bX1, bX2, bX3, bX4, bX5, bX6, bX7, bX8, bX9, bX10)
        
        valy80 = m.VGroup(valy[:5], y, eqy, by0, by1, by2, by3, by4, by5, by6, by7, by8, by9, by10)

        dy = bX11.get_y() - bX15.get_y()
        newvalX5 = valX5.copy().shift((1.5 + dy)*m.UP)
        newbX15 = bX15.copy().move_to(bX11.get_center() + 1.5*m.UP)
        newbX16 = bX16.copy().move_to(bX12.get_center() + 1.5*m.UP)
        newbX17 = bX17.copy().move_to(newbX16.get_center() + 0.2*m.RIGHT)
        newrowX = m.VGroup(newvalX5, newbX15, newbX16, newbX17)
        newvaly7 = valy[7].copy().shift((1.5 + dy)*m.UP)
        newby15 = by15.copy().move_to(by11.get_center() + 1.5*m.UP)
        newby16 = by16.copy().move_to(by12.get_center() + 1.5*m.UP)
        newby17 = by17.copy().move_to(newby16.get_center() + 0.2*m.RIGHT)
        newrowy = m.VGroup(newvaly7, newby15, newby16, newby17)

        newX = X.copy().move_to(valX3[6].get_center() + 1.5*m.LEFT)
        neweqX = eqX.copy().move_to(newX.get_center() + 0.5*m.RIGHT)
        newbX0 = bX0.copy().move_to(bX11.get_center() + 0.2*m.LEFT)
        newstartX = m.VGroup(newX, neweqX, newbX0)
        newy = y.copy().move_to(valy[5].get_center() + 1.5*m.LEFT)
        neweqy = eqy.copy().move_to(newy.get_center() + 0.5*m.RIGHT)
        newby0 = by0.copy().move_to(by11.get_center() + 0.2*m.LEFT)
        newstarty = m.VGroup(newy, neweqy, newby0)

        r8v = m.MathTex("\\vdots").move_to(bX16.get_center() + 1*m.RIGHT)
        r9v = m.MathTex("\\vdots").move_to(newbX16.get_center() + 1*m.RIGHT)

        rect80X = m.Rectangle(
            width = 6.0,
            height = 4.0,
            color = m.BLUE,
            fill_opacity = 0.5
        ).move_to(1.3*m.UP + 2*m.LEFT)

        rect20X = m.Rectangle(
            width = 6.0,
            height = 2.25,
            color = m.YELLOW,
            fill_opacity = 0.5
        ).move_to(2.25*m.DOWN + 2*m.LEFT)

        X11 = m.DecimalNumber(77).move_to(valX1[0].get_center() + 1.5*m.UP)
        X12 = m.DecimalNumber(10403).move_to(valX1[1].get_center() + 1.5*m.UP)
        X13 = m.DecimalNumber(0.6174, num_decimal_places = 4).move_to(valX1[2].get_center() + 1.5*m.UP)
        X21 = m.DecimalNumber(43).move_to(valX1[4].get_center() + 1.5*m.UP)
        X22 = m.DecimalNumber(2697).move_to(valX1[5].get_center() + 1.5*m.UP)
        X23 = m.DecimalNumber(0.9857, num_decimal_places = 4).move_to(valX1[6].get_center() + 1.5*m.UP)
        X31 = m.DecimalNumber(35).move_to(valX2[0].get_center() + 1.5*m.UP)
        X32 = m.DecimalNumber(8040).move_to(valX2[1].get_center() + 1.5*m.UP)
        X33 = m.DecimalNumber(0.6930, num_decimal_places = 4).move_to(valX2[2].get_center() + 1.5*m.UP)
        X41 = m.DecimalNumber(32).move_to(valX3[0].get_center() + 1.5*m.UP)
        X42 = m.DecimalNumber(10935).move_to(valX3[1].get_center() + 1.5*m.UP)
        X43 = m.DecimalNumber(0.6890, num_decimal_places = 4).move_to(valX3[2].get_center() + 1.5*m.UP)
        X51 = m.DecimalNumber(94).move_to(valX3[3].get_center() + 1.5*m.UP)
        X52 = m.DecimalNumber(11696).move_to(valX3[4].get_center() + 1.5*m.UP)
        X53 = m.DecimalNumber(0.8249, num_decimal_places = 4).move_to(valX3[5].get_center() + 1.5*m.UP)
        X61 = m.DecimalNumber(75).move_to(valX3[6].get_center())
        X62 = m.DecimalNumber(2565).move_to(valX3[7].get_center())
        X63 = m.DecimalNumber(0.4842, num_decimal_places = 4).move_to(valX3[8].get_center())
        X71 = m.DecimalNumber(73).move_to(valX3[9].get_center())
        X72 = m.DecimalNumber(15566).move_to(valX3[10].get_center())
        X73 = m.DecimalNumber(0.2671, num_decimal_places = 4).move_to(valX3[11].get_center())

        rect80y = m.Rectangle(
            width = 1.5,
            height = 4.0,
            color = m.BLUE,
            fill_opacity = 0.5
        ).move_to(1.3*m.UP + 5.45*m.RIGHT)

        rect20y = m.Rectangle(
            width = 1.5,
            height = 2.25,
            color = m.YELLOW,
            fill_opacity = 0.5
        ).move_to(2.25*m.DOWN + 5.45*m.RIGHT)

        y1 = m.DecimalNumber(0).move_to(valy[0].get_center() + 1.5*m.UP)
        y2 = m.DecimalNumber(1).move_to(valy[1].get_center() + 1.5*m.UP)
        y3 = m.DecimalNumber(1).move_to(valy[2].get_center() + 1.5*m.UP)
        y4 = m.DecimalNumber(0).move_to(valy[3].get_center() + 1.5*m.UP)
        y5 = m.DecimalNumber(0).move_to(valy[4].get_center() + 1.5*m.UP)
        y6 = m.DecimalNumber(1).move_to(valy[5].get_center())
        y7 = m.DecimalNumber(0).move_to(valy[6].get_center())

        bigrect80 = m.Rectangle(
            width = 13.0,
            height = 4.0,
            color = m.BLUE
        ).move_to(1.3*m.UP)

        bigrect20 = m.Rectangle(
            width = 13.0,
            height = 2.25,
            color = m.YELLOW
        ).move_to(2.25*m.DOWN)

        traintex = m.Tex("training", color = m.BLUE).move_to(newbX17.get_center() + 0.2*m.DOWN + 2*m.RIGHT)
        valtex = m.Tex("validation", color = m.YELLOW).move_to(bX17.get_center() + 0.2*m.DOWN + 2*m.RIGHT)

        Xtrain = m.MathTex("X_{train}").move_to(X.get_center() + 1.5*m.UP + 0.3*m.LEFT)
        Xval = m.MathTex("X_{val}").move_to(newX.get_center() + 0.2*m.LEFT)
        ytrain = m.MathTex("y_{train}").move_to(y.get_center() + 1.5*m.UP + 0.25*m.LEFT)
        yval = m.MathTex("y_{val}").move_to(newy.get_center() + 0.15*m.LEFT)
        
        self.play(
            m.FadeIn(it, iv, rect80, tex80, rect20, tex20)
        )
        self.wait()
        self.play(
            it.animate.shift(2.5*m.UP),
            iv.animate.shift(2.5*m.UP),
            rect80.animate.shift(2.5*m.UP),
            tex80.animate.shift(2.5*m.UP),
            rect20.animate.shift(2.5*m.UP),
            tex20.animate.shift(2.5*m.UP),
            m.FadeIn(valX, valy, bX, by)
        )
        self.wait()
        self.play(
            valX80.animate.shift(1.5*m.UP),
            valy80.animate.shift(1.5*m.UP),
            r1.animate.move_to(bX2.get_center() + 1.5*m.UP + 1*m.RIGHT),
            r2.animate.move_to(bX4.get_center() + 1.5*m.UP + 1*m.RIGHT),
            r3.animate.move_to(bX6.get_center() + 1.5*m.UP + 1*m.RIGHT),
            r4.animate.move_to(bX8.get_center() + 1.5*m.UP + 1*m.RIGHT),
            r5.animate.move_to(bX10.get_center() + 1.5*m.UP + 1*m.RIGHT),
            r6.animate.move_to(bX12.get_center() + 1*m.RIGHT),
            r7.animate.move_to(bX14.get_center() + 1*m.RIGHT),
            m.Transform(r8, r8v),
            m.Transform(r9, r9v),
            m.Create(newrowX),
            m.Create(newrowy),
            m.Create(newstartX),
            m.Create(newstarty),
            m.FadeOut(tex80, tex20),
            m.Transform(rect80, rect80X),
            m.Transform(rect20, rect20X)
        )
        self.wait()
        self.play(
            m.Transform(valX1[0], X11),
            m.Transform(valX1[1], X12),
            m.Transform(valX1[2], X13),
            m.Transform(valX1[4], X21),
            m.Transform(valX1[5], X22),
            m.Transform(valX1[6], X23),
            m.Transform(valX2[0], X31),
            m.Transform(valX2[1], X32),
            m.Transform(valX2[2], X33),
            m.Transform(valX3[0], X41),
            m.Transform(valX3[1], X42),
            m.Transform(valX3[2], X43),
            m.Transform(valX3[3], X51),
            m.Transform(valX3[4], X52),
            m.Transform(valX3[5], X53),
            m.Transform(valX3[6], X61),
            m.Transform(valX3[7], X62),
            m.Transform(valX3[8], X63),
            m.Transform(valX3[9], X71),
            m.Transform(valX3[10], X72),
            m.Transform(valX3[11], X73)
        )
        self.play(
            m.Transform(rect80, rect80y),
            m.Transform(rect20, rect20y)
        )
        self.play(
            m.Transform(valy[0], y1),
            m.Transform(valy[1], y2),
            m.Transform(valy[2], y3),
            m.Transform(valy[3], y4),
            m.Transform(valy[4], y5),
            m.Transform(valy[5], y6),
            m.Transform(valy[6], y7)
        )
        self.play(
            m.FadeOut(it, iv),
            m.Transform(rect80, bigrect80),
            m.Transform(rect20, bigrect20),
            m.Write(traintex),
            m.Write(valtex)
        )
        self.wait()
        self.play(
            m.FadeOut(rect80, rect20, traintex, valtex),
            m.Transform(X, Xtrain),
            m.Transform(newX, Xval),
            m.Transform(y, ytrain),
            m.Transform(newy, yval)
        )
        self.wait()
# ---------------------------------------------------------------------------
class Cell12(m.Scene):
    def construct(self):

        tabU = m.Table(
            [["45", "9120", "0.3241", "\\dots"],
            ["52", "2600", "0.8544", "\\dots"]],
            top_left_entry = m.Tex("TRAINING"),
            col_labels = [m.Tex("Age"),
                          m.Tex("Monthly Income"),
                          m.Tex("Debt Ratio"),
                          m.MathTex("\\dots")],
            row_labels = [m.DecimalNumber(1),
                          m.DecimalNumber(2)]
        ).move_to(1.82*m.UP)

        vdots1 = m.MathTex("\\vdots").move_to(0.58*m.UP + 4.02*m.LEFT)
        vdots2 = m.MathTex("\\vdots").move_to(0.58*m.UP + 2.11*m.LEFT)
        vdots3 = m.MathTex("\\vdots").move_to(0.58*m.UP + 0.2*m.RIGHT)
        vdots4 = m.MathTex("\\vdots").move_to(0.58*m.UP + 3.16*m.RIGHT)
        ddots = m.MathTex("\\ddots").move_to(0.58*m.UP + 4.87*m.RIGHT)
        vdots = m.VGroup(vdots1, vdots2, vdots3, vdots4, ddots)

        mid = m.Table(
            [["77", "4062", "0.3674"],
            ["32", "13985", "0.8612"],
            ["24", "6210", "0.5143"],
            ["63", "3375", "0.9412"]],
            top_left_entry = m.Tex("TRAINING", fill_opacity = 0.0),
            col_labels = [m.Tex("Age", fill_opacity = 0.0),
                          m.Tex("Monthly Income", fill_opacity = 0.0),
                          m.Tex("Debt Ratio", fill_opacity = 0.0)],
            row_labels = [m.DecimalNumber(4),
                          m.DecimalNumber(5),
                          m.DecimalNumber(6),
                          m.DecimalNumber(7)]
        ).move_to(0.525*m.DOWN + 0.455*m.LEFT)

        d1 = m.MathTex("\\dots").move_to(0.59*m.UP + 4.87*m.RIGHT)
        d2 = d1.copy().shift(0.585*m.DOWN)
        d3 = d2.copy().shift(0.585*m.DOWN)
        d4 = d3.copy().shift(0.585*m.DOWN)
        d5 = d4.copy().shift(0.585*m.DOWN)
        d = m.VGroup(d1, d2, d3, d4, d5)

        t1 = m.DecimalNumber(3).move_to(0.59*m.UP + 4.02*m.LEFT)
        t2 = m.DecimalNumber(85).move_to(0.59*m.UP + 2.11*m.LEFT)
        t3 = m.DecimalNumber(18540).move_to(0.59*m.UP + 0.2*m.RIGHT)
        t4 = m.DecimalNumber(0.0812, num_decimal_places = 4).move_to(0.59*m.UP + 3.16*m.RIGHT)
        t = m.VGroup(t1, t2, t3, t4)

        deltab = m.Table(
            [[],
            [],
            [],
            [],
            [],
            [],
            [],
            []],
            top_left_entry = m.Tex("Delinquency"),
            col_labels = [],
            row_labels = [m.DecimalNumber(0),
                          m.DecimalNumber(1),
                          m.DecimalNumber(0),
                          m.DecimalNumber(1),
                          m.DecimalNumber(1),
                          m.DecimalNumber(0),
                          m.DecimalNumber(1),
                          m.MathTex("\\vdots")],
            v_buff = 0.305
        ).move_to(0.02*m.UP + 5.24*m.RIGHT)

        valX1 = tabU.get_entries_without_labels().copy()
        valX2 = t.copy()
        valX2.remove(valX2[0])
        valX3 = mid.get_entries_without_labels().copy()
        valX4 = d.copy()
        valX5 = vdots.copy()
        valX5.remove(valX5[0]).shift(2.95*m.DOWN)
        valX = m.VGroup(valX1, valX2, valX3, valX4, valX5).shift(1.65*m.LEFT)
        valy = deltab.get_row_labels().copy().shift(0.2*m.RIGHT)

        col1 = m.VGroup(valX1[0::4], valX2[0], valX3[0::3], valX5[0])
        col2 = m.VGroup(valX1[1::4], valX2[1], valX3[1::3], valX5[1])
        col3 = m.VGroup(valX1[2::4], valX2[2], valX3[2::3], valX5[2])
        col4 = m.VGroup(valX1[3::4], valX4, valX5[3])

        X = m.MathTex("X").move_to(valX1[0].get_center() + 2*m.LEFT)
        eqX = m.MathTex("=").move_to(X.get_center() + 0.5*m.RIGHT)
        bX1 = m.MathTex("[").move_to(col1[0][0].get_center() + 0.9*m.LEFT)
        bX0 = bX1.copy().shift(0.2*m.LEFT)
        bX2 = m.MathTex("]").move_to(col4[0][0].get_center() + 2.6*m.LEFT)
        bX3 = bX1.copy().move_to(col1[0][1].get_center() + 0.9*m.LEFT)
        bX4 = bX2.copy().move_to(col4[0][1].get_center() + 2.6*m.LEFT)
        bX5 = bX1.copy().move_to(col1[1].get_center() + 0.9*m.LEFT)
        bX6 = bX2.copy().move_to(col4[1][0].get_center() + 2.6*m.LEFT)
        bX7 = bX1.copy().move_to(col1[2][0].get_center() + 0.9*m.LEFT)
        bX8 = bX2.copy().move_to(col4[1][1].get_center() + 2.6*m.LEFT)
        bX9 = bX1.copy().move_to(col1[2][1].get_center() + 0.9*m.LEFT)
        bX10 = bX2.copy().move_to(col4[1][2].get_center() + 2.6*m.LEFT)
        bX11 = bX1.copy().move_to(col1[2][2].get_center() + 0.9*m.LEFT)
        bX12 = bX2.copy().move_to(col4[1][3].get_center() + 2.6*m.LEFT)
        bX13 = bX1.copy().move_to(col1[2][3].get_center() + 0.9*m.LEFT)
        bX14 = bX2.copy().move_to(col4[1][4].get_center() + 2.6*m.LEFT)
        bX15 = bX1.copy().move_to(col1[3].get_center() + 0.9*m.LEFT)
        bX16 = bX2.copy().move_to(col4[2].get_center() + 2.6*m.LEFT)
        bX17 = bX16.copy().shift(0.2*m.RIGHT)

        y = m.MathTex("y").move_to(valy[0].get_center() + 1.5*m.LEFT)
        eqy = m.MathTex("=").move_to(y.get_center() + 0.5*m.RIGHT)
        by1 = m.MathTex("[").move_to(valy[0].get_center() + 0.4*m.LEFT)
        by0 = by1.copy().shift(0.2*m.LEFT)
        by2 = m.MathTex("]").move_to(valy[0].get_center() + 0.4*m.RIGHT)
        by3 = by1.copy().move_to(valy[1].get_center() + 0.4*m.LEFT)
        by4 = by2.copy().move_to(valy[1].get_center() + 0.4*m.RIGHT)
        by5 = by1.copy().move_to(valy[2].get_center() + 0.4*m.LEFT)
        by6 = by2.copy().move_to(valy[2].get_center() + 0.4*m.RIGHT)
        by7 = by1.copy().move_to(valy[3].get_center() + 0.4*m.LEFT)
        by8 = by2.copy().move_to(valy[3].get_center() + 0.4*m.RIGHT)
        by9 = by1.copy().move_to(valy[4].get_center() + 0.4*m.LEFT)
        by10 = by2.copy().move_to(valy[4].get_center() + 0.4*m.RIGHT)
        by11 = by1.copy().move_to(valy[5].get_center() + 0.4*m.LEFT)
        by12 = by2.copy().move_to(valy[5].get_center() + 0.4*m.RIGHT)
        by13 = by1.copy().move_to(valy[6].get_center() + 0.4*m.LEFT)
        by14 = by2.copy().move_to(valy[6].get_center() + 0.4*m.RIGHT)
        by15 = by1.copy().move_to(valy[7].get_center() + 0.4*m.LEFT)
        by16 = by2.copy().move_to(valy[7].get_center() + 0.4*m.RIGHT)
        by17 = by16.copy().shift(0.2*m.RIGHT)

        col1.shift(0.5*m.LEFT)
        col2.shift(1.5*m.LEFT)
        col3.shift(2.7*m.LEFT)
        col4.shift(3*m.LEFT)

        dy = bX11.get_y() - bX15.get_y()
        newvalX5 = valX5.copy().shift((1.5 + dy)*m.UP)
        newbX15 = bX15.copy().move_to(bX11.get_center() + 1.5*m.UP)
        newbX16 = bX16.copy().move_to(bX12.get_center() + 1.5*m.UP)
        newbX17 = bX17.copy().move_to(newbX16.get_center() + 0.2*m.RIGHT)
        newvaly7 = valy[7].copy().shift((1.5 + dy)*m.UP)
        newby15 = by15.copy().move_to(by11.get_center() + 1.5*m.UP)
        newby16 = by16.copy().move_to(by12.get_center() + 1.5*m.UP)
        newby17 = by17.copy().move_to(newby16.get_center() + 0.2*m.RIGHT)

        newX = X.copy().move_to(valX3[6].get_center() + 1.5*m.LEFT)
        neweqX = eqX.copy().move_to(newX.get_center() + 0.5*m.RIGHT)
        newbX0 = bX0.copy().move_to(bX11.get_center() + 0.2*m.LEFT)
        newy = y.copy().move_to(valy[5].get_center() + 1.5*m.LEFT)
        neweqy = eqy.copy().move_to(newy.get_center() + 0.5*m.RIGHT)
        newby0 = by0.copy().move_to(by11.get_center() + 0.2*m.LEFT)

        X11 = m.DecimalNumber(77).move_to(valX1[0].get_center() + 1.5*m.UP)
        X12 = m.DecimalNumber(10403).move_to(valX1[1].get_center() + 1.5*m.UP)
        X13 = m.DecimalNumber(0.6174, num_decimal_places = 4).move_to(valX1[2].get_center() + 1.5*m.UP)
        X21 = m.DecimalNumber(43).move_to(valX1[4].get_center() + 1.5*m.UP)
        X22 = m.DecimalNumber(2697).move_to(valX1[5].get_center() + 1.5*m.UP)
        X23 = m.DecimalNumber(0.9857, num_decimal_places = 4).move_to(valX1[6].get_center() + 1.5*m.UP)
        X31 = m.DecimalNumber(35).move_to(valX2[0].get_center() + 1.5*m.UP)
        X32 = m.DecimalNumber(8040).move_to(valX2[1].get_center() + 1.5*m.UP)
        X33 = m.DecimalNumber(0.6930, num_decimal_places = 4).move_to(valX2[2].get_center() + 1.5*m.UP)
        X41 = m.DecimalNumber(32).move_to(valX3[0].get_center() + 1.5*m.UP)
        X42 = m.DecimalNumber(10935).move_to(valX3[1].get_center() + 1.5*m.UP)
        X43 = m.DecimalNumber(0.6890, num_decimal_places = 4).move_to(valX3[2].get_center() + 1.5*m.UP)
        X51 = m.DecimalNumber(94).move_to(valX3[3].get_center() + 1.5*m.UP)
        X52 = m.DecimalNumber(11696).move_to(valX3[4].get_center() + 1.5*m.UP)
        X53 = m.DecimalNumber(0.8249, num_decimal_places = 4).move_to(valX3[5].get_center() + 1.5*m.UP)
        X61 = m.DecimalNumber(75).move_to(valX3[6].get_center())
        X62 = m.DecimalNumber(2565).move_to(valX3[7].get_center())
        X63 = m.DecimalNumber(0.4842, num_decimal_places = 4).move_to(valX3[8].get_center())
        X71 = m.DecimalNumber(73).move_to(valX3[9].get_center())
        X72 = m.DecimalNumber(15566).move_to(valX3[10].get_center())
        X73 = m.DecimalNumber(0.2671, num_decimal_places = 4).move_to(valX3[11].get_center())

        y1 = m.DecimalNumber(0).move_to(valy[0].get_center() + 1.5*m.UP)
        y2 = m.DecimalNumber(1).move_to(valy[1].get_center() + 1.5*m.UP)
        y3 = m.DecimalNumber(1).move_to(valy[2].get_center() + 1.5*m.UP)
        y4 = m.DecimalNumber(0).move_to(valy[3].get_center() + 1.5*m.UP)
        y5 = m.DecimalNumber(0).move_to(valy[4].get_center() + 1.5*m.UP)
        y6 = m.DecimalNumber(1).move_to(valy[5].get_center())
        y7 = m.DecimalNumber(0).move_to(valy[6].get_center())
        
        Xtrainval = m.VGroup(X11, X12, X13,
                             X21, X22, X23,
                             X31, X32, X33,
                             X41, X42, X43,
                             X51, X52, X53).shift(0.5*m.DOWN)
        Xvalval = m.VGroup(X61, X62, X63,
                           X71, X72, X73).shift(0.5*m.DOWN)
        ytrainval = m.VGroup(y1, y2, y3, y4, y5).shift(0.5*m.DOWN)
        yvalval = m.VGroup(y6, y7).shift(0.5*m.DOWN)

        Xtraindots = m.VGroup(valX1[3::4].shift(1.5*m.UP), valX4[:3].shift(1.5*m.UP), newvalX5).shift(0.5*m.DOWN)
        Xvaldots = m.VGroup(valX4[3:], valX5).shift(0.5*m.DOWN)
        ytraindots = newvaly7.shift(0.5*m.DOWN)
        yvaldots = valy[7].shift(0.5*m.DOWN)

        Xtrain = m.MathTex("X_{train}").move_to(X.get_center() + 0.3*m.LEFT)
        Xval = m.MathTex("X_{val}").move_to(newX.get_center() + 0.2*m.LEFT)
        ytrain = m.MathTex("y_{train}").move_to(y.get_center() + 0.25*m.LEFT)
        yval = m.MathTex("y_{val}").move_to(newy.get_center() + 0.15*m.LEFT)

        Xtrainrest = m.VGroup(Xtrain, eqX, bX0, bX1, bX2, bX3, bX4, bX5, bX6, bX7, bX8, bX9, bX10,
                              newbX15.shift(1.5*m.DOWN), newbX16.shift(1.5*m.DOWN),
                              newbX17.shift(1.5*m.DOWN)).shift(1*m.UP)
        Xvalrest = m.VGroup(Xval, neweqX, newbX0, bX11, bX12, bX13, bX14, bX15, bX16, bX17).shift(0.5*m.DOWN)
        ytrainrest = m.VGroup(ytrain, eqy, by0, by1, by2, by3, by4, by5, by6, by7, by8, by9, by10,
                              newby15.shift(1.5*m.DOWN), newby16.shift(1.5*m.DOWN),
                              newby17.shift(1.5*m.DOWN)).shift(1*m.UP)
        yvalrest = m.VGroup(yval, neweqy, newby0, by11, by12, by13, by14, by15, by16, by17).shift(0.5*m.DOWN)

        eqmu = eqX.copy().shift(0.5*m.DOWN + 2*m.RIGHT)
        mu = m.MathTex("\\mu").move_to(eqmu.get_center() + 0.5*m.LEFT)
        bmu1 = bX0.copy().shift(0.5*m.DOWN + 2*m.RIGHT)
        bmu2 = bX2.copy().shift(0.5*m.DOWN + 2*m.RIGHT)

        rect = m.Rectangle(
            width = 1.3,
            height = 4.0,
            color = m.BLUE,
            fill_opacity = 0.5
        ).move_to(m.VGroup(X31, X41).get_center() + 1.5*m.DOWN + 2*m.RIGHT)

        mu1 = m.DecimalNumber(56.2, num_decimal_places = 1).move_to(X11.get_center() + 0.5*m.DOWN + 2*m.RIGHT)
        mu2 = m.DecimalNumber(8754.2, num_decimal_places = 1).move_to(X12.get_center() + 0.5*m.DOWN + 2*m.RIGHT)
        mu3 = m.DecimalNumber(0.7620, num_decimal_places = 4).move_to(X13.get_center() + 0.5*m.DOWN + 2*m.RIGHT)
        mu4 = valX1[3].copy().shift(0.5*m.DOWN + 2*m.RIGHT)

        muline = m.VGroup(mu, eqmu, bmu1, mu1, mu2, mu3, mu4, bmu2)

        eqs = eqX.copy().shift(0.5*m.DOWN + 2*m.RIGHT)
        s = m.MathTex("\\sigma").move_to(eqs.get_center() + 0.5*m.LEFT)
        bs1 = bX0.copy().shift(0.5*m.DOWN + 2*m.RIGHT)
        bs2 = bX2.copy().shift(0.5*m.DOWN + 2*m.RIGHT)

        s1 = m.DecimalNumber(24.8, num_decimal_places = 1).move_to(X11.get_center() + 0.5*m.DOWN + 2*m.RIGHT)
        s2 = m.DecimalNumber(3265.8, num_decimal_places = 1).move_to(X12.get_center() + 0.5*m.DOWN + 2*m.RIGHT)
        s3 = m.DecimalNumber(0.1304, num_decimal_places = 4).move_to(X13.get_center() + 0.5*m.DOWN + 2*m.RIGHT)
        s4 = valX1[3].copy().shift(0.5*m.DOWN + 2*m.RIGHT)

        sline = m.VGroup(s, eqs, bs1, s1, s2, s3, s4, bs2)

        dx = (X13.get_x() - X12.get_x()) - (X12.get_x() - X11.get_x())

        self.play(
            m.FadeIn(Xtrainval, Xvalval, ytrainval, yvalval),
            m.FadeIn(Xtraindots, Xvaldots, ytraindots, yvaldots),
            m.FadeIn(Xtrainrest, Xvalrest, ytrainrest, yvalrest)
        )
        self.wait()
        self.play(
            m.FadeOut(ytrainval, ytraindots, ytrainrest, yvalval, yvaldots, yvalrest),
            Xtrainval.animate.shift(2*m.RIGHT),
            Xtraindots.animate.shift(2*m.RIGHT),
            Xtrainrest.animate.shift(2*m.RIGHT),
            Xvalval.animate.shift(2*m.RIGHT),
            Xvaldots.animate.shift(2*m.RIGHT),
            Xvalrest.animate.shift(2*m.RIGHT)
        )
        self.wait()
        self.play(
            m.FadeOut(Xvalval, Xvaldots, Xvalrest),
            Xtrainval.animate.shift(1.5*m.DOWN),
            Xtraindots.animate.shift(1.5*m.DOWN),
            Xtrainrest.animate.shift(1.5*m.DOWN)
        )
        self.wait()
        self.play(
            m.Write(mu),
            m.Write(eqmu),
            m.Write(bmu1),
            m.Write(bmu2)
        )
        self.play(
            m.FadeIn(rect)
        )
        self.play(
            m.Write(mu1)
        )
        self.play(
            rect.animate.move_to(m.VGroup(X32, X42).get_center())
        )
        self.play(
            m.Write(mu2)
        )
        self.play(
            rect.animate.move_to(m.VGroup(X33, X43).get_center())
        )
        self.play(
            m.Write(mu3)
        )
        self.play(
            rect.animate.move_to(m.VGroup(valX4[0:2]).get_center())
        )
        self.play(
            m.Write(mu4)
        )
        self.play(
            rect.animate.move_to(m.VGroup(X31, X41).get_center()),
            muline.animate.shift(1*m.UP),
            m.Write(s),
            m.Write(eqs),
            m.Write(bs1),
            m.Write(bs2)
        )
        self.play(
            m.Write(s1)
        )
        self.play(
            rect.animate.move_to(m.VGroup(X32, X42).get_center())
        )
        self.play(
            m.Write(s2)
        )
        self.play(
            rect.animate.move_to(m.VGroup(X33, X43).get_center())
        )
        self.play(
            m.Write(s3)
        )
        self.play(
            rect.animate.move_to(m.VGroup(valX4[0:2]).get_center())
        )
        self.play(
            m.Write(s4)
        )
        self.play(
            m.FadeOut(rect)
        )
        self.wait()
        self.play(
            m.Transform(X11, m.DecimalNumber(0.8393, num_decimal_places = 4).move_to(X11.get_center() + dx*m.LEFT)),
            m.Transform(X12, m.DecimalNumber(0.5049, num_decimal_places = 4).move_to(X12.get_center())),
            m.Transform(X13, m.DecimalNumber(-1.1090, num_decimal_places = 4).move_to(X13.get_center())),
            m.Transform(X21, m.DecimalNumber(-0.5326, num_decimal_places = 4).move_to(X21.get_center() + dx*m.LEFT)),
            m.Transform(X22, m.DecimalNumber(-1.8547, num_decimal_places = 4).move_to(X22.get_center())),
            m.Transform(X23, m.DecimalNumber(1.7157, num_decimal_places = 4).move_to(X23.get_center())),
            m.Transform(X31, m.DecimalNumber(-0.8555, num_decimal_places = 4).move_to(X31.get_center() + dx*m.LEFT)),
            m.Transform(X32, m.DecimalNumber(-0.2187, num_decimal_places = 4).move_to(X32.get_center())),
            m.Transform(X33, m.DecimalNumber(-0.5292, num_decimal_places = 4).move_to(X33.get_center())),
            m.Transform(X41, m.DecimalNumber(-0.9765, num_decimal_places = 4).move_to(X41.get_center() + dx*m.LEFT)),
            m.Transform(X42, m.DecimalNumber(0.6678, num_decimal_places = 4).move_to(X42.get_center())),
            m.Transform(X43, m.DecimalNumber(-0.5599, num_decimal_places = 4).move_to(X43.get_center())),
            m.Transform(X51, m.DecimalNumber(1.5253, num_decimal_places = 4).move_to(X51.get_center() + dx*m.LEFT)),
            m.Transform(X52, m.DecimalNumber(0.9008, num_decimal_places = 4).move_to(X52.get_center())),
            m.Transform(X53, m.DecimalNumber(0.4824, num_decimal_places = 4).move_to(X53.get_center())),
            newvalX5[0].animate.shift(dx*m.LEFT),
            mu.animate.shift(2*dx*m.LEFT),
            eqmu.animate.shift(2*dx*m.LEFT),
            bmu1.animate.shift(2*dx*m.LEFT),
            mu1.animate.shift(dx*m.LEFT),
            s.animate.shift(2*dx*m.LEFT),
            eqs.animate.shift(2*dx*m.LEFT),
            bs1.animate.shift(2*dx*m.LEFT),
            s1.animate.shift(dx*m.LEFT),
            Xtrain.animate.shift(2*dx*m.LEFT),
            eqX.animate.shift(2*dx*m.LEFT),
            bX0.animate.shift(2*dx*m.LEFT),
            bX1.animate.shift(2*dx*m.LEFT),
            bX3.animate.shift(2*dx*m.LEFT),
            bX5.animate.shift(2*dx*m.LEFT),
            bX7.animate.shift(2*dx*m.LEFT),
            bX9.animate.shift(2*dx*m.LEFT),
            newbX15.animate.shift(2*dx*m.LEFT)
        )
        self.wait()
        self.play(
            m.FadeOut(Xtrainval, Xtraindots, Xtrainrest),
            m.FadeIn(Xvalval, Xvaldots, Xvalrest),
            Xvalval.animate.shift(3*m.UP),
            Xvaldots.animate.shift(3*m.UP),
            Xvalrest.animate.shift(3*m.UP),
            Xval.animate.shift(3*m.UP + 2*dx*m.LEFT),
            neweqX.animate.shift(3*m.UP + 2*dx*m.LEFT),
            newbX0.animate.shift(3*m.UP + 2*dx*m.LEFT),
            bX11.animate.shift(3*m.UP + 2*dx*m.LEFT),
            bX13.animate.shift(3*m.UP + 2*dx*m.LEFT),
            bX15.animate.shift(3*m.UP + 2*dx*m.LEFT),
            X61.animate.shift(3*m.UP + dx*m.LEFT),
            X71.animate.shift(3*m.UP + dx*m.LEFT),
            valX5[0].animate.shift(3*m.UP + dx*m.LEFT)
        )
        self.wait()
        self.play(
            m.Transform(X61, m.DecimalNumber(0.7586, num_decimal_places = 4).move_to(X61.get_center())),
            m.Transform(X62, m.DecimalNumber(-1.8951, num_decimal_places = 4).move_to(X62.get_center())),
            m.Transform(X63, m.DecimalNumber(-2.1307, num_decimal_places = 4).move_to(X63.get_center())),
            m.Transform(X71, m.DecimalNumber(0.6779, num_decimal_places = 4).move_to(X71.get_center())),
            m.Transform(X72, m.DecimalNumber(2.0858, num_decimal_places = 4).move_to(X72.get_center())),
            m.Transform(X73, m.DecimalNumber(-3.7958, num_decimal_places = 4).move_to(X73.get_center()))
        )
        self.wait()
        self.play(
            m.FadeOut(muline, sline),
            m.FadeIn(Xtrainval, Xtraindots, Xtrainrest),
            Xtrainval.animate.shift(1.5*m.UP),
            Xtraindots.animate.shift(1.5*m.UP),
            Xtrainrest.animate.shift(1.5*m.UP),
            Xvalval.animate.shift(3*m.DOWN),
            Xvaldots.animate.shift(3*m.DOWN),
            Xvalrest.animate.shift(3*m.DOWN)
        )
        self.wait()
# ---------------------------------------------------------------------------
class Cell13(m.Scene):
    def construct(self):

        deltab = m.Table(
            [[],
            [],
            [],
            [],
            [],
            [],
            [],
            []],
            top_left_entry = m.Tex("Delinquency"),
            col_labels = [],
            row_labels = [m.DecimalNumber(0),
                          m.DecimalNumber(1),
                          m.DecimalNumber(0),
                          m.DecimalNumber(1),
                          m.DecimalNumber(1),
                          m.DecimalNumber(0),
                          m.DecimalNumber(1),
                          m.MathTex("\\vdots")],
            v_buff = 0.305
        ).move_to(0.02*m.UP + 5.24*m.RIGHT)

        valy = deltab.get_row_labels().copy().shift(0.2*m.RIGHT)

        y = m.MathTex("y").move_to(valy[0].get_center() + 1.5*m.LEFT)
        eqy = m.MathTex("=").move_to(y.get_center() + 0.5*m.RIGHT)
        by1 = m.MathTex("[").move_to(valy[0].get_center() + 0.4*m.LEFT)
        by0 = by1.copy().shift(0.2*m.LEFT)
        by2 = m.MathTex("]").move_to(valy[0].get_center() + 0.4*m.RIGHT)
        by3 = by1.copy().move_to(valy[1].get_center() + 0.4*m.LEFT)
        by4 = by2.copy().move_to(valy[1].get_center() + 0.4*m.RIGHT)
        by5 = by1.copy().move_to(valy[2].get_center() + 0.4*m.LEFT)
        by6 = by2.copy().move_to(valy[2].get_center() + 0.4*m.RIGHT)
        by7 = by1.copy().move_to(valy[3].get_center() + 0.4*m.LEFT)
        by8 = by2.copy().move_to(valy[3].get_center() + 0.4*m.RIGHT)
        by9 = by1.copy().move_to(valy[4].get_center() + 0.4*m.LEFT)
        by10 = by2.copy().move_to(valy[4].get_center() + 0.4*m.RIGHT)
        by11 = by1.copy().move_to(valy[5].get_center() + 0.4*m.LEFT)
        by12 = by2.copy().move_to(valy[5].get_center() + 0.4*m.RIGHT)
        by13 = by1.copy().move_to(valy[6].get_center() + 0.4*m.LEFT)
        by14 = by2.copy().move_to(valy[6].get_center() + 0.4*m.RIGHT)
        by15 = by1.copy().move_to(valy[7].get_center() + 0.4*m.LEFT)
        by16 = by2.copy().move_to(valy[7].get_center() + 0.4*m.RIGHT)
        by17 = by16.copy().shift(0.2*m.RIGHT)
        by = m.VGroup(y, eqy, by0, by1, by2, by3, by4, by5, by6, by7, by8,
                      by9, by10, by11, by12, by13, by14, by15, by16, by17)
        
        yall = m.VGroup(valy, by).move_to(m.ORIGIN)

        classtex = m.Tex("class").move_to(1*m.UP + 4*m.LEFT)
        counttex = m.Tex("count").move_to(1*m.UP + 2*m.LEFT)

        class0 = m.DecimalNumber(0).move_to(4*m.LEFT)
        class1 = m.DecimalNumber(1).move_to(1*m.DOWN + 4*m.LEFT)

        count0 = m.DecimalNumber(0).move_to(2*m.LEFT)
        count1 = m.DecimalNumber(0).move_to(1*m.DOWN + 2*m.LEFT)

        y1 = valy[0].copy().shift(3*m.RIGHT)
        y2 = valy[1].copy().shift(3*m.RIGHT)
        y3 = valy[2].copy().shift(3*m.RIGHT)
        y4 = valy[3].copy().shift(3*m.RIGHT)
        y5 = valy[4].copy().shift(3*m.RIGHT)
        y6 = valy[5].copy().shift(3*m.RIGHT)
        y7 = valy[6].copy().shift(3*m.RIGHT)

        weighttex = m.Tex("weight").move_to(1*m.UP)
        weight0 = m.DecimalNumber(1.167, num_decimal_places = 3)
        weight1 = m.DecimalNumber(0.875, num_decimal_places = 3).move_to(1*m.DOWN)

        w1 = weight0.copy().move_to(valy[0].get_center() + 2*m.LEFT)
        w2 = weight1.copy().move_to(valy[1].get_center() + 2*m.LEFT)
        w3 = weight0.copy().move_to(valy[2].get_center() + 2*m.LEFT)
        w4 = weight1.copy().move_to(valy[3].get_center() + 2*m.LEFT)
        w5 = weight1.copy().move_to(valy[4].get_center() + 2*m.LEFT)
        w6 = weight0.copy().move_to(valy[5].get_center() + 2*m.LEFT)
        w7 = weight1.copy().move_to(valy[6].get_center() + 2*m.LEFT)
        wdots = valy[7].copy().move_to(valy[7].get_center() + 2*m.LEFT)

        w = m.MathTex("w_{sample}").move_to(w1.get_center() + 2.3*m.LEFT)
        eqw = m.MathTex("=").move_to(w.get_center() + 1*m.RIGHT)
        bw1 = m.MathTex("[").move_to(w1.get_center() + 0.7*m.LEFT)
        bw0 = bw1.copy().shift(0.2*m.LEFT)
        bw2 = m.MathTex("]").move_to(w1.get_center() + 0.7*m.RIGHT)
        bw3 = bw1.copy().move_to(w2.get_center() + 0.7*m.LEFT)
        bw4 = bw2.copy().move_to(w2.get_center() + 0.7*m.RIGHT)
        bw5 = bw1.copy().move_to(w3.get_center() + 0.7*m.LEFT)
        bw6 = bw2.copy().move_to(w3.get_center() + 0.7*m.RIGHT)
        bw7 = bw1.copy().move_to(w4.get_center() + 0.7*m.LEFT)
        bw8 = bw2.copy().move_to(w4.get_center() + 0.7*m.RIGHT)
        bw9 = bw1.copy().move_to(w5.get_center() + 0.7*m.LEFT)
        bw10 = bw2.copy().move_to(w5.get_center() + 0.7*m.RIGHT)
        bw11 = bw1.copy().move_to(w6.get_center() + 0.7*m.LEFT)
        bw12 = bw2.copy().move_to(w6.get_center() + 0.7*m.RIGHT)
        bw13 = bw1.copy().move_to(w7.get_center() + 0.7*m.LEFT)
        bw14 = bw2.copy().move_to(w7.get_center() + 0.7*m.RIGHT)
        bw15 = bw1.copy().move_to(wdots.get_center() + 0.7*m.LEFT)
        bw16 = bw2.copy().move_to(wdots.get_center() + 0.7*m.RIGHT)
        bw17 = bw16.copy().shift(0.2*m.RIGHT)

        ws = m.VGroup(w1, w2, w3, w4, w5, w6, w7, wdots,
                      w, eqw, bw0, bw1, bw2, bw3, bw4, bw5, bw6, bw7, bw8,
                      bw9, bw10, bw11, bw12, bw13, bw14, bw15, bw16, bw17)

        self.play(
            m.FadeIn(yall)
        )
        self.wait()
        self.play(
            yall.animate.shift(3*m.RIGHT),
            m.Write(classtex),
            m.Write(counttex)
        )
        self.play(
            m.Write(class0),
            m.Write(class1)
        )
        self.play(
            m.Write(count0),
            m.Write(count1)
        )
        self.add(y1)
        self.play(
            y1.animate.move_to(class0.get_center())
        )
        self.play(
            m.ChangeDecimalToValue(count0, 1)
        )
        self.add(y2)
        self.play(
            y2.animate.move_to(class1.get_center())
        )
        self.play(
            m.ChangeDecimalToValue(count1, 1)
        )
        self.add(y3)
        self.play(
            y3.animate.move_to(class0.get_center())
        )
        self.play(
            m.ChangeDecimalToValue(count0, 2)
        )
        self.add(y4)
        self.play(
            y4.animate.move_to(class1.get_center())
        )
        self.play(
            m.ChangeDecimalToValue(count1, 2)
        )
        self.add(y5)
        self.play(
            y5.animate.move_to(class1.get_center())
        )
        self.play(
            m.ChangeDecimalToValue(count1, 3)
        )
        self.add(y6)
        self.play(
            y6.animate.move_to(class0.get_center())
        )
        self.play(
            m.ChangeDecimalToValue(count0, 3)
        )
        self.add(y7)
        self.play(
            y7.animate.move_to(class1.get_center())
        )
        self.play(
            m.ChangeDecimalToValue(count1, 4)
        )
        self.wait()
        self.play(
            m.Write(weighttex)
        )
        self.play(
            m.Write(weight0)
        )
        self.play(
            m.Write(weight1)
        )
        self.wait()
        self.play(
            m.FadeOut(classtex, counttex, weighttex),
            m.FadeOut(class0, count0, weight0),
            m.FadeOut(class1, count1, weight1),
            m.FadeOut(y1, y2, y3, y4, y5, y6, y7)
        )
        self.play(
            m.Create(ws)
        )
        self.wait()
# ---------------------------------------------------------------------------
class Cell14(m.Scene):
    def construct(self):

        tab = m.Table(
            [["45", "9120", "0.3241", "\\dots"],
            ["52", "2600", "0.8544", "\\dots"],
            ["\\vdots", "\\vdots", "\\vdots", "\\ddots"]],
            top_left_entry = m.Tex("TRAINING"),
            col_labels = [m.Tex("Age"),
                          m.Tex("Monthly Income"),
                          m.Tex("Debt Ratio"),
                          m.MathTex("\\dots")],
            row_labels = [m.DecimalNumber(1),
                          m.DecimalNumber(2),
                          m.MathTex("\\vdots")]
        )

        lU = m.Line(
            start = 1.26*m.UP + 5.32*m.LEFT,
            end = 1.26*m.UP + 5.32*m.RIGHT
        )
        lL = m.Line(
            start = 1.26*m.UP + 5.32*m.LEFT,
            end = 1.26*m.DOWN + 5.32*m.LEFT
        )

        counter = 0
        edges = []
        partitions = []
        layers = [11, 8, 8, 8, 1]

        for i in layers:
            partitions.append(list(range(counter + 1, counter + i + 1)))
            counter += i
        for i, v in enumerate(layers[1:]):
                last = sum(layers[:i + 1])
                for j in range(v):
                    for k in range(last - layers[i], last):
                        edges.append((k + 1, j + last + 1))

        vertices = np.arange(1, sum(layers) + 1)

        dx = 2
        layout = {}
        for part in partitions:
            for node_index, node in enumerate(part):
                if node in range(1, 12):
                    layout[node] = [-2*dx, 3.5 - 0.7*node_index, 0]
                elif node in range(12, 20):
                    layout[node] = [-dx, 2.45 - 0.7*node_index, 0]
                elif node in range(20, 28):
                    layout[node] = [0, 2.45 - 0.7*node_index, 0]
                elif node in range(28, 36):
                    layout[node] = [dx, 2.45 - 0.7*node_index, 0]
                else:
                    layout[node] = [2*dx, 0, 0]

        network = m.Graph(
            vertices,
            edges,
            layout = layout,
            vertex_config = {"color": c},
            edge_config = {"color": c, "stroke_width": 1.0}
        ).shift(0.2*m.RIGHT)

        age = tab.get_col_labels()[0]
        income = tab.get_col_labels()[1]
        ratio = tab.get_col_labels()[2]
        debt = m.Tex("Total Debt").scale(0.8).move_to(layout[4] + 1.5*m.LEFT)
        unsecure = m.Tex("Unsecured Lines").scale(0.8).move_to(layout[5] + 1.5*m.LEFT)
        credit = m.Tex("Credit Card Loans").scale(0.8).move_to(layout[6] + 1.5*m.LEFT)
        estate = m.Tex("Real Estate Loans").scale(0.8).move_to(layout[7] + 1.5*m.LEFT)
        dependents = m.Tex("Dependents").scale(0.8).move_to(layout[8] + 1.5*m.LEFT)
        late3059 = m.Tex("30-59 Days Late").scale(0.8).move_to(layout[9] + 1.5*m.LEFT)
        late6089 = m.Tex("60-59 Days Late").scale(0.8).move_to(layout[10] + 1.5*m.LEFT)
        late90 = m.Tex("90 Days Late").scale(0.8).move_to(layout[11] + 1.5*m.LEFT)
        rest = m.VGroup(debt, unsecure, credit, estate, dependents, late3059, late6089, late90)
        delinquency = m.Tex("Delinquency").scale(0.8).move_to(layout[36] + 1.5*m.RIGHT)

        r1 = m.RoundedRectangle(
            width = 2.9,
            height = 0.5,
            corner_radius = 0.1,
            color = m.BLUE
        ).move_to(layout[1] + 1.5*m.LEFT)
        r2 = r1.copy().move_to(layout[2] + 1.5*m.LEFT)
        r3 = r1.copy().move_to(layout[3] + 1.5*m.LEFT)
        r4 = r1.copy().move_to(layout[4] + 1.5*m.LEFT)
        r5 = r1.copy().move_to(layout[5] + 1.5*m.LEFT)
        r6 = r1.copy().move_to(layout[6] + 1.5*m.LEFT)
        r7 = r1.copy().move_to(layout[7] + 1.5*m.LEFT)
        r8 = r1.copy().move_to(layout[8] + 1.5*m.LEFT)
        r9 = r1.copy().move_to(layout[9] + 1.5*m.LEFT)
        r10 = r1.copy().move_to(layout[10] + 1.5*m.LEFT)
        r11 = r1.copy().move_to(layout[11] + 1.5*m.LEFT)
        rect = m.VGroup(r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11)
        r12 = m.RoundedRectangle(
            width = 2.2,
            height = 0.5,
            corner_radius = 0.1,
            color = m.RED
        ).move_to(layout[36] + 1.5*m.RIGHT)

        self.play(
            m.FadeIn(tab, lU, lL)
        )
        self.wait()
        self.play(
            m.FadeOut(tab, lU, lL),
            age.animate.scale(0.8).move_to(layout[1] + 1.5*m.LEFT),
            income.animate.scale(0.8).move_to(layout[2] + 1.5*m.LEFT),
            ratio.animate.scale(0.8).move_to(layout[3] + 1.5*m.LEFT),
            m.Create(network)
        )
        self.add(age, income, ratio)
        self.play(
            m.Create(rect),
            m.Create(rest)
        )
        self.play(
            m.Create(r12),
            m.Create(delinquency)
        )
        self.wait()
# ---------------------------------------------------------------------------
class Cell15(m.Scene):
    def construct(self):

        counter = 0
        edges = []
        partitions = []
        layers = [11, 8, 8, 8, 1]

        for i in layers:
            partitions.append(list(range(counter + 1, counter + i + 1)))
            counter += i
        for i, v in enumerate(layers[1:]):
                last = sum(layers[:i + 1])
                for j in range(v):
                    for k in range(last - layers[i], last):
                        edges.append((k + 1, j + last + 1))

        vertices = np.arange(1, sum(layers) + 1)

        dx = 2
        layout = {}
        for part in partitions:
            for node_index, node in enumerate(part):
                if node in range(1, 12):
                    layout[node] = [-2*dx, 3.5 - 0.7*node_index, 0]
                elif node in range(12, 20):
                    layout[node] = [-dx, 2.45 - 0.7*node_index, 0]
                elif node in range(20, 28):
                    layout[node] = [0, 2.45 - 0.7*node_index, 0]
                elif node in range(28, 36):
                    layout[node] = [dx, 2.45 - 0.7*node_index, 0]
                else:
                    layout[node] = [2*dx, 0, 0]

        network = m.Graph(
            vertices,
            edges,
            layout = layout,
            vertex_config = {"color": c},
            edge_config = {"color": c, "stroke_width": 1.0}
        ).shift(0.2*m.RIGHT)

        age = m.Tex("Age").scale(0.8).move_to(layout[1] + 1.5*m.LEFT)
        income = m.Tex("Monthly Income").scale(0.8).move_to(layout[2] + 1.5*m.LEFT)
        ratio = m.Tex("Debt Ratio").scale(0.8).move_to(layout[3] + 1.5*m.LEFT)
        debt = m.Tex("Total Debt").scale(0.8).move_to(layout[4] + 1.5*m.LEFT)
        unsecure = m.Tex("Unsecured Lines").scale(0.8).move_to(layout[5] + 1.5*m.LEFT)
        credit = m.Tex("Credit Card Loans").scale(0.8).move_to(layout[6] + 1.5*m.LEFT)
        estate = m.Tex("Real Estate Loans").scale(0.8).move_to(layout[7] + 1.5*m.LEFT)
        dependents = m.Tex("Dependents").scale(0.8).move_to(layout[8] + 1.5*m.LEFT)
        late3059 = m.Tex("30-59 Days Late").scale(0.8).move_to(layout[9] + 1.5*m.LEFT)
        late6089 = m.Tex("60-59 Days Late").scale(0.8).move_to(layout[10] + 1.5*m.LEFT)
        late90 = m.Tex("90 Days Late").scale(0.8).move_to(layout[11] + 1.5*m.LEFT)
        params = m.VGroup(age, income, ratio, debt, unsecure, credit,
                          estate, dependents, late3059, late6089, late90)
        delinquency = m.Tex("Delinquency").scale(0.8).move_to(layout[36] + 1.5*m.RIGHT)

        r1 = m.RoundedRectangle(
            width = 2.9,
            height = 0.5,
            corner_radius = 0.1,
            color = m.BLUE
        ).move_to(layout[1] + 1.5*m.LEFT)
        r2 = r1.copy().move_to(layout[2] + 1.5*m.LEFT)
        r3 = r1.copy().move_to(layout[3] + 1.5*m.LEFT)
        r4 = r1.copy().move_to(layout[4] + 1.5*m.LEFT)
        r5 = r1.copy().move_to(layout[5] + 1.5*m.LEFT)
        r6 = r1.copy().move_to(layout[6] + 1.5*m.LEFT)
        r7 = r1.copy().move_to(layout[7] + 1.5*m.LEFT)
        r8 = r1.copy().move_to(layout[8] + 1.5*m.LEFT)
        r9 = r1.copy().move_to(layout[9] + 1.5*m.LEFT)
        r10 = r1.copy().move_to(layout[10] + 1.5*m.LEFT)
        r11 = r1.copy().move_to(layout[11] + 1.5*m.LEFT)
        rect = m.VGroup(r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11)
        r12 = m.RoundedRectangle(
            width = 2.2,
            height = 0.5,
            corner_radius = 0.1,
            color = m.RED
        ).move_to(layout[36] + 1.5*m.RIGHT)

        m1 = []
        for i in range(1, 12):
            m1.append(m.DecimalNumber(i).move_to(network.vertices[i].get_center() + 1.5*m.RIGHT))
        
        n1 = []
        for i in range(12, 20):
            n1.append(m.DecimalNumber(i - 11).move_to(network.vertices[i].get_center() + 2.5*m.RIGHT))
        
        edges1 = m.VGroup()
        edges2 = m.VGroup()
        edges3 = m.VGroup()
        edges4 = m.VGroup()
        edges5 = m.VGroup()
        edges6 = m.VGroup()
        edges7 = m.VGroup()
        edges8 = m.VGroup()
        edges9 = m.VGroup()
        edges10 = m.VGroup()
        edges11 = m.VGroup()
        for i in range(12, 20):
            edges1.add(network.edges[(1, i)])
            edges2.add(network.edges[(2, i)])
            edges3.add(network.edges[(3, i)])
            edges4.add(network.edges[(4, i)])
            edges5.add(network.edges[(5, i)])
            edges6.add(network.edges[(6, i)])
            edges7.add(network.edges[(7, i)])
            edges8.add(network.edges[(8, i)])
            edges9.add(network.edges[(9, i)])
            edges10.add(network.edges[(10, i)])
            edges11.add(network.edges[(11, i)])

        w111 = m.MathTex("w_{11}^1").move_to(network.edges[(1, 12)].get_center() + 0.3*m.UP + 2.4*m.RIGHT)
        w121 = m.MathTex("w_{12}^1").scale(0.6).move_to(0.75*m.UP + 6*m.LEFT)
        w131 = m.MathTex("w_{13}^1").scale(0.6).move_to(0.75*m.UP + 5.5*m.LEFT)
        w141 = m.MathTex("w_{14}^1").scale(0.6).move_to(0.75*m.UP + 5*m.LEFT)
        w151 = m.MathTex("w_{15}^1").scale(0.6).move_to(0.75*m.UP + 4.5*m.LEFT)
        w161 = m.MathTex("w_{16}^1").scale(0.6).move_to(0.75*m.UP + 4*m.LEFT)
        w171 = m.MathTex("w_{17}^1").scale(0.6).move_to(0.75*m.UP + 3.5*m.LEFT)
        w181 = m.MathTex("w_{18}^1").scale(0.6).move_to(0.75*m.UP + 3*m.LEFT)
        restw1 = m.VGroup(w121, w131, w141, w151, w161, w171, w181)

        w211 = m.MathTex("w_{21}^1").scale(0.6).move_to(0.25*m.UP + 6.5*m.LEFT)
        w221 = m.MathTex("w_{22}^1").scale(0.6).move_to(0.25*m.UP + 6*m.LEFT)
        w231 = m.MathTex("w_{23}^1").scale(0.6).move_to(0.25*m.UP + 5.5*m.LEFT)
        w241 = m.MathTex("w_{24}^1").scale(0.6).move_to(0.25*m.UP + 5*m.LEFT)
        w251 = m.MathTex("w_{25}^1").scale(0.6).move_to(0.25*m.UP + 4.5*m.LEFT)
        w261 = m.MathTex("w_{26}^1").scale(0.6).move_to(0.25*m.UP + 4*m.LEFT)
        w271 = m.MathTex("w_{27}^1").scale(0.6).move_to(0.25*m.UP + 3.5*m.LEFT)
        w281 = m.MathTex("w_{28}^1").scale(0.6).move_to(0.25*m.UP + 3*m.LEFT)
        allw2 = m.VGroup(w211, w221, w231, w241, w251, w261, w271, w281)

        w311 = m.MathTex("w_{31}^1").scale(0.6).move_to(0.25*m.DOWN + 6.5*m.LEFT)
        w321 = m.MathTex("w_{32}^1").scale(0.6).move_to(0.25*m.DOWN + 6*m.LEFT)
        w331 = m.MathTex("w_{33}^1").scale(0.6).move_to(0.25*m.DOWN + 5.5*m.LEFT)
        w341 = m.MathTex("w_{34}^1").scale(0.6).move_to(0.25*m.DOWN + 5*m.LEFT)
        w351 = m.MathTex("w_{35}^1").scale(0.6).move_to(0.25*m.DOWN + 4.5*m.LEFT)
        w361 = m.MathTex("w_{36}^1").scale(0.6).move_to(0.25*m.DOWN + 4*m.LEFT)
        w371 = m.MathTex("w_{37}^1").scale(0.6).move_to(0.25*m.DOWN + 3.5*m.LEFT)
        w381 = m.MathTex("w_{38}^1").scale(0.6).move_to(0.25*m.DOWN + 3*m.LEFT)
        allw3 = m.VGroup(w311, w321, w331, w341, w351, w361, w371, w381)

        d1 = m.MathTex("\\vdots").scale(0.6).move_to(0.75*m.DOWN + 6.5*m.LEFT)
        d2 = m.MathTex("\\vdots").scale(0.6).move_to(0.75*m.DOWN + 6*m.LEFT)
        d3 = m.MathTex("\\vdots").scale(0.6).move_to(0.75*m.DOWN + 5.5*m.LEFT)
        d4 = m.MathTex("\\vdots").scale(0.6).move_to(0.75*m.DOWN + 5*m.LEFT)
        d5 = m.MathTex("\\vdots").scale(0.6).move_to(0.75*m.DOWN + 4.5*m.LEFT)
        d6 = m.MathTex("\\vdots").scale(0.6).move_to(0.75*m.DOWN + 4*m.LEFT)
        d7 = m.MathTex("\\vdots").scale(0.6).move_to(0.75*m.DOWN + 3.5*m.LEFT)
        d8 = m.MathTex("\\vdots").scale(0.6).move_to(0.75*m.DOWN + 3*m.LEFT)
        dots = m.VGroup(d1, d2, d3, d4, d5, d6, d7, d8)

        W1 = m.VGroup(w111, restw1, allw2, allw3, dots)
        W1tex = m.MathTex("[W^1]_{11 \\times 8}").move_to(4.75*m.LEFT)

        n2 = m.VGroup([e.copy() for e in n1]).shift(2*m.RIGHT)

        W2 = m.MathTex("[W^2]_{8 \\times 8}").move_to(0.5*m.DOWN + 4.75*m.LEFT)

        n3 = m.VGroup([e.copy() for e in n1]).shift(4*m.RIGHT)

        W3 = m.MathTex("[W^3]_{8 \\times 8}").move_to(1*m.DOWN + 4.75*m.LEFT)

        n4 = m.DecimalNumber(1).move_to(network.vertices[36].get_center() + 2.5*m.RIGHT)

        W4 = m.MathTex("[W^4]_{8 \\times 1}").move_to(1.5*m.DOWN + 4.75*m.LEFT)

        nb = []
        for i in range(8):
            nb.append(m.DecimalNumber(i + 1).move_to(network.vertices[i + 12].get_center() + 2.5*m.RIGHT))
        
        b11 = m.MathTex("b_1^1").move_to(network.vertices[12].get_center() + 0.6*m.UP + 2*m.RIGHT)
        b21 = m.MathTex("b_2^1").scale(0.6).move_to(6*m.LEFT)
        b31 = m.MathTex("b_3^1").scale(0.6).move_to(5.5*m.LEFT)
        b41 = m.MathTex("b_4^1").scale(0.6).move_to(5*m.LEFT)
        b51 = m.MathTex("b_5^1").scale(0.6).move_to(4.5*m.LEFT)
        b61 = m.MathTex("b_6^1").scale(0.6).move_to(4*m.LEFT)
        b71 = m.MathTex("b_7^1").scale(0.6).move_to(3.5*m.LEFT)
        b81 = m.MathTex("b_8^1").scale(0.6).move_to(3*m.LEFT)
        restb1 = m.VGroup(b21, b31, b41, b51, b61, b71, b81)

        b1 = m.VGroup(b11, restb1)
        b1tex = m.MathTex("[b^1]_{1 \\times 8}").move_to(1.5*m.UP + 4*m.LEFT)

        nb2 = m.VGroup([e.copy() for e in nb]).shift(2*m.RIGHT)

        b2 = m.MathTex("[b^2]_{1 \\times 8}").move_to(0.5*m.UP + 4*m.LEFT)

        nb3 = m.VGroup([e.copy() for e in nb]).shift(4*m.RIGHT)

        b3 = m.MathTex("[b^3]_{1 \\times 8}").move_to(0.5*m.DOWN + 4*m.LEFT)

        nb4 = m.DecimalNumber(1).move_to(network.vertices[36].get_center() + 2.5*m.RIGHT)

        b4 = m.MathTex("[b^4]_{1 \\times 1}").move_to(1.5*m.DOWN + 4*m.LEFT)

        W = m.MathTex("W").move_to(0.5*m.UP + 4*m.LEFT)
        eqW = m.MathTex("=").move_to(W.get_center() + 0.5*m.RIGHT)
        b1W = m.MathTex("[").move_to(eqW.get_center() + 0.025*m.DOWN + 0.4*m.RIGHT)
        b2W = m.MathTex("]").move_to(eqW.get_center() + 0.025*m.DOWN + 8.5*m.RIGHT)
        c1W = m.MathTex(",").move_to(0.3*m.UP + 1*m.LEFT)
        c2W = c1W.copy().shift(2*m.RIGHT)
        c3W = c1W.copy().shift(4*m.RIGHT)
        We = m.VGroup(W, eqW, b1W, b2W, c1W, c2W, c3W).shift(0.5*m.LEFT)

        b = m.MathTex("b").move_to(0.5*m.DOWN + 4*m.LEFT)
        eqb = m.MathTex("=").move_to(b.get_center() + 0.5*m.RIGHT)
        b1b = m.MathTex("[").move_to(eqb.get_center() + 0.025*m.DOWN + 0.4*m.RIGHT)
        b2b = m.MathTex("]").move_to(eqb.get_center() + 0.025*m.DOWN + 8.5*m.RIGHT)
        c1b = m.MathTex(",").move_to(0.7*m.DOWN + 1*m.LEFT)
        c2b = c1b.copy().shift(2*m.RIGHT)
        c3b = c1b.copy().shift(4*m.RIGHT)
        be = m.VGroup(b, eqb, b1b, b2b, c1b, c2b, c3b).shift(0.5*m.LEFT)

        self.play(
            m.FadeIn(network, params, delinquency, rect, r12)
        )
        self.wait()
        self.play(
            m.FadeOut(params, delinquency, rect, r12),
            network.animate.shift(2*m.RIGHT)
        )
        self.wait()
        self.play(
            network.edges[(1, 12)].animate.set_stroke_width(10.0)
        )
        self.play(
            m.Write(m1[0])
        )
        self.play(
            m.Write(n1[0])
        )
        self.play(
            m.Write(w111)
        )
        self.play(
            w111.animate.scale(0.6).move_to(0.75*m.UP + 6.5*m.LEFT)
        )
        for i in range(13, 20):
            self.play(
                m.FadeIn(n1[i - 12]),
                network.edges[(1, i)].animate.set_stroke_width(10.0),
                run_time = 0.1
            )
        self.play(
            m.Create(restw1)
        )
        self.play(
            m.Write(m1[1]),
            [e.animate.set_stroke_width(1.0) for e in edges1],
            [e.animate.set_stroke_width(10.0) for e in edges2]
        )
        self.play(
            m.Create(allw2)
        )
        self.play(
            m.Write(m1[2]),
            [e.animate.set_stroke_width(1.0) for e in edges2],
            [e.animate.set_stroke_width(10.0) for e in edges3]
        )
        self.play(
            m.Create(allw3)
        )
        self.play(
            m.Write(d1),
            m.Write(m1[3]),
            [e.animate.set_stroke_width(1.0) for e in edges3],
            [e.animate.set_stroke_width(10.0) for e in edges4],
            run_time = 0.1
        )
        self.play(
            m.Write(d2),
            m.Write(m1[4]),
            [e.animate.set_stroke_width(1.0) for e in edges4],
            [e.animate.set_stroke_width(10.0) for e in edges5],
            run_time = 0.1
        )
        self.play(
            m.Write(d3),
            m.Write(m1[5]),
            [e.animate.set_stroke_width(1.0) for e in edges5],
            [e.animate.set_stroke_width(10.0) for e in edges6],
            run_time = 0.1
        )
        self.play(
            m.Write(d4),
            m.Write(m1[6]),
            [e.animate.set_stroke_width(1.0) for e in edges6],
            [e.animate.set_stroke_width(10.0) for e in edges7],
            run_time = 0.1
        )
        self.play(
            m.Write(d5),
            m.Write(m1[7]),
            [e.animate.set_stroke_width(1.0) for e in edges7],
            [e.animate.set_stroke_width(10.0) for e in edges8],
            run_time = 0.1
        )
        self.play(
            m.Write(d6),
            m.Write(m1[8]),
            [e.animate.set_stroke_width(1.0) for e in edges8],
            [e.animate.set_stroke_width(10.0) for e in edges9],
            run_time = 0.1
        )
        self.play(
            m.Write(d7),
            m.Write(m1[9]),
            [e.animate.set_stroke_width(1.0) for e in edges9],
            [e.animate.set_stroke_width(10.0) for e in edges10],
            run_time = 0.1
        )
        self.play(
            m.Write(d8),
            m.Write(m1[10]),
            [e.animate.set_stroke_width(1.0) for e in edges10],
            [e.animate.set_stroke_width(10.0) for e in edges11],
            run_time = 0.1
        )
        self.play(
            [e.animate.set_stroke_width(1.0) for e in edges11],
            run_time = 0.1
        )
        self.play(
            m.Transform(W1, W1tex)
        )
        self.play(
            [m.FadeOut(e) for e in m1],
            [e.animate.shift(1*m.LEFT) for e in n1],
            m.Create(n2)
        )
        for i in range(20, 28):
            self.play(
                network.edges[(12, i)].animate.set_stroke_width(10.0),
                run_time = 0.1
            )
        for i in range(13, 20):
            self.play(
                network.edges[(i - 1, 20)].animate.set_stroke_width(1.0),
                network.edges[(i - 1, 21)].animate.set_stroke_width(1.0),
                network.edges[(i - 1, 22)].animate.set_stroke_width(1.0),
                network.edges[(i - 1, 23)].animate.set_stroke_width(1.0),
                network.edges[(i - 1, 24)].animate.set_stroke_width(1.0),
                network.edges[(i - 1, 25)].animate.set_stroke_width(1.0),
                network.edges[(i - 1, 26)].animate.set_stroke_width(1.0),
                network.edges[(i - 1, 27)].animate.set_stroke_width(1.0),
                network.edges[(i, 20)].animate.set_stroke_width(10.0),
                network.edges[(i, 21)].animate.set_stroke_width(10.0),
                network.edges[(i, 22)].animate.set_stroke_width(10.0),
                network.edges[(i, 23)].animate.set_stroke_width(10.0),
                network.edges[(i, 24)].animate.set_stroke_width(10.0),
                network.edges[(i, 25)].animate.set_stroke_width(10.0),
                network.edges[(i, 26)].animate.set_stroke_width(10.0),
                network.edges[(i, 27)].animate.set_stroke_width(10.0),
                run_time = 0.1
            )
        self.play(
            network.edges[(19, 20)].animate.set_stroke_width(1.0),
            network.edges[(19, 21)].animate.set_stroke_width(1.0),
            network.edges[(19, 22)].animate.set_stroke_width(1.0),
            network.edges[(19, 23)].animate.set_stroke_width(1.0),
            network.edges[(19, 24)].animate.set_stroke_width(1.0),
            network.edges[(19, 25)].animate.set_stroke_width(1.0),
            network.edges[(19, 26)].animate.set_stroke_width(1.0),
            network.edges[(19, 27)].animate.set_stroke_width(1.0),
            run_time = 0.1
        )
        self.play(
            W1.animate.shift(0.5*m.UP),
            m.Write(W2)
        )
        self.play(
            [m.FadeOut(e) for e in n1],
            [e.animate.shift(1*m.LEFT) for e in n2],
            m.Create(n3)
        )
        for i in range(28, 36):
            self.play(
                network.edges[(20, i)].animate.set_stroke_width(10.0),
                run_time = 0.1
            )
        for i in range(21, 28):
            self.play(
                network.edges[(i - 1, 28)].animate.set_stroke_width(1.0),
                network.edges[(i - 1, 29)].animate.set_stroke_width(1.0),
                network.edges[(i - 1, 30)].animate.set_stroke_width(1.0),
                network.edges[(i - 1, 31)].animate.set_stroke_width(1.0),
                network.edges[(i - 1, 32)].animate.set_stroke_width(1.0),
                network.edges[(i - 1, 33)].animate.set_stroke_width(1.0),
                network.edges[(i - 1, 34)].animate.set_stroke_width(1.0),
                network.edges[(i - 1, 35)].animate.set_stroke_width(1.0),
                network.edges[(i, 28)].animate.set_stroke_width(10.0),
                network.edges[(i, 29)].animate.set_stroke_width(10.0),
                network.edges[(i, 30)].animate.set_stroke_width(10.0),
                network.edges[(i, 31)].animate.set_stroke_width(10.0),
                network.edges[(i, 32)].animate.set_stroke_width(10.0),
                network.edges[(i, 33)].animate.set_stroke_width(10.0),
                network.edges[(i, 34)].animate.set_stroke_width(10.0),
                network.edges[(i, 35)].animate.set_stroke_width(10.0),
                run_time = 0.1
            )
        self.play(
            network.edges[(27, 28)].animate.set_stroke_width(1.0),
            network.edges[(27, 29)].animate.set_stroke_width(1.0),
            network.edges[(27, 30)].animate.set_stroke_width(1.0),
            network.edges[(27, 31)].animate.set_stroke_width(1.0),
            network.edges[(27, 32)].animate.set_stroke_width(1.0),
            network.edges[(27, 33)].animate.set_stroke_width(1.0),
            network.edges[(27, 34)].animate.set_stroke_width(1.0),
            network.edges[(27, 35)].animate.set_stroke_width(1.0),
            run_time = 0.1
        )
        self.play(
            W1.animate.shift(0.5*m.UP),
            W2.animate.shift(0.5*m.UP),
            m.Write(W3)
        )
        self.play(
            [m.FadeOut(e) for e in n2],
            [e.animate.shift(1*m.LEFT) for e in n3],
            m.Create(n4)
        )
        self.play(
            network.edges[(28, 36)].animate.set_stroke_width(10.0),
            run_time = 0.1
        )
        for i in range(29, 36):
            self.play(
                network.edges[(i - 1, 36)].animate.set_stroke_width(1.0),
                network.edges[(i, 36)].animate.set_stroke_width(10.0),
                run_time = 0.1
            )
        self.play(
            network.edges[(35, 36)].animate.set_stroke_width(1.0),
            run_time = 0.1
        )
        self.play(
            W1.animate.shift(0.5*m.UP),
            W2.animate.shift(0.5*m.UP),
            W3.animate.shift(0.5*m.UP),
            m.Write(W4)
        )
        self.play(
            [m.FadeOut(e) for e in n3],
            m.FadeOut(n4)
        )
        self.wait()
        self.play(
            W1.animate.move_to(3.5*m.UP + 6*m.LEFT),
            W2.animate.move_to(2.75*m.UP + 6*m.LEFT),
            W3.animate.move_to(2*m.UP + 6*m.LEFT),
            W4.animate.move_to(1.25*m.UP + 6*m.LEFT),
        )
        self.play(
            network.vertices[12].animate.scale(3)
        )
        self.play(
            m.Write(nb[0])
        )
        self.play(
            m.Write(b11)
        )
        self.play(
            b11.animate.scale(0.6).move_to(6.5*m.LEFT)
        )
        for i in range(13, 20):
            self.play(
                m.FadeIn(nb[i - 12]),
                network.vertices[i].animate.scale(3),
                run_time = 0.1
            )
        self.play(
            m.Create(restb1)
        )
        self.play(
            W1.animate.move_to(1.5*m.UP + 6*m.LEFT),
            W2.animate.move_to(0.5*m.UP + 6*m.LEFT),
            W3.animate.move_to(0.5*m.DOWN + 6*m.LEFT),
            W4.animate.move_to(1.5*m.DOWN + 6*m.LEFT),
            m.Transform(b1, b1tex)
        )
        for i in range(12, 20):
            self.play(
                m.FadeOut(nb[i - 12]),
                network.vertices[i].animate.scale(1/3),
                run_time = 0.1
            )
        for i in range(20, 28):
            self.play(
                m.FadeIn(nb2[i - 20]),
                network.vertices[i].animate.scale(3),
                run_time = 0.1
            )
        self.play(
            m.Write(b2)
        )
        for i in range(20, 28):
            self.play(
                m.FadeOut(nb2[i - 20]),
                network.vertices[i].animate.scale(1/3),
                run_time = 0.1
            )
        for i in range(28, 36):
            self.play(
                m.FadeIn(nb3[i - 28]),
                network.vertices[i].animate.scale(3),
                run_time = 0.1
            )
        self.play(
            m.Write(b3)
        )
        for i in range(28, 36):
            self.play(
                m.FadeOut(nb3[i - 28]),
                network.vertices[i].animate.scale(1/3),
                run_time = 0.1
            )
        self.play(
            m.FadeIn(nb4),
            network.vertices[36].animate.scale(3),
            run_time = 0.1
        )
        self.play(
            m.Write(b4)
        )
        self.play(
            m.FadeOut(nb4),
            network.vertices[36].animate.scale(1/3),
            run_time = 0.1
        )
        self.wait()
        self.play(
            m.FadeOut(network),
            W1.animate.move_to(0.5*m.UP + 2.5*m.LEFT),
            W2.animate.move_to(0.5*m.UP + 0.5*m.LEFT),
            W3.animate.move_to(0.5*m.UP + 1.5*m.RIGHT),
            W4.animate.move_to(0.5*m.UP + 3.5*m.RIGHT),
            b1.animate.move_to(0.5*m.DOWN + 2.5*m.LEFT),
            b2.animate.move_to(0.5*m.DOWN + 0.5*m.LEFT),
            b3.animate.move_to(0.5*m.DOWN + 1.5*m.RIGHT),
            b4.animate.move_to(0.5*m.DOWN + 3.5*m.RIGHT),
            m.Create(We),
            m.Create(be)
        )
        self.wait()
# ---------------------------------------------------------------------------
class Cell16(m.Scene):
    def construct(self):

        ax = m.Axes(
            x_range = [-7, 7, 5],
            y_range = [0, 1.2, 1],
            tips = False,
            axis_config = {"include_numbers": True}
        )

        xlab = ax.get_x_axis_label(m.MathTex("x"), edge = m.RIGHT, direction = m.DOWN)
        ylab = ax.get_y_axis_label(m.MathTex("y"), edge = m.UP, direction = m.LEFT)

        axlab = m.VGroup(ax, xlab, ylab)

        dx = 14/1000

        curve = ax.plot(
            lambda x: 1/(1 + np.exp(-x)),
            x_range = (-7, 7, dx),
            stroke_width = 10.0,
            color = c,
            use_smoothing = False
        )

        sigmoid = m.MathTex("\\sigma (x)").move_to(ax.coords_to_point(6, 1.1))

        self.play(
            m.Create(axlab)
        )
        self.play(
            m.Create(curve)
        )
        self.play(
            m.Write(sigmoid)
        )
        self.wait()
# ---------------------------------------------------------------------------
class Cell17(m.Scene):
    def construct(self):

        ax = m.Axes(
            x_range = [-1.2, 1.2, 1],
            y_range = [0, 1.2, 1],
            tips = False,
            axis_config = {"include_numbers": True}
        )

        xlab = ax.get_x_axis_label(m.MathTex("x"), edge = m.RIGHT, direction = m.DOWN)
        ylab = ax.get_y_axis_label(m.MathTex("y"), edge = m.UP, direction = m.LEFT)

        axlab = m.VGroup(ax, xlab, ylab)

        dx = 2.4/1000

        curve = ax.plot(
            lambda x: np.maximum(0, x),
            x_range = (-1.2, 1.2, dx),
            stroke_width = 10.0,
            color = c,
            use_smoothing = False
        )

        relu = m.MathTex("\\mathrm{ReLU}(x)").move_to(ax.coords_to_point(0.85, 1.1))

        self.play(
            m.Create(axlab)
        )
        self.play(
            m.Create(curve)
        )
        self.play(
            m.Write(relu)
        )
        self.wait()
# ---------------------------------------------------------------------------
class Cell18(m.Scene):
    def construct(self):

        ax = m.Axes(
            x_range = [-1.2, 1.2, 1],
            y_range = [0, 1.2, 1],
            tips = False,
            axis_config = {"include_numbers": True}
        )

        xlab = ax.get_x_axis_label(m.MathTex("x"), edge = m.RIGHT, direction = m.DOWN)
        ylab = ax.get_y_axis_label(m.MathTex("y"), edge = m.UP, direction = m.LEFT)

        axlab = m.VGroup(ax, xlab, ylab)

        dx = 2.4/1000

        curve = ax.plot(
            lambda x: x > 0,
            x_range = (-1.2, 1.2, dx),
            stroke_width = 10.0,
            color = c,
            use_smoothing = False
        )

        heaviside = m.MathTex("H(x)").move_to(ax.coords_to_point(1.1, 1.1))

        self.play(
            m.Create(axlab)
        )
        self.play(
            m.Create(curve)
        )
        self.play(
            m.Write(heaviside)
        )
        self.wait()
# ---------------------------------------------------------------------------
class Cell19(m.Scene):
    def construct(self):

        W1 = m.MathTex("[W^1]_{11 \\times 8}").move_to(0.5*m.UP + 2.5*m.LEFT)
        W2 = m.MathTex("[W^2]_{8 \\times 8}").move_to(0.5*m.UP + 0.5*m.LEFT)
        W3 = m.MathTex("[W^3]_{8 \\times 8}").move_to(0.5*m.UP + 1.5*m.RIGHT)
        W4 = m.MathTex("[W^4]_{8 \\times 1}").move_to(0.5*m.UP + 3.5*m.RIGHT)

        W = m.MathTex("W").move_to(0.5*m.UP + 4*m.LEFT)
        eqW = m.MathTex("=").move_to(W.get_center() + 0.5*m.RIGHT)
        b1W = m.MathTex("[").move_to(eqW.get_center() + 0.025*m.DOWN + 0.4*m.RIGHT)
        b2W = m.MathTex("]").move_to(eqW.get_center() + 0.025*m.DOWN + 8.5*m.RIGHT)
        c1W = m.MathTex(",").move_to(0.3*m.UP + 1*m.LEFT)
        c2W = c1W.copy().shift(2*m.RIGHT)
        c3W = c1W.copy().shift(4*m.RIGHT)
        We = m.VGroup(W, eqW, b1W, b2W, c1W, c2W, c3W).shift(0.5*m.LEFT)

        b1 = m.MathTex("[b^1]_{1 \\times 8}").move_to(0.5*m.DOWN + 2.5*m.LEFT)
        b2 = m.MathTex("[b^2]_{1 \\times 8}").move_to(0.5*m.DOWN + 0.5*m.LEFT)
        b3 = m.MathTex("[b^3]_{1 \\times 8}").move_to(0.5*m.DOWN + 1.5*m.RIGHT)
        b4 = m.MathTex("[b^4]_{1 \\times 1}").move_to(0.5*m.DOWN + 3.5*m.RIGHT)

        b = m.MathTex("b").move_to(0.5*m.DOWN + 4*m.LEFT)
        eqb = m.MathTex("=").move_to(b.get_center() + 0.5*m.RIGHT)
        b1b = m.MathTex("[").move_to(eqb.get_center() + 0.025*m.DOWN + 0.4*m.RIGHT)
        b2b = m.MathTex("]").move_to(eqb.get_center() + 0.025*m.DOWN + 8.5*m.RIGHT)
        c1b = m.MathTex(",").move_to(0.7*m.DOWN + 1*m.LEFT)
        c2b = c1b.copy().shift(2*m.RIGHT)
        c3b = c1b.copy().shift(4*m.RIGHT)
        be = m.VGroup(b, eqb, b1b, b2b, c1b, c2b, c3b).shift(0.5*m.LEFT)

        age = m.Tex("Age").scale(0.8).move_to(3.5*m.UP + 5.5*m.LEFT)
        income = m.Tex("Monthly Income").scale(0.8).move_to(2.8*m.UP + 5.5*m.LEFT)
        ratio = m.Tex("Debt Ratio").scale(0.8).move_to(2.1*m.UP + 5.5*m.LEFT)
        debt = m.Tex("Total Debt").scale(0.8).move_to(1.4*m.UP + 5.5*m.LEFT)
        unsecure = m.Tex("Unsecured Lines").scale(0.8).move_to(0.7*m.UP + 5.5*m.LEFT)
        credit = m.Tex("Credit Card Loans").scale(0.8).move_to(5.5*m.LEFT)
        estate = m.Tex("Real Estate Loans").scale(0.8).move_to(0.7*m.DOWN + 5.5*m.LEFT)
        dependents = m.Tex("Dependents").scale(0.8).move_to(1.4*m.DOWN + 5.5*m.LEFT)
        late3059 = m.Tex("30-59 Days Late").scale(0.8).move_to(2.1*m.DOWN + 5.5*m.LEFT)
        late6089 = m.Tex("60-59 Days Late").scale(0.8).move_to(2.8*m.DOWN + 5.5*m.LEFT)
        late90 = m.Tex("90 Days Late").scale(0.8).move_to(3.5*m.DOWN + 5.5*m.LEFT)
        params = m.VGroup(age, income, ratio, debt, unsecure, credit,
                          estate, dependents, late3059, late6089, late90)
        delinquency = m.Tex("Delinquency").scale(0.8).move_to(5.5*m.RIGHT)

        r1 = m.RoundedRectangle(
            width = 2.9,
            height = 0.5,
            corner_radius = 0.1,
            color = m.BLUE
        ).move_to(age.get_center())
        r2 = r1.copy().move_to(income.get_center())
        r3 = r1.copy().move_to(ratio.get_center())
        r4 = r1.copy().move_to(debt.get_center())
        r5 = r1.copy().move_to(unsecure.get_center())
        r6 = r1.copy().move_to(credit.get_center())
        r7 = r1.copy().move_to(estate.get_center())
        r8 = r1.copy().move_to(dependents.get_center())
        r9 = r1.copy().move_to(late3059.get_center())
        r10 = r1.copy().move_to(late6089.get_center())
        r11 = r1.copy().move_to(late90.get_center())
        rect = m.VGroup(r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11)
        r12 = m.RoundedRectangle(
            width = 2.2,
            height = 0.5,
            corner_radius = 0.1,
            color = m.RED
        ).move_to(delinquency.get_center())

        agerect = m.VGroup(age, r1)
        incomerect = m.VGroup(income, r2)
        ratiorect = m.VGroup(ratio, r3)
        debtrect = m.VGroup(debt, r4)
        unsecurerect = m.VGroup(unsecure, r5)
        creditrect = m.VGroup(credit, r6)
        estaterect = m.VGroup(estate, r7)
        dependentsrect = m.VGroup(dependents, r8)
        late3059rect = m.VGroup(late3059, r9)
        late6089rect = m.VGroup(late6089, r10)
        late90rect = m.VGroup(late90, r11)
        X = m.VGroup(agerect, incomerect, ratiorect, debtrect, unsecurerect, creditrect,
                     estaterect, dependentsrect, late3059rect, late6089rect, late90rect)
        y = m.VGroup(delinquency, r12)

        x1 = m.MathTex("x_1").move_to(agerect.get_center())
        x2 = m.MathTex("x_2").move_to(incomerect.get_center())
        x3 = m.MathTex("x_3").move_to(ratiorect.get_center())
        x4 = m.MathTex("x_4").move_to(debtrect.get_center())
        x5 = m.MathTex("x_5").move_to(unsecurerect.get_center())
        x6 = m.MathTex("x_6").move_to(creditrect.get_center())
        x7 = m.MathTex("x_7").move_to(estaterect.get_center())
        x8 = m.MathTex("x_8").move_to(dependentsrect.get_center())
        x9 = m.MathTex("x_9").move_to(late3059rect.get_center())
        x10 = m.MathTex("x_{10}").move_to(late6089rect.get_center())
        x11 = m.MathTex("x_{11}").move_to(late90rect.get_center())
        Xx = m.VGroup(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11)
        ytex = m.MathTex("y").move_to(2*m.DOWN + 5*m.RIGHT)

        Xtex = m.MathTex("[X]_{1 \\times 11}").move_to(2*m.LEFT)

        inputtex = m.Tex("input:").move_to(2.5*m.UP + 3.5*m.RIGHT)
        outputtex = m.Tex("output:").move_to(2.5*m.DOWN + 3.5*m.RIGHT)

        a0 = m.MathTex("[a^0] = [X]").move_to(2.5*m.UP + 4*m.LEFT)
        a1 = m.MathTex("[a^1] = \\mathrm{ReLU}([a^0] [W^1] + [b^1])").align_to(a0, m.LEFT).shift(1.5*m.UP)
        a2 = m.MathTex("[a^2] = \\mathrm{ReLU}([a^1] [W^2] + [b^2])").align_to(a0, m.LEFT).shift(0.5*m.UP)
        a3 = m.MathTex("[a^3] = \\mathrm{ReLU}([a^2] [W^3]+ [b^3])").align_to(a0, m.LEFT).shift(0.5*m.DOWN)
        a4 = m.MathTex("[a^4] = \\sigma ([a^3] [W^4] + [b^4])").align_to(a0, m.LEFT).shift(1.5*m.DOWN)
        eq = m.MathTex("y = [a^4]").align_to(a0, m.LEFT).shift(2.5*m.DOWN)

        self.play(
            m.FadeIn(W1, W2, W3, W4, We, b1, b2, b3, b4, be)
        )
        self.play(
            m.FadeOut(We, be)
        )
        self.play(
            W1.animate.shift(0.25*m.LEFT),
            W2.animate.shift(0.25*m.LEFT),
            W3.animate.shift(0.25*m.LEFT),
            W4.animate.shift(0.25*m.LEFT),
            b1.animate.shift(0.25*m.LEFT),
            b2.animate.shift(0.25*m.LEFT),
            b3.animate.shift(0.25*m.LEFT),
            b4.animate.shift(0.25*m.LEFT),
            m.FadeIn(X, y)
        )
        self.wait()
        self.play(
            W1.animate.move_to(2*m.UP + 4*m.RIGHT),
            b1.animate.move_to(2*m.UP + 6*m.RIGHT),
            W2.animate.move_to(1*m.UP + 4*m.RIGHT),
            b2.animate.move_to(1*m.UP + 6*m.RIGHT),
            W3.animate.move_to(4*m.RIGHT),
            b3.animate.move_to(6*m.RIGHT),
            W4.animate.move_to(1*m.DOWN + 4*m.RIGHT),
            b4.animate.move_to(1*m.DOWN + 6*m.RIGHT),
            y.animate.move_to(2*m.DOWN + 5*m.RIGHT)
        )
        self.play(
            m.Transform(X[0], Xx[0]),
            m.Transform(X[1], Xx[1]),
            m.Transform(X[2], Xx[2]),
            m.Transform(X[3], Xx[3]),
            m.Transform(X[4], Xx[4]),
            m.Transform(X[5], Xx[5]),
            m.Transform(X[6], Xx[6]),
            m.Transform(X[7], Xx[7]),
            m.Transform(X[8], Xx[8]),
            m.Transform(X[9], Xx[9]),
            m.Transform(X[10], Xx[10]),
            m.Transform(y, ytex)
        )
        self.play(
            agerect.animate.move_to(6*m.LEFT),
            incomerect.animate.move_to(5.2*m.LEFT),
            ratiorect.animate.move_to(4.4*m.LEFT),
            debtrect.animate.move_to(3.6*m.LEFT),
            unsecurerect.animate.move_to(2.8*m.LEFT),
            creditrect.animate.move_to(2*m.LEFT),
            estaterect.animate.move_to(1.2*m.LEFT),
            dependentsrect.animate.move_to(0.4*m.LEFT),
            late3059rect.animate.move_to(0.4*m.RIGHT),
            late6089rect.animate.move_to(1.2*m.RIGHT),
            late90rect.animate.move_to(2*m.RIGHT)
        )
        self.wait()
        self.play(
            m.Transform(X, Xtex)
        )
        self.wait()
        self.play(
            m.Write(inputtex),
            m.Write(outputtex),
            X.animate.move_to(2.5*m.UP + 5*m.RIGHT),
            W1.animate.move_to(1.5*m.UP + 4*m.RIGHT),
            b1.animate.move_to(1.5*m.UP + 6*m.RIGHT),
            W2.animate.move_to(0.5*m.UP + 4*m.RIGHT),
            b2.animate.move_to(0.5*m.UP + 6*m.RIGHT),
            W3.animate.move_to(0.5*m.DOWN + 4*m.RIGHT),
            b3.animate.move_to(0.5*m.DOWN + 6*m.RIGHT),
            W4.animate.move_to(1.5*m.DOWN + 4*m.RIGHT),
            b4.animate.move_to(1.5*m.DOWN + 6*m.RIGHT),
            y.animate.move_to(2.5*m.DOWN + 5*m.RIGHT)
        )
        self.play(
            m.Write(a0)
        )
        self.play(
            m.Write(a1)
        )
        self.play(
            m.Write(a2)
        )
        self.play(
            m.Write(a3)
        )
        self.play(
            m.Write(a4)
        )
        self.play(
            m.Write(eq)
        )
        self.wait()
# ---------------------------------------------------------------------------
class Cell20(m.Scene):
    def construct(self):

        yb = m.VGroup()
        yb.add(m.MathTex("[").move_to(3.2*m.UP + 1*m.LEFT))
        yb.add(m.MathTex("]").move_to(3.2*m.DOWN + 1*m.RIGHT))
        for i in range(9):
            yb.add(m.MathTex("[").move_to((3.2 - i*0.8)*m.UP + 0.8*m.LEFT))
            yb.add(m.MathTex("]").move_to((3.2 - i*0.8)*m.UP + 0.8*m.RIGHT))

        y0 = m.MathTex("y").move_to(3.2*m.UP + 2*m.LEFT)
        yeq = m.MathTex("=").move_to(3.2*m.UP + 1.5*m.LEFT)
        y1 = m.DecimalNumber(0.0256, num_decimal_places = 4).move_to(3.2*m.UP)
        y2 = m.DecimalNumber(0.4491, num_decimal_places = 4).move_to(2.4*m.UP)
        y3 = m.DecimalNumber(0.3109, num_decimal_places = 4).move_to(1.6*m.UP)
        y4 = m.DecimalNumber(0.0078, num_decimal_places = 4).move_to(0.8*m.UP)
        ydots = m.MathTex("\\vdots")
        y5 = m.DecimalNumber(0.6712, num_decimal_places = 4).move_to(0.8*m.DOWN)
        y6 = m.DecimalNumber(0.0506, num_decimal_places = 4).move_to(1.6*m.DOWN)
        y7 = m.DecimalNumber(0.1369, num_decimal_places = 4).move_to(2.4*m.DOWN)
        y8 = m.DecimalNumber(0.5234, num_decimal_places = 4).move_to(3.2*m.DOWN)
        y = m.VGroup(y0, yeq, y1, y2, y3, y4, ydots, y5, y6, y7, y8, yb).shift(2.5*m.LEFT)

        y1tex = m.DecimalNumber(0.7332, num_decimal_places = 4).move_to(y1.get_center())
        y2tex = m.DecimalNumber(0.7330, num_decimal_places = 4).move_to(y2.get_center())
        y3tex = m.DecimalNumber(0.7327, num_decimal_places = 4).move_to(y3.get_center())
        y4tex = m.DecimalNumber(0.7327, num_decimal_places = 4).move_to(y4.get_center())
        ydotstex = m.MathTex("\\vdots").move_to(ydots.get_center())
        y5tex = m.DecimalNumber(0.0011, num_decimal_places = 4).move_to(y5.get_center())
        y6tex = m.DecimalNumber(0.0010, num_decimal_places = 4).move_to(y6.get_center())
        y7tex = m.DecimalNumber(0.0006, num_decimal_places = 4).move_to(y7.get_center())
        y8tex = m.DecimalNumber(0.0006, num_decimal_places = 4).move_to(y8.get_center())

        ytb = m.VGroup()
        ytb.add(m.MathTex("[").move_to(3.2*m.UP + 0.6*m.LEFT))
        ytb.add(m.MathTex("]").move_to(3.2*m.DOWN + 0.6*m.RIGHT))
        for i in range(9):
            ytb.add(m.MathTex("[").move_to((3.2 - i*0.8)*m.UP + 0.4*m.LEFT))
            ytb.add(m.MathTex("]").move_to((3.2 - i*0.8)*m.UP + 0.4*m.RIGHT))

        yt0 = m.MathTex("y_{train}").move_to(3.2*m.UP + 1.9*m.LEFT)
        yteq = m.MathTex("=").move_to(3.2*m.UP + 1.1*m.LEFT)
        yt1 = m.DecimalNumber(0).move_to(3.2*m.UP)
        yt2 = m.DecimalNumber(1).move_to(2.4*m.UP)
        yt3 = m.DecimalNumber(0).move_to(1.6*m.UP)
        yt4 = m.DecimalNumber(0).move_to(0.8*m.UP)
        ytdots = m.MathTex("\\vdots")
        yt5 = m.DecimalNumber(1).move_to(0.8*m.DOWN)
        yt6 = m.DecimalNumber(0).move_to(1.6*m.DOWN)
        yt7 = m.DecimalNumber(0).move_to(2.4*m.DOWN)
        yt8 = m.DecimalNumber(1).move_to(3.2*m.DOWN)
        yt = m.VGroup(yt0, yteq, yt1, yt2, yt3, yt4, ytdots, yt5, yt6, yt7, yt8, ytb).shift(2.5*m.RIGHT)
        yti = m.VGroup(yt1, yt2, yt3, yt4, ytdots, yt5, yt6, yt7, yt8)

        yt1tex = m.DecimalNumber(1).move_to(yt1.get_center())
        yt2tex = m.DecimalNumber(1).move_to(yt2.get_center())
        yt3tex = m.DecimalNumber(1).move_to(yt3.get_center())
        yt4tex = m.DecimalNumber(0).move_to(yt4.get_center())
        ytdotstex = m.MathTex("\\vdots").move_to(ytdots.get_center())
        yt5tex = m.DecimalNumber(0).move_to(yt5.get_center())
        yt6tex = m.DecimalNumber(0).move_to(yt6.get_center())
        yt7tex = m.DecimalNumber(0).move_to(yt7.get_center())
        yt8tex = m.DecimalNumber(0).move_to(yt8.get_center())
        ytitex = m.VGroup(yt1tex, yt2tex, yt3tex, yt4tex, ytdotstex, yt5tex, yt6tex, yt7tex, yt8tex)

        arrow = m.Arrow(
            start = 3.2*m.UP + 1*m.LEFT,
            end = 3.2*m.DOWN + 1*m.LEFT,
            buff = 0.0
        )

        order = m.Tex("descending order").move_to(0.5*m.LEFT).rotate(-np.pi/2)

        arrows = m.VGroup()
        for i in range(9):
            ar = m.Arrow(
                start = (3.2 - i*0.8)*m.UP + 1*m.LEFT,
                end = (3.2 - i*0.8)*m.UP + 0.5*m.LEFT,
                buff = 0.0
            )
            arrows.add(ar)

        tpb = m.VGroup()
        tpb.add(m.MathTex("[").move_to(3.2*m.UP + 1*m.LEFT))
        tpb.add(m.MathTex("]").move_to(3.2*m.DOWN + 1*m.RIGHT))
        for i in range(9):
            tpb.add(m.MathTex("[").move_to((3.2 - i*0.8)*m.UP + 0.8*m.LEFT))
            tpb.add(m.MathTex("]").move_to((3.2 - i*0.8)*m.UP + 0.8*m.RIGHT))

        tp0 = m.MathTex("\\mathrm{TP}").move_to(3.2*m.UP + 2.1*m.LEFT)
        tpeq = m.MathTex("=").move_to(3.2*m.UP + 1.5*m.LEFT)
        tp1 = m.DecimalNumber(1).move_to(3.2*m.UP)
        tp2 = m.DecimalNumber(2).move_to(2.4*m.UP)
        tp3 = m.DecimalNumber(3).move_to(1.6*m.UP)
        tp4 = m.DecimalNumber(3).move_to(0.8*m.UP)
        tpdots = m.MathTex("\\vdots")
        tp5 = m.DecimalNumber(8006).move_to(0.8*m.DOWN)
        tp6 = m.DecimalNumber(8006).move_to(1.6*m.DOWN)
        tp7 = m.DecimalNumber(8006).move_to(2.4*m.DOWN)
        tp8 = m.DecimalNumber(8006).move_to(3.2*m.DOWN)
        tp = m.VGroup(tp0, tpeq, tp1, tp2, tp3, tp4, tpdots, tp5, tp6, tp7, tp8, tpb)

        fpb = m.VGroup()
        fpb.add(m.MathTex("[").move_to(3.2*m.UP + 1*m.LEFT))
        fpb.add(m.MathTex("]").move_to(3.2*m.DOWN + 1*m.RIGHT))
        for i in range(9):
            fpb.add(m.MathTex("[").move_to((3.2 - i*0.8)*m.UP + 0.8*m.LEFT))
            fpb.add(m.MathTex("]").move_to((3.2 - i*0.8)*m.UP + 0.8*m.RIGHT))

        fp0 = m.MathTex("\\mathrm{FP}").move_to(3.2*m.UP + 2.1*m.LEFT)
        fpeq = m.MathTex("=").move_to(3.2*m.UP + 1.5*m.LEFT)
        fp1 = m.DecimalNumber(0).move_to(3.2*m.UP)
        fp2 = m.DecimalNumber(0).move_to(2.4*m.UP)
        fp3 = m.DecimalNumber(0).move_to(1.6*m.UP)
        fp4 = m.DecimalNumber(1).move_to(0.8*m.UP)
        fpdots = m.MathTex("\\vdots")
        fp5 = m.DecimalNumber(111991).move_to(0.8*m.DOWN)
        fp6 = m.DecimalNumber(111992).move_to(1.6*m.DOWN)
        fp7 = m.DecimalNumber(111993).move_to(2.4*m.DOWN)
        fp8 = m.DecimalNumber(111994).move_to(3.2*m.DOWN)
        fp = m.VGroup(fp0, fpeq, fp1, fp2, fp3, fp4, fpdots, fp5, fp6, fp7, fp8, fpb).shift(4.5*m.RIGHT)

        truep = m.Tex("true positive").scale(0.8).move_to(tp0.get_center() + 0.5*m.UP)
        falsep = m.Tex("false positive").scale(0.8).move_to(fp0.get_center() + 0.5*m.UP)

        tp1tex = m.DecimalNumber(0.0001, num_decimal_places = 4).move_to(tp1.get_center())
        tp2tex = m.DecimalNumber(0.0002, num_decimal_places = 4).move_to(tp2.get_center())
        tp3tex = m.DecimalNumber(0.0004, num_decimal_places = 4).move_to(tp3.get_center())
        tp4tex = m.DecimalNumber(0.0004, num_decimal_places = 4).move_to(tp4.get_center())
        tpdotstex = m.MathTex("\\vdots").move_to(tpdots.get_center())
        tp5tex = m.DecimalNumber(1.0000, num_decimal_places = 4).move_to(tp5.get_center())
        tp6tex = m.DecimalNumber(1.0000, num_decimal_places = 4).move_to(tp6.get_center())
        tp7tex = m.DecimalNumber(1.0000, num_decimal_places = 4).move_to(tp7.get_center())
        tp8tex = m.DecimalNumber(1.0000, num_decimal_places = 4).move_to(tp8.get_center())

        fp1tex = m.DecimalNumber(0.0000, num_decimal_places = 4).move_to(fp1.get_center())
        fp2tex = m.DecimalNumber(0.0000, num_decimal_places = 4).move_to(fp2.get_center())
        fp3tex = m.DecimalNumber(0.0000, num_decimal_places = 4).move_to(fp3.get_center())
        fp4tex = m.DecimalNumber(0.0000, num_decimal_places = 4).move_to(fp4.get_center())
        fpdotstex = m.MathTex("\\vdots").move_to(fpdots.get_center())
        fp5tex = m.DecimalNumber(1.0000, num_decimal_places = 4).move_to(fp5.get_center())
        fp6tex = m.DecimalNumber(1.0000, num_decimal_places = 4).move_to(fp6.get_center())
        fp7tex = m.DecimalNumber(1.0000, num_decimal_places = 4).move_to(fp7.get_center())
        fp8tex = m.DecimalNumber(1.0000, num_decimal_places = 4).move_to(fp8.get_center())

        ax = m.Axes(
            x_range = [0, 1, 1],
            y_range = [0, 1, 1],
            x_length = 6, 
            y_length = 6,
            tips = False,
            axis_config = {"include_numbers": True}
        ).shift(3.5*m.LEFT)

        xlab = m.MathTex("\\mathrm{FP}").move_to(3.4*m.DOWN + 3.5*m.LEFT)
        ylab = m.MathTex("\\mathrm{TP}").move_to(6.9*m.LEFT).rotate(np.pi/2)

        axlab = m.VGroup(ax, xlab, ylab)

        dx = 2.4/1000

        curve = ax.plot(
            lambda x: np.sqrt(1 - (x - 1)**2),
            x_range = (0, 1, dx),
            stroke_width = 10.0,
            color = c,
            use_smoothing = False
        )

        area = ax.get_area(
            curve,
            x_range = (0, 1),
            color = c,
            opacity = 0.1
        )

        roc_auc = m.Tex("ROC AUC").move_to(0.4*m.DOWN + 3.1*m.LEFT)
        roc_def = m.Tex("Receiver Operating Characteristic").scale(0.8).move_to(roc_auc.get_center() + 0.5*m.DOWN)
        auc_def = m.Tex("Area Under the Curve").scale(0.8).move_to(roc_auc.get_center() + 0.9*m.DOWN)

        perfect_curve = ax.plot(
            lambda x: 1,
            x_range = (0, 1, dx),
            stroke_width = 10.0,
            color = c,
            use_smoothing = False
        )

        perfect_area = ax.get_area(
            perfect_curve,
            x_range = (0, 1),
            color = c,
            opacity = 0.1
        )

        perfect_auc = m.MathTex("\\mathrm{AUC} = 1.0").move_to(3.5*m.LEFT)

        perfect_classifier = m.Tex("perfect classifier").move_to(3.5*m.UP + 3.5*m.LEFT)

        random_curve = ax.plot(
            lambda x: x,
            x_range = (0, 1, dx),
            stroke_width = 10.0,
            color = c,
            use_smoothing = False
        )

        random_area = ax.get_area(
            random_curve,
            x_range = (0, 1),
            color = c,
            opacity = 0.1
        )

        random_auc = m.MathTex("\\mathrm{AUC} = 0.5").move_to(1.3*m.DOWN + 2.2*m.LEFT)

        random_guessing = m.Tex("random guessing").move_to(3.5*m.UP + 3.5*m.LEFT)

        self.play(
            m.Create(y),
            m.Create(yt)
        )
        self.wait()
        self.play(
            m.GrowArrow(arrow),
            m.Create(order)
        )
        self.play(
            m.Transform(y1, y1tex),
            m.Transform(y2, y2tex),
            m.Transform(y3, y3tex),
            m.Transform(y4, y4tex),
            m.Transform(ydots, ydotstex),
            m.Transform(y5, y5tex),
            m.Transform(y6, y6tex),
            m.Transform(y7, y7tex),
            m.Transform(y8, y8tex)
        )
        self.play(
            m.FadeOut(arrow, order)
        )
        self.play(
            m.GrowArrow(arrows[0]),
            m.Transform(yti[0], ytitex[0]),
            run_time = 0.5
        )
        for i in range(1, 9):
            self.play(
                m.FadeOut(arrows[i - 1]),
                run_time = 0.5
            )
            self.play(
                m.GrowArrow(arrows[i]),
                m.Transform(yti[i], ytitex[i]),
                run_time = 0.5
            )
        self.play(
            m.FadeOut(arrows[8])
        )
        self.play(
            m.FadeOut(y),
            yt.animate.move_to(5*m.LEFT)
        )
        self.wait()
        self.play(
            m.Create(tp),
            m.Create(fp)
        )
        self.play(
            m.FadeIn(truep, falsep)
        )
        self.play(
            m.FadeOut(truep, falsep)
        )
        self.play(
            m.Transform(tp1, tp1tex),
            m.Transform(tp2, tp2tex),
            m.Transform(tp3, tp3tex),
            m.Transform(tp4, tp4tex),
            m.Transform(tpdots, tpdotstex),
            m.Transform(tp5, tp5tex),
            m.Transform(tp6, tp6tex),
            m.Transform(tp7, tp7tex),
            m.Transform(tp8, tp8tex),
            m.Transform(fp1, fp1tex),
            m.Transform(fp2, fp2tex),
            m.Transform(fp3, fp3tex),
            m.Transform(fp4, fp4tex),
            m.Transform(fpdots, fpdotstex),
            m.Transform(fp5, fp5tex),
            m.Transform(fp6, fp6tex),
            m.Transform(fp7, fp7tex),
            m.Transform(fp8, fp8tex)
        )
        self.wait()
        self.play(
            m.FadeOut(yt),
            tp.animate.shift(2.3*m.RIGHT),
            fp.animate.shift(1.5*m.RIGHT)
        )
        self.wait()
        self.play(
            m.Create(axlab)
        )
        self.play(
            m.Create(curve)
        )
        self.play(
            m.FadeIn(area)
        )
        self.play(
            m.FadeIn(roc_auc, roc_def, auc_def)
        )
        self.wait()
        self.play(
            m.FadeOut(curve, area, roc_auc, roc_def, auc_def),
            m.Create(perfect_curve)
        )
        self.play(
            m.FadeIn(perfect_area)
        )
        self.play(
            m.FadeIn(perfect_auc, perfect_classifier)
        )
        self.wait()
        self.play(
            m.FadeOut(perfect_curve, perfect_area, perfect_auc, perfect_classifier),
            m.Create(random_curve)
        )
        self.play(
            m.FadeIn(random_area)
        )
        self.play(
            m.FadeIn(random_auc, random_guessing)
        )
        self.wait()
        self.play(
            m.FadeOut(random_curve, random_area, random_auc, random_guessing)
        )
        self.play(
            m.FadeIn(curve, area, roc_auc)
        )
        self.wait()
# ---------------------------------------------------------------------------
class Cell21(m.Scene):
    def construct(self):

        Xb = m.VGroup()
        Xb.add(m.MathTex("[").move_to(3.2*m.UP + 4.6*m.LEFT))
        for i in range(9):
            Xb.add(m.MathTex("[").move_to((3.2 - i*0.8)*m.UP + 4.4*m.LEFT))
            Xb.add(m.MathTex("]").move_to((3.2 - i*0.8)*m.UP + 4.4*m.RIGHT))
        Xb.add(m.MathTex("]").move_to(3.2*m.DOWN + 4.6*m.RIGHT))
        
        xij = m.VGroup()
        for i in range(8):
            for j in range(8):
                xij.add(m.MathTex(f"x_{{{i + 1}{j + 1}}}").move_to((3.2 - i*0.8)*m.UP + (4.0 - j*1.0)*m.LEFT))
            xij.add(m.MathTex("\\dots").move_to((3.2 - i*0.8)*m.UP + (4.0 - 8*1.0)*m.LEFT))
        for j in range(8):
            xij.add(m.MathTex("\\vdots").move_to((3.2 - 8*0.8)*m.UP + (4.0 - j*1.0)*m.LEFT))
        xij.add(m.MathTex("\\ddots").move_to((3.2 - 8*0.8)*m.UP + (4.0 - 8*1.0)*m.LEFT))

        Xtrain = m.MathTex("X_{train}").move_to(3.2*m.UP + 5.7*m.LEFT)
        Xeq = m.MathTex("=").move_to(3.2*m.UP + 4.9*m.LEFT)
        X = m.VGroup(Xtrain, Xeq, Xb, xij)

        X1 = m.VGroup(xij[0:9])
        X2 = m.VGroup(xij[9:18])
        X3 = m.VGroup(xij[18:27])
        X4 = m.VGroup(xij[27:36])
        X5 = m.VGroup(xij[36:45])
        X6 = m.VGroup(xij[45:54])
        X7 = m.VGroup(xij[54:63])
        X8 = m.VGroup(xij[63:72])
        X9 = m.VGroup(xij[72:81])
        Xi = m.VGroup(X1, X2, X3, X4, X5, X6, X7, X8, X9)
        X1tex = m.MathTex("X_1").move_to(3.2*m.UP + 3.8*m.LEFT)
        X2tex = m.MathTex("X_2").move_to(2.4*m.UP + 3.8*m.LEFT)
        X3tex = m.MathTex("X_3").move_to(1.6*m.UP + 3.8*m.LEFT)
        X4tex = m.MathTex("X_4").move_to(0.8*m.UP + 3.8*m.LEFT)
        X5tex = m.MathTex("X_5").move_to(3.8*m.LEFT)
        X6tex = m.MathTex("X_6").move_to(0.8*m.DOWN + 3.8*m.LEFT)
        X7tex = m.MathTex("X_7").move_to(1.6*m.DOWN + 3.8*m.LEFT)
        X8tex = m.MathTex("X_8").move_to(2.4*m.DOWN + 3.8*m.LEFT)
        X9tex = m.MathTex("\\vdots").move_to(3.2*m.DOWN + 3.8*m.LEFT)

        yb = m.VGroup()
        yb.add(m.MathTex("[").move_to(3.2*m.UP + 0.4*m.LEFT))
        for i in range(9):
            yb.add(m.MathTex("[").move_to((3.2 - i*0.8)*m.UP + 0.2*m.LEFT))
            yb.add(m.MathTex("]").move_to((3.2 - i*0.8)*m.UP + 1*m.RIGHT))
        yb.add(m.MathTex("]").move_to(3.2*m.DOWN + 1.2*m.RIGHT))
        
        yi = m.VGroup()
        for i in range(8):
            yi.add(m.MathTex(f"y_{{{i + 1}}}").move_to((3.2 - i*0.8)*m.UP + 0.4*m.RIGHT))
        yi.add(m.MathTex("\\vdots").move_to((3.2 - 8*0.8)*m.UP + 0.4*m.RIGHT))

        ytrain = m.MathTex("y_{train}").move_to(3.2*m.UP + 1.5*m.LEFT)
        yeq = m.MathTex("=").move_to(3.2*m.UP + 0.7*m.LEFT)
        y = m.VGroup(ytrain, yeq, yb, yi)

        wb = m.VGroup()
        wb.add(m.MathTex("[").move_to(3.2*m.UP + 3.8*m.RIGHT))
        for i in range(9):
            wb.add(m.MathTex("[").move_to((3.2 - i*0.8)*m.UP + 4*m.RIGHT))
            wb.add(m.MathTex("]").move_to((3.2 - i*0.8)*m.UP + 5.2*m.RIGHT))
        wb.add(m.MathTex("]").move_to(3.2*m.DOWN + 5.4*m.RIGHT))
        
        wi = m.VGroup()
        for i in range(8):
            wi.add(m.MathTex(f"w_{{{i + 1}}}").move_to((3.2 - i*0.8)*m.UP + 4.6*m.RIGHT))
        wi.add(m.MathTex("\\vdots").move_to((3.2 - 8*0.8)*m.UP + 4.6*m.RIGHT))

        wsample = m.MathTex("w_{sample}").move_to(3.2*m.UP + 2.5*m.RIGHT)
        weq = m.MathTex("=").move_to(3.2*m.UP + 3.5*m.RIGHT)
        w = m.VGroup(wsample, weq, wb, wi)

        sw = 10
        m.ArcBetweenPoints.set_default(
            color = c,
            stroke_width = sw
        )

        rad = 4
        h = rad - np.sin(np.pi/4)*rad
        d = np.cos(np.pi/4)*rad

        arcUL = m.ArcBetweenPoints(
            start = d*m.LEFT + h*m.UP,
            end = m.ORIGIN,
            radius = -rad
        )
        arcUR = m.ArcBetweenPoints(
            start = m.ORIGIN,
            end = d*m.RIGHT + h*m.UP,
            radius = -rad
        )
        arcDL = m.ArcBetweenPoints(
            start = d*m.LEFT + h*m.DOWN,
            end = m.ORIGIN,
            radius = rad
        )
        arcDR = m.ArcBetweenPoints(
            start = m.ORIGIN,
            end = d*m.RIGHT + h*m.DOWN,
            radius = rad
        )
        atU = m.Triangle(
            color = c,
            fill_opacity = 1.0
        ).rotate(np.pi/6).scale(0.5).move_to(d*m.RIGHT + h*m.UP)
        atD = m.Triangle(
            color = c,
            fill_opacity = 1.0
        ).rotate(np.pi/6).scale(0.5).move_to(d*m.RIGHT + h*m.DOWN)

        perm = m.VGroup(arcUL, arcUR, arcDL, arcDR, atU, atD)

        Xitex = m.VGroup()
        yitex = m.VGroup()
        witex = m.VGroup()
        newi = [93, 692, 100, 562, 729, 924, 393, 685]
        for i in range(8):
            Xitex.add(m.MathTex(f"X_{{{newi[i]}}}").move_to(Xi[i].get_center() + 3.8*m.LEFT))
            yitex.add(m.MathTex(f"y_{{{newi[i]}}}").move_to(yi[i].get_center()))
            witex.add(m.MathTex(f"w_{{{newi[i]}}}").move_to(wi[i].get_center()))
        
        xo = Xitex[0].copy()
        y93 = yitex[0].copy()
        w93 = witex[0].copy()
        yo = m.VGroup(y93, w93)

        ieq = m.MathTex("i =").move_to(3.5*m.UP + 0.2*m.LEFT)
        n93 = m.DecimalNumber(93).move_to(3.5*m.UP + 0.5*m.RIGHT)
        n692 = m.DecimalNumber(692).move_to(3*m.UP + 0.5*m.RIGHT).set_opacity(0.0)
        idots = m.MathTex("\\dots").move_to(3*m.UP + 0.5*m.RIGHT).set_opacity(0.0)
        i93 = m.VGroup(ieq, n93)
        
        x1 = m.MathTex("x_1").move_to(3.5*m.UP + 5.5*m.LEFT)
        x2 = m.MathTex("x_2").move_to(2.8*m.UP + 5.5*m.LEFT)
        x3 = m.MathTex("x_3").move_to(2.1*m.UP + 5.5*m.LEFT)
        x4 = m.MathTex("x_4").move_to(1.4*m.UP + 5.5*m.LEFT)
        x5 = m.MathTex("x_5").move_to(0.7*m.UP + 5.5*m.LEFT)
        x6 = m.MathTex("x_6").move_to(5.5*m.LEFT)
        x7 = m.MathTex("x_7").move_to(0.7*m.DOWN + 5.5*m.LEFT)
        x8 = m.MathTex("x_8").move_to(1.4*m.DOWN + 5.5*m.LEFT)
        x9 = m.MathTex("x_9").move_to(2.1*m.DOWN + 5.5*m.LEFT)
        x10 = m.MathTex("x_{10}").move_to(2.8*m.DOWN + 5.5*m.LEFT)
        x11 = m.MathTex("x_{11}").move_to(3.5*m.DOWN + 5.5*m.LEFT)
        x = m.VGroup(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11)

        ydel = m.MathTex("y").move_to(5.5*m.RIGHT)

        counter = 0
        edges = []
        partitions = []
        layers = [11, 8, 8, 8, 1]

        for i in layers:
            partitions.append(list(range(counter + 1, counter + i + 1)))
            counter += i
        for i, v in enumerate(layers[1:]):
                last = sum(layers[:i + 1])
                for j in range(v):
                    for k in range(last - layers[i], last):
                        edges.append((k + 1, j + last + 1))

        vertices = np.arange(1, sum(layers) + 1)

        dx = 2
        layout = {}
        for part in partitions:
            for node_index, node in enumerate(part):
                if node in range(1, 12):
                    layout[node] = [-2*dx, 3.5 - 0.7*node_index, 0]
                elif node in range(12, 20):
                    layout[node] = [-dx, 2.45 - 0.7*node_index, 0]
                elif node in range(20, 28):
                    layout[node] = [0, 2.45 - 0.7*node_index, 0]
                elif node in range(28, 36):
                    layout[node] = [dx, 2.45 - 0.7*node_index, 0]
                else:
                    layout[node] = [2*dx, 0, 0]

        network = m.Graph(
            vertices,
            edges,
            layout = layout,
            vertex_config = {"color": c},
            edge_config = {"color": c, "stroke_width": 1.0}
        ).shift(0.2*m.RIGHT)

        age = m.Tex("Age").scale(0.8).move_to(layout[1] + 1.5*m.LEFT)
        income = m.Tex("Monthly Income").scale(0.8).move_to(layout[2] + 1.5*m.LEFT)
        ratio = m.Tex("Debt Ratio").scale(0.8).move_to(layout[3] + 1.5*m.LEFT)
        debt = m.Tex("Total Debt").scale(0.8).move_to(layout[4] + 1.5*m.LEFT)
        unsecure = m.Tex("Unsecured Lines").scale(0.8).move_to(layout[5] + 1.5*m.LEFT)
        credit = m.Tex("Credit Card Loans").scale(0.8).move_to(layout[6] + 1.5*m.LEFT)
        estate = m.Tex("Real Estate Loans").scale(0.8).move_to(layout[7] + 1.5*m.LEFT)
        dependents = m.Tex("Dependents").scale(0.8).move_to(layout[8] + 1.5*m.LEFT)
        late3059 = m.Tex("30-59 Days Late").scale(0.8).move_to(layout[9] + 1.5*m.LEFT)
        late6089 = m.Tex("60-59 Days Late").scale(0.8).move_to(layout[10] + 1.5*m.LEFT)
        late90 = m.Tex("90 Days Late").scale(0.8).move_to(layout[11] + 1.5*m.LEFT)
        params = m.VGroup(age, income, ratio, debt, unsecure, credit,
                          estate, dependents, late3059, late6089, late90)
        delinquency = m.Tex("Delinquency").scale(0.8).move_to(layout[36] + 1.5*m.RIGHT)

        r1 = m.RoundedRectangle(
            width = 2.9,
            height = 0.5,
            corner_radius = 0.1,
            color = m.BLUE
        ).move_to(layout[1] + 1.5*m.LEFT)
        r2 = r1.copy().move_to(layout[2] + 1.5*m.LEFT)
        r3 = r1.copy().move_to(layout[3] + 1.5*m.LEFT)
        r4 = r1.copy().move_to(layout[4] + 1.5*m.LEFT)
        r5 = r1.copy().move_to(layout[5] + 1.5*m.LEFT)
        r6 = r1.copy().move_to(layout[6] + 1.5*m.LEFT)
        r7 = r1.copy().move_to(layout[7] + 1.5*m.LEFT)
        r8 = r1.copy().move_to(layout[8] + 1.5*m.LEFT)
        r9 = r1.copy().move_to(layout[9] + 1.5*m.LEFT)
        r10 = r1.copy().move_to(layout[10] + 1.5*m.LEFT)
        r11 = r1.copy().move_to(layout[11] + 1.5*m.LEFT)
        rect = m.VGroup(r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11)
        r12 = m.RoundedRectangle(
            width = 2.2,
            height = 0.5,
            corner_radius = 0.1,
            color = m.RED
        ).move_to(layout[36] + 1.5*m.RIGHT)

        rectangles = m.VGroup(r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12)

        def bg():
            cols = []
            for i in range(11):
                val = np.random.uniform(0.0, 1.0)
                if val <= 0.5:
                    op = 2*val
                    col = m.interpolate_color(m.RED, m.YELLOW, op)
                else:
                    op = 2*(val - 0.5)
                    col = m.interpolate_color(m.YELLOW, m.GREEN, op)
                cols.append(col)
            res = np.random.randint(2)
            if res == 0:
                col = m.RED
            else:
                col = m.GREEN
            cols.append(col)
            return cols
        
        cols = bg()
        cols0 = cols
        d1 = m.VGroup()
        dd1 = m.VGroup()
        for i in range(11):
            d1.add(network.vertices[i + 1].copy().scale(2).set_color(cols[i]))
            dd1.add(m.VGroup())
        for i in range(8):
            for j in range(11):
                dd1[j].add(d1[j].copy())

        cols = bg()
        d2 = m.VGroup()
        dd2 = m.VGroup()
        for i in range(8):
            d2.add(network.vertices[i + 12].copy().scale(2).set_color(cols[i]))
            dd2.add(m.VGroup())
        for i in range(8):
            for j in range(8):
                dd2[j].add(d2[j].copy())

        cols = bg()
        d3 = m.VGroup()
        dd3 = m.VGroup()
        for i in range(8):
            d3.add(network.vertices[i + 20].copy().scale(2).set_color(cols[i]))
            dd3.add(m.VGroup())
        for i in range(8):
            for j in range(8):
                dd3[j].add(d3[j].copy())
        
        cols = bg()
        d4 = m.VGroup()
        for i in range(8):
            d4.add(network.vertices[i + 28].copy().scale(2).set_color(cols[i]))
        
        cols = bg()
        d5 = network.vertices[36].copy().scale(2).set_color(cols[0])

        circ = r12.copy().set_color(cols0[-1])
        circgoal = m.Circle(
            radius = 0.8,
            color = cols0[-1],
            stroke_width = 5
        ).move_to(circ.get_center())

        s0 = [0 for j in range(36)]
        sU = [0.02*(5 - j) for j in range(11)]
        sD = [0.02*(j - 5) for j in range(11)]
        s = s0 + sU + sD + s0

        cols = bg()
        cols1 = cols
        d6 = m.VGroup()
        dd6 = m.VGroup()
        for i in range(11):
            d6.add(network.vertices[i + 1].copy().scale(2).set_color(cols[i]))
            dd6.add(m.VGroup())
        for i in range(8):
            for j in range(11):
                dd6[j].add(d6[j].copy())
        
        cols = bg()
        d7 = m.VGroup()
        dd7 = m.VGroup()
        for i in range(8):
            d7.add(network.vertices[i + 12].copy().scale(2).set_color(cols[i]))
            dd7.add(m.VGroup())
        for i in range(8):
            for j in range(8):
                dd7[j].add(d7[j].copy())
        
        cols = bg()
        d8 = m.VGroup()
        dd8 = m.VGroup()
        for i in range(8):
            d8.add(network.vertices[i + 20].copy().scale(2).set_color(cols[i]))
            dd8.add(m.VGroup())
        for i in range(8):
            for j in range(8):
                dd8[j].add(d8[j].copy())
        
        cols = bg()
        d9 = m.VGroup()
        for i in range(8):
            d9.add(network.vertices[i + 28].copy().scale(2).set_color(cols[i]))
        
        cols = bg()
        d10 = network.vertices[36].copy().scale(2).set_color(cols[0])

        circ2 = r12.copy().set_color(cols1[-1])
        circ2goal = m.Circle(
            radius = 0.8,
            color = cols1[-1],
            stroke_width = 5
        ).move_to(circ2.get_center())

        ax = m.Axes(
            x_range = [0, 100, 20],
            y_range = [0, 1, 0.2],
            tips = False,
            axis_config = {"include_numbers": True}
        ).shift(0.1*m.RIGHT)

        xlab = m.Tex("epoch").move_to(3.5*m.DOWN + 0.1*m.RIGHT)
        ylab = m.Tex("ROC AUC").move_to(6.9*m.LEFT).rotate(np.pi/2)

        curve = ax.plot(
            lambda x: 0.87*(1 - np.exp(-0.1*x)),
            x_range = (0, 100, 1),
            stroke_width = 10.0,
            color = c
        )

        axlableg = m.VGroup(ax, xlab, ylab)

        winning = m.Tex("competition winning accuracy: 86.96\\%")
        best = m.Tex("best achieved accuracy: 86.71\\%").align_to(winning, m.RIGHT).shift(1*m.DOWN)
        bracket = m.Tex("\\}").scale(3).move_to(0.5*m.DOWN + 4*m.RIGHT)
        err = m.Tex("0.29\\%").move_to(0.5*m.DOWN + 5*m.RIGHT)

        self.play(
            m.Create(X)
        )
        self.wait()
        self.play(
            m.Transform(X1, X1tex),
            m.Transform(X2, X2tex),
            m.Transform(X3, X3tex),
            m.Transform(X4, X4tex),
            m.Transform(X5, X5tex),
            m.Transform(X6, X6tex),
            m.Transform(X7, X7tex),
            m.Transform(X8, X8tex),
            m.Transform(X9, X9tex),
            Xb[2].animate.move_to(3.2*m.UP + 3.2*m.LEFT),
            Xb[4].animate.move_to(2.4*m.UP + 3.2*m.LEFT),
            Xb[6].animate.move_to(1.6*m.UP + 3.2*m.LEFT),
            Xb[8].animate.move_to(0.8*m.UP + 3.2*m.LEFT),
            Xb[10].animate.move_to(3.2*m.LEFT),
            Xb[12].animate.move_to(0.8*m.DOWN + 3.2*m.LEFT),
            Xb[14].animate.move_to(1.6*m.DOWN + 3.2*m.LEFT),
            Xb[16].animate.move_to(2.4*m.DOWN + 3.2*m.LEFT),
            Xb[18].animate.move_to(3.2*m.DOWN + 3.2*m.LEFT),
            Xb[19].animate.move_to(3.2*m.DOWN + 3*m.LEFT)
        )
        self.play(
            m.Create(y)
        )
        self.play(
            m.Create(w)
        )
        self.wait()
        self.play(
            m.FadeIn(perm, rate_func = m.rate_functions.there_and_back),
            m.Transform(Xtrain, m.MathTex("X_{shuf}").move_to(Xtrain.get_center())),
            m.Transform(ytrain, m.MathTex("y_{shuf}").move_to(ytrain.get_center())),
            m.Transform(wsample, m.MathTex("w_{shuf}").move_to(wsample.get_center() + 0.2*m.RIGHT)),
            [m.Transform(Xi[i], Xitex[i]) for i in range(8)],
            [m.Transform(yi[i], yitex[i]) for i in range(8)],
            [m.Transform(wi[i], witex[i]) for i in range(8)]
        )
        self.wait()
        self.add(xo, y93, w93)
        self.play(
            m.FadeOut(perm, X, y, w)
        )
        self.play(
            m.Transform(xo, x),
            m.Transform(yo, ydel),
            m.Create(i93)
        )
        self.play(
            m.FadeIn(network, rect, r12)
        )
        self.play(
            m.Transform(xo, params),
            m.Transform(yo, delinquency)
        )
        self.play(
            [rectangles[i].animate.set_color(cols0[i]) for i in range(12)],
            m.FadeIn(d1)
        )
        self.wait()
        self.add(dd1)
        self.remove(d1)
        for j in range(8):
            self.play(
                [dd1[i][j].animate.move_to(network.vertices[j + 12]) for i in range(11)],
                m.FadeIn(d2[j]),
                run_time = 1 - 0.1*j
            )
        self.add(dd2)
        self.remove(dd1, *d2)
        for j in range(8):
            self.play(
                [dd2[i][j].animate.move_to(network.vertices[j + 20]) for i in range(8)],
                m.FadeIn(d3[j]),
                run_time = 1 - 0.1*j
            )
        self.add(dd3)
        self.remove(dd2, *d3)
        for j in range(8):
            self.play(
                [dd3[i][j].animate.move_to(network.vertices[j + 28]) for i in range(8)],
                m.FadeIn(d4[j]),
                run_time = 1 - 0.1*j
            )
        self.remove(dd3)
        self.play(
            [d4[i].animate.move_to(network.vertices[36]) for i in range(8)],
            m.FadeIn(d5)
        )
        self.add(circ)
        self.remove(r12, *d4)
        self.play(
            m.Transform(circ, circgoal),
            d5.animate.scale(4).move_to(circ.get_center()),
            yo.animate.shift(1.2*m.DOWN)
        )
        for i in range(58):
            self.play(
                [network.vertices[j + 1].animate.shift(s[i + j + 1]*m.LEFT) for j in range(36)],
                rate_func = m.rate_functions.linear,
                run_time = 0.01
            )
        self.play(
            m.FadeOut(d5),
            m.Transform(circ, r12),
            yo.animate.shift(1.2*m.UP)
        )
        self.wait()
        self.add(r12, n692)
        self.remove(circ)
        self.play(
            n93.animate.shift(0.5*m.UP).set_opacity(0.0),
            n692.animate.shift(0.5*m.UP).set_opacity(1.0)
        )
        self.play(
            [rectangles[i].animate.set_color(cols1[i]) for i in range(12)],
            m.FadeIn(d6)
        )
        self.wait()
        self.add(dd6)
        self.remove(d6)
        self.play(
            [dd6[i][j].animate.move_to(network.vertices[j + 12]) for i in range(11) for j in range(8)],
            m.FadeIn(d7)
        )
        self.add(dd7)
        self.remove(dd6, d7)
        self.play(
            [dd7[i][j].animate.move_to(network.vertices[j + 20]) for i in range(8) for j in range(8)],
            m.FadeIn(d8)
        )
        self.add(dd8)
        self.remove(dd7, d8)
        self.play(
            [dd8[i][j].animate.move_to(network.vertices[j + 28]) for i in range(8) for j in range(8)],
            m.FadeIn(d9)
        )
        self.remove(dd8)
        self.play(
            [d9[i].animate.move_to(network.vertices[36]) for i in range(8)],
            m.FadeIn(d10)
        )
        self.add(circ2)
        self.remove(r12, d9)
        self.play(
            m.Transform(circ2, circ2goal),
            d10.animate.scale(4).move_to(circ2.get_center()),
            yo.animate.shift(1.2*m.DOWN)
        )
        for i in range(58):
            self.play(
                [network.vertices[j + 1].animate.shift(s[i + j + 1]*m.LEFT) for j in range(36)],
                rate_func = m.rate_functions.linear,
                run_time = 0.01
            )
        self.play(
            m.FadeOut(d10),
            m.Transform(circ2, r12),
            yo.animate.shift(1.2*m.UP)
        )
        self.wait()
        self.add(r12, idots)
        self.remove(circ2)
        self.play(
            n692.animate.shift(0.5*m.UP).set_opacity(0.0),
            idots.animate.shift(0.5*m.UP).set_opacity(1.0)
        )
        self.play(
            [rectangles[i].animate.set_color(m.BLUE) for i in range(11)],
            rectangles[11].animate.set_color(m.RED)
        )
        self.play(
            m.FadeOut(network, rectangles, xo, yo, ieq, n93, n692, idots)
        )
        self.play(
            m.Create(axlableg)
        )
        self.play(
            m.Create(curve),
            rate_func = m.rate_functions.linear,
            run_time = 3
        )
        self.wait()
        self.play(
            m.FadeIn(winning)
        )
        self.wait()
        self.play(
            m.FadeIn(best)
        )
        self.wait()
        self.play(
            m.FadeIn(bracket, err)
        )
        self.wait()