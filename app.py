import flet as ft

def crear_titulos(texto, color):
    return ft.Text(
        f"{texto}",
        weight=ft.FontWeight.BOLD,
        color=color,
        size=50
    )

def crear_subtitulos(texto, color):
    return ft.Text(
        f"{texto}",
        weight=ft.FontWeight.BOLD,
        color=color,
        size=30
    )

def crear_textos(texto, color):
    return ft.Text(
        f"{texto}",
        weight=ft.FontWeight.BOLD,
        color=color,
        size=15
    )

def crear_textfield(label, color, color2):
    return ft.TextField(
        label=label,
        color=color,
        bgcolor=color2
    )

espacio_vacio1 = ft.Container(height=100)
espacio_vacio2 = ft.Container(height=50)

def main(page):

    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.theme_mode = ft.ThemeMode.LIGHT

    titulo = ft.Text(
        "CALCULADORA DE PRECIOS",
        size=50,
        weight=ft.FontWeight.BOLD,
        align=ft.Alignment.CENTER,
        color=ft.Colors.WHITE
    )

    ingresar_cantidad = crear_textfield("CANTIDAD", ft.Colors.BLACK, ft.Colors.WHITE)
    ingresar_perdida = crear_textfield("PÉRDIDA", ft.Colors.BLACK, ft.Colors.WHITE)
    fila_datos1 = ft.Row(
        controls=[ingresar_cantidad, ingresar_perdida],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY
    )

    ingresar_ganancia = crear_textfield("GANANCIA", ft.Colors.BLACK, ft.Colors.WHITE)

    contenedor = ft.Container(
        content=titulo,
        bgcolor=ft.Colors.BLACK,
        padding=20, 
        border_radius=10,
        align=ft.Alignment.CENTER,
        width=100000000000
    )

    page.add(contenedor, espacio_vacio1, fila_datos1, espacio_vacio2, ingresar_ganancia)

ft.run(main)