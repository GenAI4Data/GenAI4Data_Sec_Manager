# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# "IMPORTANT: This application is a prototype and should be used for experimental purposes only.
# It is not intended for production use. 
# This software is provided 'as is' without warranty of any kind, express or implied, including but not limited to the warranties 
# of merchantability, fitness for a particular purpose and noninfringement. 
# In no event shall Google or the developers be liable for any claim, damages or other liability, whether in an action of contract, 
# tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software. 
# Google is not responsible for the functionality, reliability, or security of this prototype. 
# Use of this tool is at your own discretion and risk."


from nicegui import ui

def menu() -> None:
    # ui.button('Home', icon='home', on_click=lambda: ui.navigate.to('/')).props('align=left').style('width:250px')
    # ui.button('Create Row Level Policy', icon='policy', on_click=lambda: ui.navigate.to('/createrls/')).props('align=left').style('width:250px')
    # ui.button('Assign Filters to Policy', icon='filter_alt', on_click=lambda: ui.navigate.to('/assignfilters/')).props('align=left').style('width:250px')
    # ui.button('Audit Logs', icon='gavel', on_click=lambda: ui.navigate.to('/reports/')).props('align=left').style('width:250px')

    with ui.list():#.props('dense separator'):
        with ui.item(on_click=lambda: ui.navigate.to('/')):
            with ui.item_section().props('avatar'):
                ui.icon('home', color='blue-500')
            with ui.item_section():
                ui.item_label('Home').classes(replace = 'text-primary text-bold').style('font-size:16px')
        with ui.expansion('Row Level Security', caption='Click to Expand', icon='policy').classes('w-full text-primary text-bold').style('font-size:16px'):
            with ui.item(on_click=lambda: ui.navigate.to('/createrlsusers/')):
                with ui.item_section().props('avatar'):
                    ui.icon('person', color='blue-500')
                with ui.item_section():
                    ui.item_label('Create RLS for Users').classes(replace = 'text-primary text-bold').style('font-size:14px')
            with ui.item(on_click=lambda: ui.navigate.to('/createrlsgroups/')):
                with ui.item_section().props('avatar'):
                    ui.icon('groups', color='blue-500')
                with ui.item_section():
                    ui.item_label('Create RLS for Groups').classes(replace = 'text-primary text-bold').style('font-size:14px')
            with ui.item(on_click=lambda: ui.navigate.to('/assignuserstopolicy/')):
                with ui.item_section().props('avatar'):
                    ui.icon('assignment_ind', color='blue-500')
                with ui.item_section():
                    ui.item_label('Assign Users to Policy').classes(replace = 'text-primary text-bold').style('font-size:14px')
            with ui.item(on_click=lambda: ui.navigate.to('/assignvaluestogroup/')):
                with ui.item_section().props('avatar'):
                    ui.icon('assignment', color='blue-500')
                with ui.item_section():
                    ui.item_label('Assign Values to Groups').classes(replace = 'text-primary text-bold').style('font-size:14px')
        with ui.item(on_click=lambda: ui.navigate.to('/')):
            with ui.item_section().props('avatar'):
                ui.icon('gavel', color='blue-500')
            with ui.item_section():
                ui.item_label('Audit Logs').classes(replace = 'text-primary text-bold').style('font-size:16px')
                ui.item_label('Coming Soon!').props('caption')