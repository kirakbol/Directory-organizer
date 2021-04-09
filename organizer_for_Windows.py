import shutil
import glob
import os

#change the paths below to what you want them to be or even add new if you need more
document_dir = 'C:/Users/kirak/Desktop/python_stuff/Test_dir_2/documents/'
audio_dir = 'C:/Users/kirak/Desktop/python_stuff/Test_dir_2/audio/'
video_dir = 'C:/Users/kirak/Desktop/python_stuff/Test_dir_2/video/'
picture_dir = 'C:/Users/kirak/Desktop/python_stuff/Test_dir_2/pictures/'
pythonscripts_dir = 'C:/Users/kirak/Desktop/python_stuff/Test_dir_2/python_scripts/'
#change the extensions or even add new ones depending on what files you want to move
document_extensions = ['.doc', '.docx', '.log', '.msg', '.odt', '.pages', '.rtf', '.tex', '.txt', '.wpd', '.wps']
audio_extensions = ['.aif', '.aac', '.iff', '.m3u', '.m4a', '.mid', '.mp3', '.mpa', '.wav', '.wma']
video_extensions = ['.3g2', '.3gp', '.asf', '.avi', '.flv', '.m4v', '.mov', '.mp4', '.mpg', '.rm', '.srt', '.swf', '.vob', '.wmv']
picture_extensions = ['.3dm', '.3ds', '.max', '.obj', '.bmp', '.dds', '.gif', '.heic', '.jpg', '.png', '.psp', '.pspimage', '.tga', '.thm', '.tif', '.tiff', '.yuv', '.ai', '.eps', '.svg']
pythonscripts_extensions = ['.egg-info', '.epp', '.oog', '.p', '.p4a', '.pickle', '.pil', '.pth', '.py', '.pyc', '.pyd', '.pyo', '.pyt', '.pyw', '.pyz', '.pyzw', '.rpy', '.ssdf', '.whl', '.yaml']


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






organizer(document_dir,document_extensions)
organizer(audio_dir,audio_extensions)
organizer(video_dir,video_extensions)
organizer(picture_dir,picture_extensions)
organizer(pythonscripts_dir,pythonscripts_extensions)