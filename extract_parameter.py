# I am pre-defining input_dict as the unit_operations_data dictionary in the function's arguments
def extract_parameter(unit_name, param_name, index, input_dict=unit_operations_data):
    # dict.get() allows us to retrieve the values stored by a specified key (in this case unit_name), and will return a keyerror if the key isn't found.
    sub_dict = input_dict.get(unit_name)
    # Looking at the structure of unit_operations_data, it holds sub dictionaries "distillation_column", "reactor", and "heat_exchanger" which can be accessed using the same dict.get() as before.
    sub_list = sub_dict.get(param_name)
    value = sub_list[index]
    return f'{unit_name}_{param_name}_{value}'
