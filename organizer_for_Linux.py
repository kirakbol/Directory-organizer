import shutil
import glob
import os
'''
#previously:

document_dir = '/home/pi/Documents/'
audio_dir = '/home/pi/Music/'
video_dir = '/home/pi/Videos/'
picture_dir = '/home/pi/Pictures/'
pythonscripts_dir = '/home/pi/Python/'

document_extensions = ['.doc', '.docx', '.log', '.msg', '.odt', '.pages', '.rtf', '.tex', '.txt', '.wpd', '.wps']
audio_extensions = ['.aif', '.aac', '.iff', '.m3u', '.m4a', '.mid', '.mp3', '.mpa', '.wav', '.wma']
video_extensions = ['.3g2', '.3gp', '.asf', '.avi', '.flv', '.m4v', '.mov', '.mp4', '.mpg', '.rm', '.srt', '.swf', '.vob', '.wmv']
picture_extensions = ['.3dm', '.3ds', '.max', '.obj', '.bmp', '.dds', '.gif', '.heic', '.jpg', '.png', '.psp', '.pspimage', '.tga', '.thm', '.tif', '.tiff', '.yuv', '.ai', '.eps', '.svg']
pythonscript_extensions = ['.egg-info', '.epp', '.oog', '.p', '.p4a', '.pickle', '.pil', '.pth', '.py', '.pyc', '.pyd', '.pyo', '.pyt', '.pyw', '.pyz', '.pyzw', '.rpy', '.ssdf', '.whl', '.yaml']

for file in glob.glob(f'/home/pi/Downloads/*{document_extensions}'):
    shutil.move(file, document_dir)
    print(f'moved {file} to {document_dir}')

for file in glob.glob(f'/home/pi/Downloads/*{audio_extensions}'):
    shutil.move(file, audio_dir)
    print(f'moved {file} to {audio_dir}')

for file in glob.glob(f'/home/pi/Downloads/*{video_extensions}'):
    shutil.move(file, video_dir)
    print(f'moved {file} to {video_dir}')

for file in glob.glob(f'/home/pi/Downloads/*{picture_extensions}'):
    shutil.move(file, picture_dir)
    print(f'moved {file} to {picture_dir}')

for file in glob.glob(f'/home/pi/Downloads/*{pythonscript_extensions}'):
    shutil.move(file, pythonscripts_dir)
    print(f'moved {file} to {pythonscripts_dir}')
'''

#current
types=[{"name":"document",
"path":"/home/pi/Documents/",
"extensions":['.doc', '.docx', '.log', '.msg', '.odt', '.pages', '.rtf', '.tex', '.txt', '.wpd', '.wps']},
{"name":"audio",
"path":"/home/pi/Music/",
"extensions":['.aif', '.aac', '.iff', '.m3u', '.m4a', '.mid', '.mp3', '.mpa', '.wav', '.wma']},
{"name":"video",
"path":"/home/pi/Videos/",
"extensions":['.3g2', '.3gp', '.asf', '.avi', '.flv', '.m4v', '.mov', '.mp4', '.mpg', '.rm', '.srt', '.swf', '.vob', '.wmv']},
{"name":"picture",
"path":"/home/pi/Pictures/",
"extensions":['.3dm', '.3ds', '.max', '.obj', '.bmp', '.dds', '.gif', '.heic', '.jpg', '.png', '.psp', '.pspimage', '.tga', '.thm', '.tif', '.tiff', '.yuv', '.ai', '.eps', '.svg']},
{"name":"pythonscript",
"path":"/home/pi/Python/",
"extensions":['.egg-info', '.epp', '.oog', '.p', '.p4a', '.pickle', '.pil', '.pth', '.py', '.pyc', '.pyd', '.pyo', '.pyt', '.pyw', '.pyz', '.pyzw', '.rpy', '.ssdf', '.whl', '.yaml']}]

for type in types:
    for file in glob.glob(f'/home/pi/Downloads/*{type["extensions"]}'):
        shutil.move(file, type["path"])
        print(f'moved {file} to {type["path"]}')
