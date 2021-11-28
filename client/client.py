# ----------------------------------------------------------------------
import dearpygui.dearpygui as dpg
# from dearpygui.demo import show_demo

# ----------------------------------------------------------------------
dpg.create_context()
dpg.create_viewport(title='Game World', width=1000, height=500)
# ----------------------------------------------------------------------
# Русский шрифт ////////////////////////////////////////////////////////
with dpg.font_registry():
    with dpg.font("fonts/Roboto-Regular.ttf", 18)  as font1:
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
with dpg.window(label="Game World", pos=(200, 50), width=560, height=340):
    dpg.bind_font(font1) # Применить русский шрифт

    dpg.add_text("Старт игры   ...   [ ok ]")
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# show_demo()
# dpg.show_font_manager()
# ----------------------------------------------------------------------
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
# ----------------------------------------------------------------------