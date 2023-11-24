from aya_dict import surah_aya
import flet as ft


def main(page):
    page.title = 'Quran Ayah by Ayah'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.fonts = {}
    
    quran_text = ft.Text('a', size=10)
    surah_aya_field = ft.TextField(hint_text='Surah:Ayah', label='Index')
    
    def get_text(e):
        index = surah_aya_field.value
        data = surah_aya[index]
        # get arabic text
        text = data[0]
        # get font name
        font = data[1]
        # set to field
        quran_text.font_family = f"Fonts\\{font}.ttf"
        quran_text.value = text
        page.update()
        
    
    submit_button = ft.IconButton(ft.icons.CHECK, on_click=get_text)
    
    page.add(
        ft.Column([
            ft.Row([
                surah_aya_field,
                submit_button
            ],
            alignment=ft.MainAxisAlignment.CENTER),
            
            quran_text
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )


if __name__ == '__main__':
    ft.app(target=main)