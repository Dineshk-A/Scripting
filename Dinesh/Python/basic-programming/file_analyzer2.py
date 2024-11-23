import os 

class fileanalyzer():
    def __init__(self,file_path) -> None:
        self.file_path = file_path
    
    def file_exists(self):
        return os.path.exists(self.file_path)
    
    def analyse(self):
        if not self.file_exists():
            raise FileNotFoundError(f"file doesnt exists '{self.file_path}'")
        
        with open(self.file_path,'r') as file:
            lines = file.readlines()

        lines_count = len(lines)
        word_count = sum(len(line.split()) for line in lines)
        char_count = sum(len(line) for line in lines)

        return {
            "lines": lines_count,
            "words": word_count,
            "chars": char_count
        }
    
def main():
    file_path = r"c:\Dinesh Kumar\leetcode\Bash Scripting\day 1\ask_name.sh"

    analyzer = fileanalyzer(file_path)

    try:
        result = analyzer.analyse()

        print(f"line count: '{result['lines']}")
        print(f"word count: '{result['words']}")
        print(f"char count: '{result['chars']}")

    except FileNotFoundError as e:
        print(e)

    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()