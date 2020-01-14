import os

os.environ['JAVA_HOME'] = r"C:\java_dev_env\jdk6_gr"
os.environ['PATH'] = os.environ['PATH'] + r";C:\java_dev_env\jdk6_gr\bin"
os.environ['CLASSPATH'] = r".;C:\java_dev_env\jdk6_gr\lib\tools.jar;C:\Users\Administrator\Documents\workspace-spring-tool-suite-4-4.4.0.RELEASE\zshjym\bin;;C:\Users\Administrator\Documents\workspace-spring-tool-suite-4-4.4.0.RELEASE\zshjym\lib\JNative.jar"

with open('zsh.txt','r',encoding='gbk') as f:
    zshs = f.readlines()

for zsh in zshs:
    cmd = r"java com.zshjym.Helper {}".format(zsh[0:14])
    os.system(cmd)