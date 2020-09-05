'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

class FileSystem:
	currentDir = ''
	rootdir="/"
	parentDir = '..'
	dirList = []
	
	def reverse(self,s):
	    if len(s) ==0:
	        return s
	    else:
	        return self.reverse(s[1:])+s[0]
	
	def cd(self,path):
	   if(path[:1] == "/"):
	       path = "/"+path.strip("/")+"/"
	       if(path in self.dirList):
	         self.currentDir =path
	       else:
	         print("path \""+ path+"\" does not exist")
	   
	   elif(path.strip("/") ==".."):
	       self.currentDir = self.reverse(self.currentDir).lstrip("/")
	       self.currentDir = self.currentDir[self.currentDir.find("/")+1:]
	       self.currentDir = self.reverse(self.currentDir)

	   else:
	    path = "/"+path.strip("/")+"/"
	    constructedPath = (self.currentDir.rstrip("/")+path).strip()
	    if(constructedPath in self.dirList):
	        self.currentDir =self.currentDir.rstrip("/")+path
	    else:
	        print("path does not exist")

	
	def pwd(self):
	    return self.currentDir
	
	def mkdir(self,name):
	 global dirList,currentDir
	 if(name[:1] =="/"):
	     strname =str(name).strip("/")
	     if(strname.find("/")>0):
	      strname = self.reverse(strname)
	      strname = strname[strname.find("/")+1:]
	      strname = "/"+self.reverse(strname)+"/"
	      if(strname in self.dirList):
	         self.dirList.append(name.rstrip("/")+"/")
	      else:
	         print(strname + " folder does not exist")
	     else:
	         self.dirList.append(self.currentDir.rstrip("/")+"/"+strname+"/")
	 else:   
	  strname = str(name).strip("/")
	  orgstrname = strname
	  if(strname.find("/")>0):
	     strname = self.reverse(strname)
	     strname = strname[strname.find("/")+1:]
	     strname = "/"+self.reverse(strname)+"/"
	     if((self.currentDir.rstrip("/")+ strname) in self.dirList):
	         self.dirList.append(self.currentDir+"/"+orgstrname+"/")
	     else:
	         print("folder \""+strname.strip("/") +"\" does not exist")
	  else:
	    self.dirList.append(self.currentDir.rstrip("/")+"/"+strname+"/")

	 
	def rmdir(self,path):
	  if(path[:1] == "/"):
	       path = "/"+path.strip("/")+"/"
	       if(path in self.dirList):
	           self.dirList.remove(path)
	       else:
	         print("path \""+ path+"\" does not exist")

	  else:
	    path = "/"+path.strip("/")+"/"
	    directory = self.reverse(self.currentDir.strip("/"))
	    directory = directory[directory.find("/")+1:]
	    directory = "/"+self.reverse(directory)+"/"
	    constructedPath = (directory.rstrip("/")+path).strip()
	    if(constructedPath in self.dirList):
	        self.dirList.remove(constructedPath)
	        self.cd(directory)
	    else:
	        print("path does not exist")
	        

if __name__ == "__main__":

    fs=FileSystem()
    fs.mkdir('usr'); 
    fs.cd('usr'); 
    fs.mkdir('local'); 
    fs.cd('local'); 
    print(fs.pwd()); 
    fs.cd('..'); 
    fs.mkdir('share'); 
    fs.mkdir('share/info'); 
    fs.cd('share/info'); 
    print(fs.pwd()) 
    fs.mkdir('/usr/local/log'); 
    fs.cd('/usr/local/log'); 
    print(fs.pwd()); 
    fs.mkdir('some/folder')
    fs.cd('/usr/unknown/folder');
