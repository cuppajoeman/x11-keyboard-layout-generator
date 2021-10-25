import sys

TOP_ROW = [
    "<AD01>",
    "<AD02>",
    "<AD03>",
    "<AD04>",
    "<AD05>",
    "<AD06>",
    "<AD07>",
    "<AD08>",
    "<AD09>",
    "<AD10>",
]

HOME_ROW = [
    "<AC01>",
    "<AC02>",
    "<AC03>",
    "<AC04>",
    "<AC05>",
    "<AC06>",
    "<AC07>",
    "<AC08>",
    "<AC09>",
    "<AC10>",
]

BOTTOM_ROW = [
    "<AB01>",
    "<AB02>",
    "<AB03>",
    "<AB04>",
    "<AB05>",
    "<AB06>",
    "<AB07>",
    "<AB08>",
    "<AB09>",
    "<AB10>",
]

KEYBOARD = [TOP_ROW, HOME_ROW, BOTTOM_ROW]

custom_keyboard = [[], [], []]

file_name = sys.argv[1]

with open(file_name) as keyboard_file:
    for row_num, row in enumerate(keyboard_file):
        full_row = row.split("|")
        cleaned_row = full_row[1:-1]
        for key_num, string in enumerate(cleaned_row):
            keyboard_keys = []
            for character in string:
                temp_unicode = hex(ord(character))
                unicode = "U" + temp_unicode.upper()[2:]
                keyboard_keys.append(unicode)
            custom_keyboard[row_num].append([KEYBOARD[row_num][key_num], keyboard_keys])


def format_custom_keyboard_for_config_file(custom_keyboard):
    config_string = """\n    // CUSTOM CONFIGURATION\n\n"""
    for row in custom_keyboard:
        for key_config in row:
            key_name = key_config[0]
            key_bindings = key_config[1]
            config_string += f"    key {key_name} {{    {key_bindings}   }};\n"
        config_string_cleaned = config_string.replace("'", "")
        config_string_cleaned += """\n    // END CUSTOM CONFIGURATION\n"""
    return config_string_cleaned


print(format_custom_keyboard_for_config_file(custom_keyboard))


with open("us_copy", "r") as f:
    contents = f.readlines()

index = 56

contents.insert(index, format_custom_keyboard_for_config_file(custom_keyboard))

with open("custom_layout", "w") as f:
    contents = "".join(contents)
    f.write(contents)
