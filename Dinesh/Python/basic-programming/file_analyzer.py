"""This Program checks if file exists in locally"""

import os 

class fileanalyser():
    def __init__(self,file_path) -> None:
        self.file_path = file_path 

    def file_exists(self):
        return os.path.exists(self.file_path)
    
analyser = fileanalyser(r"c:\Dinesh Kumar\leetcode\Bash Scripting\day 1\ask_name.sh")

if analyser.file_exists():
    print(f"file path {analyser.file_path} exists")
else:
    print("file doesnt exists")