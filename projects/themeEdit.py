def add_setting(user_settings,setting_tuple):
    key, value = setting_tuple
    key= key.lower()
    value= value.lower()
    if key in user_settings:
        print(f"Setting {key} already exists! Cannot add a new setting with this name.")
    else :
        print(f"Setting '{key}' added with value '{value}' successfully!")
def update_setting(user_settings,setting_tuple) :
    key, value = setting_tuple
    key= key.lower()
    value= value.lower()
    if key in user_settings:
        print(f"Setting '{key}' updated to '{value}' successfully!")
    else :
        print(f"Setting '{key}' does not exist! Cannot update a non-existing setting.")
def delete_setting(user_settings,key) :
    key= key.lower()
    if key in user_settings:
        print(f"Setting '[{key}' deleted successfully!")
    else :
        print(f"Setting not found!")
def view_settings(user_settings):
    if len(user_settings)== 0:
        print("No settings available.")
    else :
        print("Current User Settings:")
        for key, value in user_settings.items():
            print(f"'{key}': '{value}'")

test_settings={ 'Theme' : 'dark', 'Notifications': 'enabled'}
add_setting({'theme': 'light'}, ('THEME', 'dark'))
add_setting({'theme': 'light'}, ('volume', 'high'))
update_setting({'theme': 'light'}, ('theme', 'dark'))
update_setting({'theme': 'light'}, ('volume', 'high'))
delete_setting({'theme': 'light'}, 'theme')
delete_setting({'theme': 'light'}, '')
view_settings({})
view_settings(test_settings)

