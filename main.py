import math
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import StringProperty, NumericProperty, ListProperty
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.lang import Builder
# ✅ NEW: Import LabelBase for font registration
from kivy.core.text import LabelBase

# تنظیم سایز پنجره
Window.size = (520, 750)

# ✅ NEW: Register the Persian font globally
# The font file 'Vazirmatn-Regular.ttf' must be placed in the same directory as this script.
LabelBase.register(
    name='Vazirmatn',
    fn_regular='Vazirmatn-Regular.ttf'
)

# =========================
# ✅ NEW: Global KV rules to apply Vazirmatn to ALL text widgets
# These rules ensure every Label, Button, and TextInput in the app uses the Persian font.
# =========================
Builder.load_string("""
<Label>:
    font_name: 'Vazirmatn'

<Button>:
    font_name: 'Vazirmatn'

<TextInput>:
    font_name: 'Vazirmatn'

<CustomTextInput>:
    font_size: 14
    size_hint_y: None
    height: 40
    padding: [10, 10]
    multiline: False
    background_color: 0.2, 0.23, 0.29, 1
    foreground_color: 1, 1, 1, 1
    cursor_color: 1, 1, 0, 1
    on_focus: app.set_active_entry(self) if self.focus else None

<BaseScreen>:
    canvas.before:
        Color:
            rgba: self.bg_color
        Rectangle:
            pos: self.pos
            size: self.size

<GeometryScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 10
        spacing: 10
        Label:
            id: title
            font_size: 20
            bold: True
            size_hint_y: None
            height: 40
            color: 1, 1, 1, 1
        GridLayout:
            cols: 2
            size_hint_y: None
            height: 100
            spacing: 5
            Label:
                id: label_n
                text: 'n or height:'
                color: 1, 1, 1, 1
            CustomTextInput:
                id: n_entry
            Label:
                id: label_val
                text: 'value:'
                color: 1, 1, 1, 1
            CustomTextInput:
                id: val_entry
        GridLayout:
            cols: 2
            spacing: 5
            Button:
                id: btn_diagonals
                text: 'Diagonals'
                on_press: root.diagonals()
            Button:
                id: btn_angles
                text: 'Angles'
                on_press: root.angles()
            Button:
                id: btn_perimeter
                text: 'Perimeter'
                on_press: root.perimeter()
            Button:
                id: btn_area
                text: 'Triangle Area'
                on_press: root.area()
            Button:
                id: btn_volume
                text: 'Sphere Volume'
                on_press: root.volume()
            Button:
                id: btn_lateral
                text: 'Cylinder Lateral'
                on_press: root.lateral()
            Button:
                id: btn_circle_area
                text: 'Circle Area'
                on_press: root.circle_area()
            Button:
                id: btn_circumference
                text: 'Circumference'
                on_press: root.circle_perimeter()

<VectorsScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 10
        spacing: 10
        Label:
            id: title
            font_size: 20
            bold: True
            size_hint_y: None
            height: 40
            color: 1, 1, 1, 1
        GridLayout:
            cols: 2
            size_hint_y: None
            height: 100
            spacing: 5
            Label:
                id: label_v1
                text: 'Vector 1'
                color: 1, 1, 1, 1
            CustomTextInput:
                id: v1
            Label:
                id: label_v2
                text: 'Vector 2'
                color: 1, 1, 1, 1
            CustomTextInput:
                id: v2
        GridLayout:
            cols: 2
            spacing: 5
            Button:
                id: btn_add
                text: 'Add'
                on_press: root.add_vectors()
            Button:
                id: btn_distance
                text: 'Distance'
                on_press: root.distance_vectors()
            Button:
                id: btn_dot
                text: 'Dot Product'
                on_press: root.dot_product()
            Button:
                id: btn_length
                text: 'Length'
                on_press: root.vector_length()

<ProportionScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 10
        spacing: 10
        Label:
            id: title
            font_size: 20
            bold: True
            size_hint_y: None
            height: 40
            color: 1, 1, 1, 1
        GridLayout:
            cols: 2
            size_hint_y: None
            height: 50
            spacing: 5
            Label:
                id: label_input
                text: 'Input'
                color: 1, 1, 1, 1
            CustomTextInput:
                id: prop_entry
        GridLayout:
            cols: 2
            spacing: 5
            Button:
                id: btn_table
                text: 'Table'
                on_press: root.table()
            Button:
                id: btn_percent
                text: 'Percent'
                on_press: root.percent_p()

<AlgebraScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 10
        spacing: 10
        Label:
            id: title
            font_size: 20
            bold: True
            size_hint_y: None
            height: 40
            color: 1, 1, 1, 1
        GridLayout:
            cols: 2
            size_hint_y: None
            height: 50
            spacing: 5
            Label:
                id: label_input
                text: 'Input'
                color: 1, 1, 1, 1
            CustomTextInput:
                id: algebra_entry
        GridLayout:
            cols: 2
            spacing: 5
            Button:
                id: btn_linear
                text: 'Linear'
                on_press: root.solve_linear()
            Button:
                id: btn_quadratic
                text: 'Quadratic'
                on_press: root.quadratic()

<StatisticsScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 10
        spacing: 10
        Label:
            id: title
            font_size: 20
            bold: True
            size_hint_y: None
            height: 40
            color: 1, 1, 1, 1
        GridLayout:
            cols: 2
            size_hint_y: None
            height: 50
            spacing: 5
            Label:
                id: label_input
                text: 'Input'
                color: 1, 1, 1, 1
            CustomTextInput:
                id: stats_entry
        GridLayout:
            cols: 2
            spacing: 5
            Button:
                id: btn_avg
                text: 'Average'
                on_press: root.average()
            Button:
                id: btn_max
                text: 'Max'
                on_press: root.maximum()
            Button:
                id: btn_min
                text: 'Min'
                on_press: root.minimum()
            Button:
                id: btn_prob
                text: 'Probability'
                on_press: root.probability()
""")
# =========================
# صفحه هندسه
# =========================
class GeometryScreen(BaseScreen):
    def update_texts(self):
        t = TRANSLATIONS[self.lang]
        self.ids.title.text = t['geometry']
        self.ids.label_n.text = t['n_or_height']
        self.ids.label_val.text = t['value']
        self.ids.btn_diagonals.text = t['diagonals']
        self.ids.btn_angles.text = t['angles']
        self.ids.btn_perimeter.text = t['perimeter']
        self.ids.btn_area.text = t['triangle_area']
        self.ids.btn_volume.text = t['sphere_volume']
        self.ids.btn_lateral.text = t['cylinder_lateral']
        self.ids.btn_circle_area.text = t['circle_area']
        self.ids.btn_circumference.text = t['circle_circumference']

    def diagonals(self):
        try:
            n = int(self.ids.n_entry.text)
            result = n * (n - 3) // 2
            formula = f"d = n(n-3)/2 = {n}({n-3})/2 = {result}"
            App.get_running_app().set_result(f"{self.translate('diagonals')}: {result}", formula)
        except:
            self.show_error('enter_n')

    def angles(self):
        try:
            n = int(self.ids.n_entry.text)
            total = (n - 2) * 180
            each = total / n
            formula = f"Sum = (n-2)×180 = ({n}-2)×180 = {total} | Each = {total}/{n} = {each}"
            App.get_running_app().set_result(f"Sum = {total} | Each = {each}", formula)
        except:
            self.show_error('enter_n')

    def perimeter(self):
        try:
            n = int(self.ids.n_entry.text)
            a = float(self.ids.val_entry.text)
            result = n * a
            formula = f"P = n×a = {n}×{a} = {result}"
            App.get_running_app().set_result(f"{self.translate('perimeter')} = {result}", formula)
        except:
            self.show_error('enter_n_side')

    def area(self):
        try:
            b = float(self.ids.val_entry.text)
            h = float(self.ids.n_entry.text)
            result = 0.5 * b * h
            formula = f"A = ½×b×h = ½×{b}×{h} = {result}"
            App.get_running_app().set_result(f"{self.translate('triangle_area')} = {result}", formula)
        except:
            self.show_error('enter_base_height')

    def volume(self):
        try:
            r = float(self.ids.val_entry.text)
            result = (4/3) * math.pi * r**3
            formula = f"V = 4/3×π×r³ = 4/3×π×{r}³ = {result}"
            App.get_running_app().set_result(f"{self.translate('sphere_volume')} = {result}", formula)
        except:
            self.show_error('enter_radius')

    def lateral(self):
        try:
            r = float(self.ids.val_entry.text)
            h = float(self.ids.n_entry.text)
            result = 2 * math.pi * r * h
            formula = f"LA = 2×π×r×h = 2×π×{r}×{h} = {result}"
            App.get_running_app().set_result(f"{self.translate('cylinder_lateral')} = {result}", formula)
        except:
            self.show_error('enter_radius_height')

    def circle_area(self):
        try:
            r = float(self.ids.val_entry.text)
            result = math.pi * r**2
            formula = f"A = π×r² = π×{r}² = {result}"
            App.get_running_app().set_result(f"{self.translate('circle_area')} = {result}", formula)
        except:
            self.show_error('enter_radius')

    def circle_perimeter(self):
        try:
            r = float(self.ids.val_entry.text)
            result = 2 * math.pi * r
            formula = f"C = 2×π×r = 2×π×{r} = {result}"
            App.get_running_app().set_result(f"{self.translate('circle_circumference')} = {result}", formula)
        except:
            self.show_error('enter_radius')

