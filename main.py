from json_mapping.JsonMapping import JsonMapping
from json_mapping.JsonKeyValueSwapper import JsonKeyValueSwapper
import os
import json

# Input json fields
resume_fields = {
        "countryCallingCode": "",
        "resume_id":"112654984",
        "mobileNumber": "",
        "email": "",
        "avatar": None,
        "firstName": "",
        "lastName": "",
        "gender": 1,
        "birthDate": "",
         "lat": 0.0,
         "long": 0.0,
         "address": "",
         "cityId": 1,
         "cityTitle": "",
         "provinceId": 1,
         "provinceTitle": "",
         "cv": None,
         "portfolio": None,
         "audioFile": None,
         "description": "",
         "personalCar": None,
         "drivingLicense": None,
        "degrees":
        [
          {
            "id": 0,
            "majorTitle": "",
            "majorId": 0,
            "subMajorId": 0,
            "subMajorTitle": "",
            "degree": "",
            "institutionName": "",
            "gpa": 0.0,
            "start": "",
            "end": ""
          }
        ],
        "skills":
        [
          {
            "id": 0,
            "title": "",
            "duration": 0
          }
        ],
        "jobExperiences": [ { "id": 0, "title": "", "companyName": "", "start": "", "end": "", "lastSalaryReceived": 0 } ],
        "projectExperiences": [ { "id": 0, "title": "", "employerName": "", "startOfProjectExperience": "", "endOfProjectExperience": "" } ],
        "interestCategories":
        [
          {
            "id": 0,

            "title": "",
            "interests": [
              {
                "id": 0,
                "title": ""
              }
            ]
          }
        ]
      }


# Get the root directory of the project
root_dir = os.path.abspath(os.path.dirname(__file__))

mapping_keys_path = os.path.join(root_dir, f'Mapping_Keys.json')

resume_professional_items_path = os.path.join(root_dir, f'Resume_Professional_Items.json')

# Read and load the JSON file
with open(mapping_keys_path, 'r', encoding='utf-8') as json_file:
    mapping_keys = json.load(json_file)

with open(mapping_keys_path, 'r', encoding='utf-8') as json_file:
    resume_professional_items = json.load(json_file)

#########################################################################################################

# Resume mapping for LLM input
mapper = JsonMapping()
resume_fields_mapped_json = mapper.resume_mapping(resume_fields, mapping_keys[0], resume_professional_items[0])

json_str = json.dumps(resume_fields_mapped_json, ensure_ascii=False)
resume_fields_mapped_json = mapper.replace_keys(json_str, resume_professional_items[0])

json_swapper = JsonKeyValueSwapper()
resume_mapping_swapped = json_swapper.swap_keys_values(mapping_keys[0])

resume_mapping_extra_swapped = json_swapper.swap_keys_values(resume_professional_items[0])

resume_mapping_swapped_str = json.dumps(resume_mapping_swapped, ensure_ascii=False)
resume_mapping_swapped = mapper.replace_keys(resume_mapping_swapped_str, resume_professional_items[0])

# Convert to json
resume_mapping_swapped = json.loads(resume_mapping_swapped)

# Example LLM output
llm_output = {
    "نام": "فرید",
    "نام خانوادگی": "دیوان پور",
    "جنسیت": "مرد"
}

llm_output_mapped = mapper.resume_mapping(llm_output, resume_mapping_swapped, resume_mapping_extra_swapped)

llm_output_str = json.dumps(llm_output_mapped, ensure_ascii=False)
response = mapper.replace_keys(llm_output_str, resume_mapping_extra_swapped)


print("Final Result: ", response)