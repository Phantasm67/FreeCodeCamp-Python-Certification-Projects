test_settings = {
    'theme': 'dark',
    'notifications': 'enabled',
    'volume': 'high'
}
new_settings = ('TheME', 'Dark')

def convert_lower(a_tuple):
    key, value = a_tuple
    return str(key).lower(), str(value).lower()

def add_setting(dictionary: dict, a_tuple: tuple):
    setting_key, setting_value = convert_lower(a_tuple)

    if setting_key in dictionary.keys():
        return f"Setting '{setting_key}' already exists! Cannot add a new setting with this name."
    else:
        dictionary[setting_key] = setting_value
        return f"Setting '{setting_key}' added with value '{setting_value}' successfully!"

def update_setting(dictionary: dict, a_tuple: tuple):
    setting_key, setting_value = convert_lower(a_tuple)

    if setting_key in dictionary.keys():
        dictionary[setting_key] = setting_value
        return f"Setting '{setting_key}' updated to '{setting_value}' successfully!"
    else:
        return f"Setting '{setting_key}' does not exist! Cannot update a non-existing setting."

def delete_setting(dictionary: dict, a_key: str):
    setting_key = a_key.lower()

    if setting_key in dictionary.keys():
        dictionary.pop(setting_key, None)
        return f"Setting '{setting_key}' deleted successfully!"
    else:
        return f"Setting not found!"

def view_settings(dictionary: dict):
    if dictionary == {}:
        return f"No settings available."

    else:
        result = "Current User Settings:\n"
        for key, value in dictionary.items():
            result += f"{str(key).capitalize()}: {str(value)}\n"

        return result