# =========================
# صفحه بردارها
# =========================
class VectorsScreen(BaseScreen):
    def update_texts(self):
        t = TRANSLATIONS[self.lang]
        self.ids.title.text = t['vectors']
        self.ids.label_v1.text = t['vector1']
        self.ids.label_v2.text = t['vector2']
        self.ids.btn_add.text = t['add_vectors']
        self.ids.btn_distance.text = t['distance']
        self.ids.btn_dot.text = t['dot_product']
        self.ids.btn_length.text = t['vector_length']

    def add_vectors(self):
        try:
            x1, y1 = map(float, self.ids.v1.text.split())
            x2, y2 = map(float, self.ids.v2.text.split())
            result = (x1+x2, y1+y2)
            formula = f"V1+V2 = ({x1},{y1})+({x2},{y2}) = ({result[0]},{result[1]})"
            App.get_running_app().set_result(f"Sum = ({result[0]}, {result[1]})", formula)
        except:
            self.show_error('use_x_y')

    def distance_vectors(self):
        try:
            x1, y1 = map(float, self.ids.v1.text.split())
            x2, y2 = map(float, self.ids.v2.text.split())
            d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
            formula = f"d = √(({x2}-{x1})²+({y2}-{y1})²) = {d}"
            App.get_running_app().set_result(f"Distance = {d}", formula)
        except:
            self.show_error('use_x_y')

    def dot_product(self):
        try:
            x1, y1 = map(float, self.ids.v1.text.split())
            x2, y2 = map(float, self.ids.v2.text.split())
            result = x1*x2 + y1*y2
            formula = f"V1·V2 = {x1}×{x2}+{y1}×{y2} = {result}"
            App.get_running_app().set_result(f"Dot Product = {result}", formula)
        except:
            self.show_error('use_x_y')

    def vector_length(self):
        try:
            x, y = map(float, self.ids.v1.text.split())
            result = math.sqrt(x*x + y*y)
            formula = f"|V| = √({x}²+{y}²) = {result}"
            App.get_running_app().set_result(f"Length = {result}", formula)
        except:
            self.show_error('use_x_y')

