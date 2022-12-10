import logging
import urllib.request


class Task:

    def __init__(self, url: str):
        self.url = url
        self.name = self.parse_kata_name(self.url)
    
    @staticmethod
    def codewars_checker(url: str):
        return url.startswith('https://www.codewars.com/kata/')
    
    def parse_kata_name(self, url: str):
        print("🤖 start parse codewars kata's page")
        if Task.codewars_checker(url):
            try:
                with urllib.request.urlopen(url) as f:
                    content = f.read().decode('utf-8')

                idx = content.index('<h4 ')
                name = content[idx:idx+1000].split('>')[1][:-4].strip()  # yes, it's a magic!
            
                logging.info(name)
                
                return name

            except Exception as e:
                print(e)
                logging.info(e)
    
        
    def __repr__(self):
        return self.name




