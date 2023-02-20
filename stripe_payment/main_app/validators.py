
def validate_passed_item_ids(ids_str):
    return ids_str is not None and all(item.strip().isdigit() for item in ids_str.split(','))
