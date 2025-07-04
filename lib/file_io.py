def write_file(file_name, file_content):
    enhanced = str(file_name) + '.txt'
    with open(enhanced, mode = 'w', encoding='utf-8') as f:
        f.write(file_content)
   


def append_file(file_name, file_content):
    enhanced = str(file_name) + '.txt'
    with open(enhanced, mode = 'a', encoding='utf-8') as f:
        f.write(file_content)
 
    
  
def read_file(file_name):
    enhanced = str(file_name) + '.txt'
    with open( enhanced, encoding= 'utf-8') as f:
        return f.read()





write_file("text", "This is test content")
append_file('text', "This is appended content")
print(read_file('text'))

