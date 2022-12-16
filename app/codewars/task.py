import logging
import re
import urllib.request


class Task:

    def __init__(self, url: str):
        self.url = url
    
    @property
    def name(self):
        return self.parse_kata_name(self.url)
    
    @staticmethod
    def codewars_checker(url: str):
        return url.startswith('https://www.codewars.com/kata/')
    
    def parse_kata_name(self, url: str):
        print("🤖 start parse codewars kata's page")
        if Task.codewars_checker(url):
            try:
                with urllib.request.urlopen(url) as f:
                    content = f.read().decode('utf-8')
                    
                REG = '<h4[^>]*>([^<]*)<\/h4>'

                name = re.search(REG, content).group(1)
                            
                logging.info(name)
                
                return name

            except Exception as e:
                print(e)
                logging.info(e)
    
        
    def __repr__(self):
        return self.name



url = 'https://www.codewars.com/kata/514b92a657cdc65150000006'
task = Task(url)


print(task)
