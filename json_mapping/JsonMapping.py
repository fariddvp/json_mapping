import re

class JsonMapping:

    def resume_mapping(self, input_json, map_template_json, map_template_json_extra):
        if isinstance(input_json, dict):
            temp_dict = {}
            for key, value in input_json.items():
                # Check if key exists in map_template_json or map_template_json_extra
                if key in map_template_json:
                    new_key = map_template_json[key] if isinstance(map_template_json[key], str) else key
                    temp_dict[new_key] = self.resume_mapping(value, 
                                                             map_template_json.get(key, {}) if isinstance(map_template_json, dict) else {}, 
                                                             map_template_json_extra.get(key, {}) if isinstance(map_template_json_extra, dict) else {})
                elif key in map_template_json_extra:
                    new_key = map_template_json_extra[key] if isinstance(map_template_json_extra[key], str) else key
                    temp_dict[new_key] = self.resume_mapping(value, 
                                                             map_template_json.get(key, {}) if isinstance(map_template_json, dict) else {}, 
                                                             map_template_json_extra.get(key, {}) if isinstance(map_template_json_extra, dict) else {})
                else:
                    # اگر کلید در هیچکدام وجود ندارد، همان کلید را برگردانیم
                    temp_dict[key] = self.resume_mapping(value, 
                                                         map_template_json.get(key, {}) if isinstance(map_template_json, dict) else {}, 
                                                         map_template_json_extra.get(key, {}) if isinstance(map_template_json_extra, dict) else {})
            return temp_dict

        elif isinstance(input_json, list):
            # برای لیست‌ها پیمایش بازگشتی انجام دهیم
            return [self.resume_mapping(item, 
                                        map_template_json[0] if isinstance(map_template_json, list) else {}, 
                                        map_template_json_extra[0] if isinstance(map_template_json_extra, list) else {}) 
                    for item in input_json]

        else:
            # If the value is a primitive type (int, str, etc.), return it as is
            return input_json


    def replace_keys(self, json_str, mapping):
        for old_key, new_key in mapping.items():
            # Pattern to match the key (ensure it's a key by matching the colon after it)
            pattern = rf'"{old_key}"\s*:'
            replacement = f'"{new_key}":'
            json_str = re.sub(pattern, replacement, json_str)
        return json_str
            
