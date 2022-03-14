from pygame import mixer
import time
def sound(f1,stopper):
    mixer.init()
    mixer.music.load(f1)
    mixer.music.play()
    while 1:
        a=input("")
        if a==stopper:
            mixer.music.stop()
            break

if __name__=="__main__":
    init_water=45
    init_eyes=30
    init_exercise=150
    water=time.time()
    eyes=time.time()
    exercise=time.time()
    s=time.time()
    while 1:
        if time.time()-s==300:
            print("Press q to quit and c to continue ")
            a=input("")
            if a=="q":
                break  
        if time.time()-water >init_water:
            print("Water Alarm ")
            print("Press d to stop")
            sound("Water.mp3","d")
            water=time.time()
        elif time.time()-eyes >init_eyes:
            print("Do some eye exercise ")
            print("Press e to stop")  
            sound("Eyes.mp3","e")
            eyes=time.time()
        elif time.time()-exercise >init_exercise:
            print("Do some Physical Exercise ")
            print("Press p to stop ")
            sound("Physical.mp3","p")
            exercise=time.time()
        

       
            
    
