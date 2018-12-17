import os
class FileManager:


    def create_dir(self,name,address):
        # Create a directory if theres not the same
        path=address+'/'+name       
        if not os.path.exists(path):
            os.mkdir(path)
            print("dir " , name ,  " created! ")


    def create_file(self,name,address):
        # Create a file if theres not the same
        path=address+'/'+name 
        if not os.path.exists(path):
            fileobj = open(path,"w")
            print("file ",name," created!")


    def delete(self,name,address):
        # delete  if theres was a file
        path=address+'/'+name
        if  os.path.exists(path):
            os.remove(path)
            print("file ",name," deleted!")

    
    def find(self,name,address):
        #find all files name in dir and sub dirs
        result = []
        for root, dirs, files in os.walk(address):  
            if name in files:
                result.append(os.path.join(root,name))
        return result


fm=FileManager()
fm.create_dir('test', '.')
fm.create_dir('test1', 'test')
fm.create_dir('test2', 'test/test1/')

fm.create_file('test.txt', 'test')
fm.create_file('test.txt', 'test/test1')
fm.create_file('test.txt', 'test/test1/test2')

print(fm.find('test.txt', 'test'))

fm.delete('test.txt', 'test')
fm.delete('test.txt', 'test/test1/')
fm.delete('test.txt', 'test/test1/test2')
#fm.restore('test.txt')
#fm.restore('test.txt')
