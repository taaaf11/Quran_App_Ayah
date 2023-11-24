from aya_dict import surah_aya
from fonts_names import font_names
import flet as ft


def main(page):
    page.title = 'Quran Ayah by Ayah'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = '#ff272f33'
    page.fonts = font_names
    
    # input field
    surah_aya_field = ft.TextField(hint_text='Surah:Ayah', label='Index')
    surah_aya_field.border_color = '#ff2ca4ab'
    
    # Quran text
    quran_text = ft.Text('', size=40)
    
    def get_text(e):
        index = surah_aya_field.value
        data = surah_aya[index]
        
        # get arabic text
        text = data[0]
        
        # get font name
        font = data[1]
        
        # display quran
        quran_text.font_family = f"{font}"
        quran_text.value = text
        
        page.update()
        
    # submit button
    submit_button = ft.IconButton(ft.icons.CHECK, on_click=get_text)
    submit_button.icon_color = '#ff2ca4ab'
    
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