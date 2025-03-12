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
from pages.create_rls_users import RLSCreateforUsers
from pages.create_rls_groups import RLSCreateforGroups
from pages.assign_users_to_policy import RLSAssignUserstoPolicy
from pages.assign_values_to_group import RLSAssignValuestoGroup

def create() -> None:
    def create_rls_page_for_users():
        rls_instance = RLSCreateforUsers()  # Create an INSTANCE of RLSCreate
        rls_instance.run()          # Call the run method on the INSTANCE
    ui.page('/createrlsusers/')(create_rls_page_for_users)  # Pass the function to ui.page

    def create_rls_page_for_groups():
        rls_instance = RLSCreateforGroups()  # Create an INSTANCE of RLSCreate
        rls_instance.run()          # Call the run method on the INSTANCE
    ui.page('/createrlsgroups/')(create_rls_page_for_groups)  # Pass the function to ui.page

    def assign_users_to_policy():
        rls_instance = RLSAssignUserstoPolicy()  # Create an INSTANCE of RLSCreate
        rls_instance.run()          # Call the run method on the INSTANCE
    ui.page('/assignuserstopolicy/')(assign_users_to_policy) 

    def assign_values_to_group():
        rls_instance = RLSAssignValuestoGroup()  # Create an INSTANCE of RLSCreate
        rls_instance.run()          # Call the run method on the INSTANCE
    ui.page('/assignvaluestogroup/')(assign_values_to_group) 

if __name__ == '__main__':
    create()
