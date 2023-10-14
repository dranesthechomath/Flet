import flet as ft  #upm package(flet)


def main(page: ft.Page):
    page.title = "Flet example App"
    page.horizontal_alignment = "center"
    page.padding = 10
    dioxide = ft.TextField(value="", text_align="center", width=100)
    bicarb = ft.TextField(value="", text_align="center", width=100)
    txt_ph = ft.Text(text_align="center", width=200)

    def btn_ph_click(e):
        dioxide_val = dioxide.value
        bicarb_val = bicarb.value
        hydrogen = (float(dioxide_val) / float(bicarb_val)) * 0.24
        ph = 7.80 - hydrogen
        txt_ph.value = f"pH should be: {ph:.3}"
        page.update()

    ct_1 = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(controls=[
                    ft.Text("Dioxide Value : "),
                    dioxide,
                ],
                       alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                       height=50),
                ft.Row(controls=[
                    ft.Text("HCO3 value : "),
                    bicarb,
                ],
                       alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                       height=50),
                ft.Row(controls=[
                    ft.ElevatedButton(
                        text="Calculate PH",
                        width=200,
                        on_click=btn_ph_click,
                    ),
                ],
                       alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                       height=50),
                txt_ph,
            ],
            #alignment="center"),
            spacing=50,
        ),
        width=500,
        height=400,
        padding=25,
        margin=20,
        border_radius=25,
        bgcolor="teal")

    page.add(ct_1, )


ft.app(main)