# =========================
# صفحه تناسب
# =========================
class ProportionScreen(BaseScreen):
    def update_texts(self):
        t = TRANSLATIONS[self.lang]
        self.ids.title.text = t['proportion']
        self.ids.label_input.text = t['proportion_input']
        self.ids.btn_table.text = t['table_proportion']
        self.ids.btn_percent.text = t['percent_of_total']

    def table(self):
        try:
            a, b, c = map(float, self.ids.prop_entry.text.split())
            result = (b*c)/a
            formula = f"x = (b×c)/a = ({b}×{c})/{a} = {result}"
            App.get_running_app().set_result(f"x = {result}", formula)
        except:
            self.show_error('use_a_b_c')

    def percent_p(self):
        try:
            p, t = map(float, self.ids.prop_entry.text.split())
            result = (p/t)*100
            formula = f"% = (p/t)×100 = ({p}/{t})×100 = {result}%"
            App.get_running_app().set_result(f"Percent = {result}%", formula)
        except:
            self.show_error('use_good_total')

# =========================
# صفحه جبر
# =========================
class AlgebraScreen(BaseScreen):
    def update_texts(self):
        t = TRANSLATIONS[self.lang]
        self.ids.title.text = t['algebra']
        self.ids.label_input.text = t['algebra_input']
        self.ids.btn_linear.text = t['solve_linear']
        self.ids.btn_quadratic.text = t['quadratic']

    def solve_linear(self):
        try:
            a, b, c = map(float, self.ids.algebra_entry.text.split())
            x = (c-b)/a
            formula = f"x = (c-b)/a = ({c}-{b})/{a} = {x}"
            App.get_running_app().set_result(f"x = {x}", formula)
        except:
            self.show_error('use_a_b_c')

    def quadratic(self):
        try:
            a, b, c = map(float, self.ids.algebra_entry.text.split())
            delta = b**2 - 4*a*c
            if delta < 0:
                App.get_running_app().set_result(self.translate('no_real_roots'), "")
                return
            x1 = (-b + math.sqrt(delta))/(2*a)
            x2 = (-b - math.sqrt(delta))/(2*a)
            formula = f"Δ = b²-4ac = {b}²-4×{a}×{c} = {delta}\nx1 = (-b+√Δ)/2a = {x1}\nx2 = (-b-√Δ)/2a = {x2}"
            App.get_running_app().set_result(f"x1 = {x1} | x2 = {x2}", formula)
        except:
            self.show_error('use_a_b_c')

