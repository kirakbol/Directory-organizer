import shutil
import glob
import os
from pathlib import Path
# you need to change the paths below to what you want them to be.
document_dir = 'C:/Users/kirak/Desktop/python_stuff/Test_dir_2/documents/'
audio_dir = 'C:/Users/kirak/Desktop/python_stuff/Test_dir_2/audio/'
video_dir = 'C:/Users/kirak/Desktop/python_stuff/Test_dir_2/video/'
picture_dir = 'C:/Users/kirak/Desktop/python_stuff/Test_dir_2/pictures/'
pythonscripts_dir = 'C:/Users/kirak/Desktop/python_stuff/Test_dir_2/python_scripts/'

'''
document_extensions = ['.doc', '.docx', '.log', '.msg', '.odt', '.pages', '.rtf', '.tex', '.txt', '.wpd', '.wps']
audio_extensions = ['.aif', '.aac', '.iff', '.m3u', '.m4a', '.mid', '.mp3', '.mpa', '.wav', '.wma']
video_extensions = ['.3g2', '.3gp', '.asf', '.avi', '.flv', '.m4v', '.mov', '.mp4', '.mpg', '.rm', '.srt', '.swf', '.vob', '.wmv']
picture_extensions = ['.3dm', '.3ds', '.max', '.obj', '.bmp', '.dds', '.gif', '.heic', '.jpg', '.png', '.psp', '.pspimage', '.tga', '.thm', '.tif', '.tiff', '.yuv', '.ai', '.eps', '.svg']
python_extensions = ['.egg-info', '.epp', '.oog', '.p', '.p4a', '.pickle', '.pil', '.pth', '.py', '.pyc', '.pyd', '.pyo', '.pyt', '.pyw', '.pyz', '.pyzw', '.rpy', '.ssdf', '.whl', '.yaml']
'''

def organizer(x, y):
    for file in Path(r'C:/Users/kirak/Desktop/python_stuff/Test_dir/').glob(f'*{x}'):
        try:
            os.rename(file, f'{y}{os.path.basename(file)}')
            print(f'moved {file} to {y}')
        except FileExistsError:
            continue

#for the video files
organizer('.avi', video_dir)
organizer('.flv', video_dir)
organizer('.m4v', video_dir)
organizer('.mov', video_dir)
organizer('.mp4', video_dir)
organizer('.rm', video_dir)
organizer('.srt', video_dir)
organizer('.vob', video_dir)
organizer('.wmv', video_dir)
#for the audio files
organizer('.aif', audio_dir)
organizer('.aac', audio_dir)
organizer('.iff', audio_dir)
organizer('.m3u', audio_dir)
organizer('.m4a', audio_dir)
organizer('.mid', audio_dir)
organizer('.mp3', audio_dir)
organizer('.mpa', audio_dir)
organizer('.wav', audio_dir)
organizer('.wma', audio_dir)
#for the document files
organizer('.doc', document_dir)
organizer('.docx', document_dir)
organizer('.log', document_dir)
organizer('.msg', document_dir)
organizer('.odt', document_dir)
organizer('.pages', document_dir)
organizer('.rtf', document_dir)
organizer('.tex', document_dir)
organizer('.txt', document_dir)
organizer('.wpd', document_dir)
organizer('.wps', document_dir)
#for the picture files
organizer('.max', picture_dir)
organizer('.obj', picture_dir)
organizer('.bmp', picture_dir)
organizer('.dds', picture_dir)
organizer('.gif', picture_dir)
organizer('.heic', picture_dir)
organizer('.jpg', picture_dir)
organizer('.png', picture_dir)
organizer('.tif', picture_dir)
organizer('.yuv', picture_dir)
organizer('.eps', picture_dir)
organizer('.svg', picture_dir)
#for the python files
organizer('.py', pythonscripts_dir)
organizer('.pyt', pythonscripts_dir)
organizer('.oog', pythonscripts_dir)