"""
App Name: Quran Ayah App
Author: Muhammad Altaaf
Contact: taafuuu@gmail.com


Program to read a specific ayah in full
"""


from aya_dict import surah_aya
from fonts_names import font_names
import flet as ft


def main(page):
    github_repo_url = 'https://github.com/taaaf11/Quran_App_Ayah'
    def change_tab(e):
        current_tab = e.control.selected_index
        tab_home.visible = True if current_tab == 0 else False
        tab_about.visible = True if current_tab == 1 else False
        page.update()
        
    page.title = 'Quran Ayah by Ayah'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = '#ff272f33'
    page.fonts = font_names
    
    
    def set_font_size(e):
        quran_text.size = font_size_slider.value
        page.update()
    
    
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
        quran_text.text_align = ft.TextAlign.CENTER
        
        page.update()
    
    
    # input field
    surah_aya_field = ft.TextField(hint_text='Surah:Ayah', label='Index', border_color = '#ff2ca4ab')
    
    # Quran text
    quran_text = ft.Text('', size=30)
    
    # font size scrollbar
    font_size_slider = ft.Slider(min=30, max=100, label="{value}",
                                 on_change=set_font_size, thumb_color='#ff2ca4ab', active_color='#ff2ca4ab')
    
    # submit button
    submit_button = ft.IconButton(ft.icons.CHECK, on_click=get_text, icon_color = '#ff2ca4ab')
    
    
    tab_home = ft.Container(ft.Column([
            ft.Row([
                surah_aya_field,
                submit_button
            ],
            alignment=ft.MainAxisAlignment.CENTER),
            
            quran_text,
            ft.Container(font_size_slider, margin=45)
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        padding=45,
        margin=30,
        visible=True)
    
    tab_about = ft.Column([
            ft.Text('Written by:', size = 50),
            ft.Container(ft.Column([
                ft.Text('Muhammad Altaaf', size=20)],
                                   horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                         margin=20),
            ft.Row([
                ft.Text('Source Code:'),
                ft.IconButton(ft.icons.EDIT_DOCUMENT, on_click=lambda _:page.launch_url(github_repo_url))
                ], alignment=ft.MainAxisAlignment.CENTER)
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER, visible=False)
    
    page.navigation_bar = ft.NavigationBar(
        destinations=[
        ft.NavigationDestination(icon=ft.icons.HOME, label='Home'),
        ft.NavigationDestination(icon=ft.icons.QUESTION_MARK, label='About'),
    ], selected_index=0, on_change=change_tab)
    
    page.add(ft.Column([tab_home, tab_about]))


if __name__ == '__main__':
    ft.app(target=main)
