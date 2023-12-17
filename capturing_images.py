# this is the script for capturing the images for datasets
import os
import cv2
import time
print(f'{os.getcwd()}')
cam = cv2.VideoCapture(0)
path_cwd = 'V:/Open cv/'

try:
    if not os.path.exists(path_cwd + 'data'):
        os.makedirs(path_cwd + 'data')
except OSError:
    print('error in creating the direcotry')   

classes = 0
inp_num = -1
while(classes<=9):
    current_frame = 0
    os.makedirs(path_cwd+'data'+ '/' + str(classes))
    inp_num = input(f'press 1 is u r ready')
    

    if inp_num:
        time.sleep(2)  # Add a delay of 2 seconds
        while(current_frame<140):
            ret, frame = cam.read()
            if ret:
                name = path_cwd+'data'+ '/' + str(classes) + '/' + str(current_frame) + '.jpeg'
                cv2.putText(frame, str(current_frame), (25,25), cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0), 2)
                cv2.imshow('frame', frame)
                if cv2.waitKey(200) == ord('q'):
                    break
                
                cv2.imwrite(name, frame)
                print(f'createed:   {name}')
                current_frame+=1    
    classes+=1        
    inp_num =0                   
cam.release()
cv2.destroyAllWindows()           
# e f h i j k m n q r
