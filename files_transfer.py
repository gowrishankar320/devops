import shutil
import os
path="\\\\192.168.11.90\\MACK-Releases\\consolidations"
source = path+'\\'+%Enter Release Number:%+'\\APP'
destination1 = os.environ['JBOSS_HOME']+'\\modules'
destination2 = os.environ['JBOSS_HOME']+'\\standalone\\deployments'
print(source)
for lt in os.listdir(source):
    if lt == 'modules':
        b=source+'\modules'
        for ms in os.listdir(b):
            if ms == '()':
                d=b+'\()'
            if ms == '( )':
                d=b+'\( )'
            if ms == '(2)':
                d=b+'\(2)'
            if ms == 'svm':
                d=b
            print(f"source - {d} , destination1 {destination1}")
            os.system("Robocopy "+d+" "+destination1+" /E /IS /IT /IM")
            print("modules files copied successfully")       
    if lt == 'standalone':
        c=source+'\standalone\deployments'
        for ls in os.listdir(c):
            if ls == '()':
                a=c+'\()'
            if ls == '(SHORE)':
                a=c+'\(SHORE)'
            print(f"source - {a} , destination2 {destination2}")
            os.system("Robocopy "+a+" "+destination2+" /E /IS /IT /IM")   
            print("Deployments Files copied successfully")
