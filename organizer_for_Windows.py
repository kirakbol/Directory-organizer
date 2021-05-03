import shutil
import glob
import os

types = [
    {
        'name': 'documents',
        'dir_path': 'C:/Users/kirak/Desktop/python_stuff/Test_dir_2/documents/',
        'extension': ['.doc', '.docx', '.log', '.msg', '.odt', '.pages', '.rtf', '.tex', '.txt', '.wpd', '.wps'],
    },
    {
        'name': 'audio',
        'dir_path': 'C:/Users/kirak/Desktop/python_stuff/Test_dir_2/audio/',
        'extension': ['.aif', '.aac', '.iff', '.m3u', '.m4a', '.mid', '.mp3', '.mpa', '.wav', '.wma'],
    },
    {
        'name': 'video',
        'dir_path': 'C:/Users/kirak/Desktop/python_stuff/Test_dir_2/video/',
        'extension': ['.3g2', '.3gp', '.asf', '.avi', '.flv', '.m4v', '.mov', '.mp4', '.mpg', '.rm', '.srt', '.swf', '.vob', '.wmv'],
    },
    {
        'name': 'picture',
        'dir_path': 'C:/Users/kirak/Desktop/python_stuff/Test_dir_2/pictures/',
        'extension': ['.3dm', '.3ds', '.max', '.obj', '.bmp', '.dds', '.gif', '.heic', '.jpg', '.png', '.psp', '.pspimage', '.tga', '.thm', '.tif', '.tiff', '.yuv', '.ai', '.eps', '.svg'],
    },
    {
        'name': 'pythonscripts',
        'dir_path': 'C:/Users/kirak/Desktop/python_stuff/Test_dir_2/python_scripts/',
        'extension': ['.egg-info', '.epp', '.oog', '.p', '.p4a', '.pickle', '.pil', '.pth', '.py', '.pyc', '.pyd', '.pyo', '.pyt', '.pyw', '.pyz', '.pyzw', '.rpy', '.ssdf', '.whl', '.yaml'],
    },
         ]

check_path='C:/Users/kirak/Desktop/python_stuff/Test_dir/'
def organizer(new_dir,extension_set):
    path_names_list=[name for name in os.listdir(r'C:\Users\kirak\Desktop\python_stuff\Test_dir') if list(filter(name.endswith,extension_set)) != [] ]
    destination_path_names_list=[name for name in os.listdir(new_dir) if list(filter(name.endswith,extension_set)) != [] ]
    for name in path_names_list:
        if name in destination_path_names_list:
            i=0
            new_file_name=name
            while new_file_name in destination_path_names_list:             #tracks if there's a file with the same name and finds what number indicator to put
                i=i+1
                x=""                
                for j in new_file_name:          #tracks at which spot of the filename the . is so it puts the number indicator before it
                    if j==".":
                        x=x+"("+str(i)+")"+j
                    else:
                        x=x+j
                if not(x in destination_path_names_list):
                    new_file_name=x

            os.replace(check_path+name,new_dir+new_file_name)
            print(f'moved file {name} to {new_dir}')
        else:
            os.replace(check_path+name,new_dir+name)
            print(f'moved file {name} to {new_dir}')

for i in types:
    organizer(i['dir_path'], i['extension'])