# =========================
# صفحه آمار
# =========================
class StatisticsScreen(BaseScreen):
    def update_texts(self):
        t = TRANSLATIONS[self.lang]
        self.ids.title.text = t['statistics']
        self.ids.label_input.text = t['stats_input']
        self.ids.btn_avg.text = t['average']
        self.ids.btn_max.text = t['maximum']
        self.ids.btn_min.text = t['minimum']
        self.ids.btn_prob.text = t['probability']

    def average(self):
        try:
            nums = list(map(float, self.ids.stats_entry.text.split()))
            result = sum(nums)/len(nums)
            formula = f"Avg = ({'+'.join(map(str,nums))})/{len(nums)} = {result}"
            App.get_running_app().set_result(f"Average = {result}", formula)
        except:
            self.show_error('enter_numbers')

    def maximum(self):
        try:
            nums = list(map(float, self.ids.stats_entry.text.split()))
            result = max(nums)
            formula = f"Max = max({', '.join(map(str,nums))}) = {result}"
            App.get_running_app().set_result(f"Max = {result}", formula)
        except:
            self.show_error('enter_numbers')

    def minimum(self):
        try:
            nums = list(map(float, self.ids.stats_entry.text.split()))
            result = min(nums)
            formula = f"Min = min({', '.join(map(str,nums))}) = {result}"
            App.get_running_app().set_result(f"Min = {result}", formula)
        except:
            self.show_error('enter_numbers')

    def probability(self):
        try:
            g, t = map(float, self.ids.stats_entry.text.split())
            result = g/t
            formula = f"P = good/total = {g}/{t} = {result}"
            App.get_running_app().set_result(f"Probability = {result}", formula)
        except:
            self.show_error('use_good_total')
            # =========================
# صفحه ماشین حساب استاندارد (جدید)
# =========================
class CalculatorScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # عنوان صفحه
        self.title_label = Label(
            text=TRANSLATIONS[self.lang].get('calculator', 'Calculator'),
            font_size=20, bold=True, size_hint_y=None, height=40,
            color=(1, 1, 1, 1)
        )
        layout.add_widget(self.title_label)
        
        # صفحه نمایش ماشین حساب
        self.calc_display = TextInput(
            text='', font_size=24, multiline=False,
            size_hint_y=None, height=60,
            background_color=(0.1, 0.1, 0.1, 1),
            foreground_color=(1, 1, 1, 1),
            halign='right', valign='middle'
        )
        layout.add_widget(self.calc_display)
        
        # کیبورد اختصاصی ماشین حساب
        keypad = GridLayout(cols=4, spacing=5, size_hint_y=1)
        btns = [
            'C', '⌫', '%', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '(', ')', '.', '=',
            '0', '', '', ''
        ]
        for b in btns:
            if b == '':
                keypad.add_widget(Widget())
                continue
            btn = Button(text=b, font_size=20)
            btn.bind(on_press=lambda instance, val=b: self.on_calc_button(val))
            keypad.add_widget(btn)
            
        layout.add_widget(keypad)
        self.add_widget(layout)

    def update_texts(self):
        if hasattr(self, 'title_label'):
            self.title_label.text = TRANSLATIONS[self.lang].get('calculator', 'Calculator')

    def on_calc_button(self, val):
        if val == 'C':
            self.calc_display.text = ''
        elif val == '⌫':
            self.calc_display.text = self.calc_display.text[:-1]
        elif val == '=':
            self.calculate()
        else:
            self.calc_display.text += val

    def calculate(self):
        expr = self.calc_display.text
        try:
            # بررسی امنیت عبارت (فقط اعداد و عملگرهای مجاز)
            allowed = set("0123456789+-*/.() ")
            if not all(c in allowed for c in expr):
                raise ValueError("Invalid characters")
            
            # ارزیابی امن عبارت
            result = eval(expr, {"__builtins__": None}, {})
            self.calc_display.text = str(result)
            App.get_running_app().set_result(str(result), expr)
        except Exception:
            self.calc_display.text = "Error"

