import shutil
import glob
import os

types=[{"name":"document",
"path":"/home/dj_gandalf/test/documents",
"extensions":['doc', 'docx', 'log', 'msg', 'odt', 'pages', 'rtf', 'tex', 'txt', 'wpd', 'wps', 'pdf']},
{"name":"audio",
"path":"/home/dj_gandalf/test/audio",
"extensions":['aif', 'aac', 'iff', 'm3u', 'm4a', 'mid', 'mp3', 'mpa', 'wav', 'wma']},
{"name":"video",
"path":"/home/dj_gandalf/test/videos",
"extensions":['3g2', '3gp', 'asf', 'avi', 'flv', 'm4v', 'mov', 'mp4', 'mpg', 'rm', 'srt', 'swf', 'vob', 'wmv']},
{"name":"picture",
"path":"/home/dj_gandalf/test/pictures",
"extensions":['.3dm', '3ds', 'max', 'obj', 'bmp', 'dds', 'gif', 'heic', 'jpg', 'png', 'psp', 'pspimage', 'tga', 'thm', 'tif', 'tiff', 'yuv', 'ai', 'eps', 'svg']},
{"name":"pythonscript",
"path":"/home/dj_gandalf/test/Python",
"extensions":['egg-info', 'epp', 'oog', 'p', 'p4a', 'pickle', 'pil', 'pth', 'py', 'pyc', 'pyd', 'pyo', 'pyt', 'pyw', 'pyz', 'pyzw', 'rpy', 'ssdf', 'whl', 'yaml']},]

for type in types:
    for extension in type["extensions"]:
        for file in glob.glob(f'/home/dj_gandalf/test/source/*.{extension}'):
            shutil.move(file, type["path"])
            print(f'moved {file} to {type["path"]}')
