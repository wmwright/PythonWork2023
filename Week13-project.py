import os

def generate_file_info(path='.'):
    file_info_list = []

    for root, dirs, files in os.walk(path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_size = os.path.getsize(file_path)

            file_info = {
                'name': file_name,
                'path': file_path,
                'size': file_size
            }

            file_info_list.append(file_info)

    return file_info_list

# Example usage:
path = input("Enter a directory path (optional): ")
file_info_list = generate_file_info(path)
print(file_info_list)