# =========================
# کلاس اصلی اپلیکیشن
# =========================
class APZApp(App):
    result_text = StringProperty("آماده")
    formula_text = StringProperty("")
    current_screen = NumericProperty(0)
    active_entry = None
    current_lang = 'fa'
    current_theme = 'dark'

    def build(self):
        self.sm = ScreenManager()
        # اضافه کردن صفحات (شامل صفحه جدید ماشین حساب)
        self.sm.add_widget(GeometryScreen(name='geometry'))
        self.sm.add_widget(VectorsScreen(name='vectors'))
        self.sm.add_widget(ProportionScreen(name='proportion'))
        self.sm.add_widget(AlgebraScreen(name='algebra'))
        self.sm.add_widget(StatisticsScreen(name='statistics'))
        self.sm.add_widget(CalculatorScreen(name='calculator')) # ✅ صفحه جدید

        # ساخت UI اصلی
        root = BoxLayout(orientation='vertical')

        # نوار ابزار بالا (زبان و تم)
        toolbar = BoxLayout(size_hint_y=None, height=50, spacing=5, padding=5)
        with toolbar.canvas.before:
            Color(rgba=(0.12, 0.16, 0.23, 1))
            self.toolbar_rect = Rectangle(pos=toolbar.pos, size=toolbar.size)
        toolbar.bind(pos=self._update_toolbar_rect, size=self._update_toolbar_rect)
        
        self.lang_btn = Button(
            text='🇮🇷 فارسی', size_hint_x=None, width=100,
            background_color=(0.2, 0.23, 0.29, 1), color=(1, 1, 1, 1)
        )
        self.lang_btn.bind(on_press=self.toggle_language)
        toolbar.add_widget(self.lang_btn)

        self.theme_btn = Button(
            text='🌙 تیره', size_hint_x=None, width=100,
            background_color=(0.2, 0.23, 0.29, 1), color=(1, 1, 1, 1)
        )
        self.theme_btn.bind(on_press=self.toggle_theme)
        toolbar.add_widget(self.theme_btn)

        self.title_label = Label(
            text=TRANSLATIONS['fa']['app_title'], font_size=16, bold=True, color=(1, 1, 1, 1)
        )
        toolbar.add_widget(self.title_label)
        root.add_widget(toolbar)

        # نوار نتیجه
        result_box = BoxLayout(orientation='vertical', size_hint_y=None, height=100, padding=5)
        with result_box.canvas.before:
            Color(rgba=(0.08, 0.12, 0.18, 1))
            self.result_rect = Rectangle(pos=result_box.pos, size=result_box.size)
        result_box.bind(pos=self._update_result_rect, size=self._update_result_rect)
        
        self.result_label = Label(
            text=self.result_text, font_size=16, bold=True, color=(1, 1, 0, 1),
            size_hint_y=None, height=40, halign='center', valign='middle',
            text_size=(Window.width, 40)
        )
        result_box.add_widget(self.result_label)

        self.formula_label = Label(
            text=self.formula_text, font_size=12, color=(0.5, 0.8, 1, 1),
            size_hint_y=None, height=40, halign='center', valign='middle',
            text_size=(Window.width, 40)
        )
        result_box.add_widget(self.formula_label)
        root.add_widget(result_box)

        # ScreenManager
        root.add_widget(self.sm)

        # ناوبری
        nav = BoxLayout(size_hint_y=None, height=60, spacing=20, padding=10)
        prev_btn = Button(
            text=TRANSLATIONS['fa']['previous'],
            background_color=(0.49, 0.23, 0.93, 1), color=(1, 1, 1, 1)
        )
        prev_btn.bind(on_press=self.prev_screen)
        
        next_btn = Button(
            text=TRANSLATIONS['fa']['next'],
            background_color=(0.49, 0.23, 0.93, 1), color=(1, 1, 1, 1)
        )
        next_btn.bind(on_press=self.next_screen)
        
        nav.add_widget(prev_btn)
        nav.add_widget(next_btn)
        root.add_widget(nav)

        # کیبورد مجازی عمومی (برای صفحات دیگر)
        keypad = GridLayout(cols=4, spacing=2, size_hint_y=None, height=200, padding=5)
        buttons = ['7', '8', '9', '-', '4', '5', '6', '.', '1', '2', '3', '⌫', '0', 'C', '', '']
        for btn_text in buttons:
            if btn_text == '':
                keypad.add_widget(Widget())
                continue
            btn = Button(text=btn_text)
            if btn_text == 'C':
                btn.background_color = (0.86, 0.15, 0.15, 1)
                btn.color = (1, 1, 1, 1)
                btn.bind(on_press=self.clear_entry)
            elif btn_text == '⌫':
                btn.background_color = (0.86, 0.15, 0.15, 1)
                btn.color = (1, 1, 1, 1)
                btn.bind(on_press=self.backspace)
            else:
                btn.bind(on_press=lambda x, t=btn_text: self.insert_num(t))
            keypad.add_widget(btn)
            
        root.add_widget(keypad)

        self.update_all_screens()
        return root

    def _update_toolbar_rect(self, instance, value):
        self.toolbar_rect.pos = instance.pos
        self.toolbar_rect.size = instance.size

    def _update_result_rect(self, instance, value):
        self.result_rect.pos = instance.pos
        self.result_rect.size = instance.size

    def toggle_language(self, instance):
        if self.current_lang == 'fa':
            self.current_lang = 'en'
            self.lang_btn.text = '🇬🇧 English'
            self.title_label.text = TRANSLATIONS['en']['app_title']
        else:
            self.current_lang = 'fa'
            self.lang_btn.text = '🇮🇷 فارسی'
            self.title_label.text = TRANSLATIONS['fa']['app_title']
        self.update_all_screens()
        self.result_label.text = TRANSLATIONS[self.current_lang]['ready']

    def toggle_theme(self, instance):
        if self.current_theme == 'dark':
            self.current_theme = 'light'
            self.theme_btn.text = '☀️ روشن'
            self.apply_theme_to_all('light')
        else:
            self.current_theme = 'dark'
            self.theme_btn.text = '🌙 تیره'
            self.apply_theme_to_all('dark')

    def apply_theme_to_all(self, theme):
        text_color = (0, 0, 0, 1) if theme == 'light' else (1, 1, 1, 1)
        for screen in self.sm.screens:
            screen.update_theme(theme)
        self.title_label.color = text_color
        self.result_label.color = (1, 1, 0, 1) if theme == 'dark' else (0.8, 0.4, 0, 1)
        self.formula_label.color = (0.5, 0.8, 1, 1) if theme == 'dark' else (0, 0.3, 0.8, 1)

    def update_all_screens(self):
        for screen in self.sm.screens:
            if hasattr(screen, 'update_language'):
                screen.update_language(self.current_lang)

    def insert_num(self, num):
        if self.active_entry:
            self.active_entry.insert_text(num)

    def backspace(self, instance):
        if self.active_entry:
            text = self.active_entry.text
            if len(text) > 0:
                self.active_entry.text = text[:-1]

    def clear_entry(self, instance):
        if self.active_entry:
            self.active_entry.text = ''

    def set_active_entry(self, entry):
        self.active_entry = entry

    def set_result(self, result, formula=""):
        self.result_text = result
        self.formula_text = formula
        self.result_label.text = result
        self.formula_label.text = f"📐 {formula}" if formula else ""

    def show_error(self, msg_key):
        msg = TRANSLATIONS[self.current_lang].get(msg_key, msg_key)
        popup = Popup(
            title=TRANSLATIONS[self.current_lang]['error'],
            content=Label(text=msg),
            size_hint=(0.8, 0.4)
        )
        popup.open()

    def next_screen(self, instance):
        # ✅ آپدیت شده برای ۶ صفحه (ایندکس ۰ تا ۵)
        if self.current_screen < 5:
            self.current_screen += 1
            self.sm.current = self.sm.screen_names[self.current_screen]

    def prev_screen(self, instance):
        if self.current_screen > 0:
            self.current_screen -= 1
            self.sm.current = self.sm.screen_names[self.current_screen]

    def translate(self, key):
        return TRANSLATIONS[self.current_lang].get(key, key)

# =========================
# اجرای برنامه
# =========================
if __name__ == '__main__':
    APZApp().run()
