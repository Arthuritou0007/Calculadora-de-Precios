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
        bgcolor=color2,
        width=150
    )

espacio_vacio1 = ft.Container(height=100)
espacio_vacio2 = ft.Container(height=50)


# Funciones lógicas:
def calcular_precio(cantidad, pérdida, valor_original):
    cantidad_total = cantidad - pérdida
    precio_costo = valor_original / cantidad_total
    return round(precio_costo, 2)

def calcular_ganancia(precio_costo, ganancia):
    porcentaje = (ganancia / 100) + 1
    final = precio_costo * porcentaje
    return round(final, 2)


def main(page):

    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.theme_mode = ft.ThemeMode.LIGHT

    def calcular_ft(e):
        cantidad = int(ingresar_cantidad.value)
        perdida = int(ingresar_perdida.value)
        valor_original = int(ingresar_valor_original.value)
        ganancia = int(ingresar_ganancia.value)
        precio_costo = calcular_precio(cantidad, perdida, valor_original)

        dato_total.value = str(precio_costo)

        final = calcular_ganancia(precio_costo, ganancia)

        dato_costo.value = str(final)


    titulo = ft.Text(
        "CALCULADORA DE PRECIOS",
        size=50,
        weight=ft.FontWeight.BOLD,
        align=ft.Alignment.CENTER,
        color=ft.Colors.WHITE
    )
    contenedor_titulo = ft.Container(
        content=titulo,
        bgcolor=ft.Colors.BLACK,
        padding=20, 
        border_radius=10,
        align=ft.Alignment.CENTER,
        width=100000000000
    )

    seleccionar_cantidad = ft.SegmentedButton(
    segments=[
        ft.Segment(value="kg", label=ft.Text("Kg")),
        ft.Segment(value="unidades", label=ft.Text("Unidades")),
        ],
    selected=["kg"]
    )
    
    ingresar_cantidad = crear_textfield("CANTIDAD", ft.Colors.BLACK, ft.Colors.WHITE)
    fila_cantidad = ft.Row(
        controls=[ingresar_cantidad, seleccionar_cantidad]
    )
    ingresar_perdida = crear_textfield("PÉRDIDA", ft.Colors.BLACK, ft.Colors.WHITE)
    fila_datos1 = ft.Row(
        controls=[fila_cantidad, ingresar_perdida],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY
    )

    ingresar_ganancia = ft.TextField(
        label="GANANCIA",
        color=ft.Colors.BLACK,
        bgcolor=ft.Colors.WHITE,
        width=150,
        on_change=calcular_ft
    )

    texto_total = crear_subtitulos("Total:", ft.Colors.BLACK)
    dato_total = ft.Text(
        " ",
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.WHITE,
        size=30,
        align=ft.Alignment.CENTER
        )
    contenedor_total = ft.Container(
        content=dato_total,
        bgcolor=ft.Colors.BLACK,
        border_radius=10,
        padding=20,
        width=170
    )


    texto_costo = crear_subtitulos("Costo:", ft.Colors.BLACK)
    dato_costo = ft.Text(
        " ",
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.WHITE,
        size=30,
        align=ft.Alignment.CENTER
        )
    contenedor_costo = ft.Container(
        content=dato_costo,
        bgcolor=ft.Colors.BLACK,
        border_radius=10,
        padding=20,
        width=170
    )


    texto_sugerido = crear_subtitulos("Precio sugerido:", ft.Colors.BLACK)
    dato_sugerido = ft.Text(
        " ",
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.WHITE,
        size=30,
        align=ft.Alignment.CENTER
        )
    contenedor_sugerido = ft.Container(
        content=dato_sugerido,
        bgcolor=ft.Colors.BLACK,
        border_radius=10,
        padding=20,
        width=170
    )

    columna_datos_texto = ft.Column(
        controls=[texto_total, texto_costo, texto_sugerido],
        alignment=ft.MainAxisAlignment.CENTER
    )

    columna_datos = ft.Column(
        controls=[contenedor_total, contenedor_costo, contenedor_sugerido]
    )

    fila_precios = ft.Row(
        controls=[columna_datos_texto, columna_datos],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY
    )

    calcular = ft.Button("CALCULAR", on_click=calcular_ft)

    ingresar_valor_original = crear_textfield("Valor original", ft.Colors.BLACK, ft.Colors.WHITE)

    page.add(contenedor_titulo, espacio_vacio1, ingresar_valor_original, fila_datos1, espacio_vacio2, ingresar_ganancia, espacio_vacio2, calcular, espacio_vacio1, fila_precios)

ft.run(main)