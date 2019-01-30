import mysql.connector
import random

#########################PUZZLES CHECKS############################                     

#Checks if there is a puzzle in target location
def checkforpuzzle():
    cur = db.cursor()
    sql = "SELECT Puzzle.ID FROM Puzzle join player where puzzle.locationid = player.locationid and completed = 2"
    cur.execute(sql)
    if cur.rowcount>=1:
        for row in cur.fetchall():
#            print("there's a puzzle here")
            puzzle=row[0]
    else:
        puzzle = "no"
    return puzzle

#Finds the right puzzle
def puzzlehappens(puzzle):
    if puzzle == "no":
            print("")
    elif puzzle==1:
            mikepuzzle()
    elif puzzle==2:
            stevepuzzle()
    elif puzzle==3:
            reggiepuzzle()
    elif puzzle==4:
            highwaypuzzle()
    elif puzzle==5:
            papaJohn()
    elif puzzle==6:
            phonepuzzle()
    elif puzzle==7:
            andyspuzzle()
    elif puzzle==8:
            computerpuzzle()
    elif puzzle==9:
            pepsilandiapuzzle()
    elif puzzle==10:
            ceopuzzle()
    elif puzzle==11:
            coinpuzzle()
    elif puzzle==12:
            reportpuzzle()
    elif puzzle==13:
            taxipuzzle()
    else:
        print("no such puzzle")
    return 
        
############################PUZZLES################################################
#FINAL BOSS BATTLE# ID = 10
def ceopuzzle():
    right=0
    wrong=0
    answer1="0"
    asnwer2="0"
    answer3="0"
    answer4="0"
    answer5="0"
    answer6="0"
    answer7="0"
    answer8="0"
    answer9="0"
    answer10="0"
    print("FINAL BATTLE WITH PEPSI CEO")
    print("")
    print("Its time for trial by fire")
    print("This is what it all comes down to")
    print("The final confrontation with the big bad blue, the evil itself, PEPSI CEO!!!")
    print("Pick a line you would like to use") 
    print("")
    print("")
    #Pepsi CEO opening lines
    print("Pepsi CEO: HAHAHAA YOU CANNOT STOP ME!!! I WILL MAKE THIS WORLD MINE")
    print("Pepsi CEO: I have my best men cracking the code, its only a matter of time till i will have access to what was supposed to be your last hope")
    print("")
    wins=0
    losses=0
    while right!=3 or wrong!=3 and wins==0 and losses==0:
        while right ==0 and wrong ==0:
            print("Pepsi CEO: So what are you doing here anyway, werent you supposed to be dealt with?")
            print("Your lines:")
            print("1. I was resurrected from the dead, Im gonna haunt you for the rest of your life!!!")
            print("2. Well things dont always go the way you want them to go")
            print("3. Im not sure what you told them to do but all they did was beat me up and throw me to garbage container?")
            print("")
            answer1=input("")
            if answer1=="1":
                print("1. I was resurrected from the dead, Im gonna haunt you for the rest of your life!!!")
                wrong=wrong+1
                print("")
                print("Pepsi CEO: Well go ahead then, one or two ghosts wont make any difference to me")
            elif answer1=="2":
                print("2. Well things dont always go the way you want them to go")
                print("")
                print("Pepsi CEO: Well thats easy to fix anyway, EVENTUALLY things always go my way")
                wrong=wrong+1
            elif answer1=="3":
                print("3. Im not sure what you told them to do but all they did was beat me up and throw me to garbage container?")
                print("")
                print("Pepsi CEO: Those imbecilles.. I did tell them to take the trashes out but in gang language that usually means taking care of business")
                print("Pepsi CEO: In evil corporation language: Dealing with problems, killing someone.. you get it?")
                print("You: yes yes yes i get it...")
                right=right+1
            else:
                print("Whatcha saying again?")
        while right ==1 and wrong ==0:
            print("Pepsi CEO anyway if you're here for the recipe you're way too late, we're already cracking the code")
            print("Pepsi CEO: Its only a matter of time before we can start mass producing it ourselves")
            print("")
            print("Your lines:")
            print("1. Sure go ahead. It wont get you anywhere anyway")
            print("2. No way. Im gonna take it by force if i have to!")
            print("3. How about we negotiate? I get the recipe and you get the description key? That way my boss wont be mad at me")
            print("")
            answer2=input()
            if answer2 == "1":
                print("1. Sure go ahead. It wont get you anywhere anyway")
                right=right+1
                print("Pepsi CEO: oh you're gonna give up that easily?")
                print("You: Or maybe I just have an ace up my sleeve")
                print("Pepsi CEO: Thats what they all say when they fall")
                print("You: Because you have been played. I thought you'd want to know how")
                print("Pepsi CEO: Me? played? unlikely?")
                print("You: Ye sure i didnt go to that dark alley on that exact time to get robbed on purpose or anything...")
                print("Pepsi CEO: .. what?")
                    
                print("")
            elif answer2 =="2":
                print("2. No way. Im gonna take it by force if i have to!")
                right=right+1
                print("Pepsi CEO: Sure go ahead. Good luck dealing with my goons when i press this red button, i'll make sure trashes are taken care of properly this time around")
                print("You: .....!")
                print("")
            elif answer2=="3":
                print("3. How about we negotiate? I get the recipe and you get the description key? That way my boss wont be mad at me")
                wrong=wrong+1
                print("Pepsi CEO: HAHAHHAA How about we dont. You have nothing of value for me!")
                print("You: ....but!...(damn my boss is so gonna kill me for this)")
            else:
                print("Me no understand!(parser)")
        while right ==0 and wrong ==2:
            print("Pepsi CEO: Now its time for you to leave. GOONS!")
            print("You: Are you sure you want to do that?")
            print("Pepsi CEO: and why wouldnt i want to do that?")
            print("")
            print("Your lines:")
            print("1. Because, i've always wanted to be a pepsi goon, i'd like to join you guys!")
            print("2. Because you have been played. I thought you'd want to know how")
            print("3. Its my liife. now or neever its my liife. now or neveeer")
            answer3=input("")
            if answer3 == "1":
                print("1. Because, i've always wanted to be a pepsi goon, i'd like to join you guys!")
                wrong=wrong+1
                print("Pepsi CEO: Just no. I can smell a dirty liar from miles away")
            elif answer3=="2":
                print("2. Because you have been played. I thought you'd want to know how")
                print("PEPSI CEO: And how's that?")
                print("You: The recipe you have been given is a trap. We meant you to steal it from us in the first place")
                print("Pepsi CEO: Is that so.. What proof do you have?")
                print("You: you can ask your favourite goon andy for more information regarding that")
                print("Pepsi CEO: And why would you tell me this")
                print("You: because i dont want to play it dirty like you guys. I just want honest competition. My heart bleeds red!(sherlock)")
                print("You: Aand because I think it might be toxic so alot of people could die if you dont have all the right pieces")
                print("Pepsi CEO: Oh..")
                right=right+1
            elif answer3=="3":
                print("3. Its my liife. i belieeve in better days, its my liife.")
                print("Pepsi CEO: SO WHY WOULD YOU SING NOW EXACTLY?")
                print("You: just checking if you were paying any attention to the world around you or if you were just talking to yourself")
                print("Pepsi CEO: Ha, ha very funny. I can assure you i can see alot")
                wrong=wrong+1
            else:
                print("Couldnt quite make sense of what you were trying to achieve?")
        while right ==0 and wrong ==1:
            print("Pepsi CEO: So are you here to witness our moment of triumph or just to get your ass handed to you again?")
            print("You: Perhaps im here to witness your downfall?")
            print("Pepsi CEO: Unlikely.")
            print("")
            print("Your lines:")
            print("1. No. for real. You might be ignorant but you cannot have missed the clear hints about whats happening in the world, havent you paid any attention? ")
            print("2. Don't you feel even a bit threatened by the fact that you dont even know what the recipe actually is, and that it actually requires a key?")
            print("3. Feel free to float in your own castle of clouds, I can assure you it will come raining down fast enough")
            answer4=input()
            if answer4=="1":
                print("1. No. for real. You might be ignorant but you cannot have missed the clear hints about whats happening in the world, havent you paid any attention? ")
                wrong=wrong+1
                print("")
                print("Pepsi CEO: Damn right I PAY FOR others to pay attention. And I pay more than anyone else can.")
                print("You: Or so you think?")
                print("Pepsi CEO: Or so i KNOW")
                print("You:...")
                print("Pepsi CEO: Trust me I dont play around")
            elif answer4=="2":
                print("2. Don't you feel even a bit threatened by the fact that you dont even know what the recipe actually is, and that it actually requires a key?")
                print("")
                print("Pepsi CEO: What do you mean? Of course its a new coca cola recipe?")
                print("You: What if its actually toxic and you start mass producing it?")
                print("Pepsi CEO: But thats more our style of feint...")
                print("You: Better think this through, its not me who's going to be responsible for all those deaths (Well actually i kinda would be for losing it in the first place.. but hey..!)")
                print("Pepsi CEO: ....")
                wrong=wrong+1
            elif answer4=="3":
                print("3. Feel free to float in your own castle of clouds, I can assure you it will come raining down fast enough")
                print("")
                print("Pepsi CEO: Empty words")
                print("You: Like your head?")
                print("Pepsi CEO: You fail to amuse me.")
                wrong=wrong+1
            else:
                print("Wait what?")              
        while right ==2 and wrong ==0:
            print("Pepsi CEO: So why exactly are you doing this?")
            print("Pepsi CEO: Why would you let us rob you on purpose, If the goons would have done their job properly you'd be dead!")
            print("You: Perhaps your goons are not as loyal as you think.")
            print("Pepsi CEO: But they're paid better than anyone!")
            print("You: That doesnt make them smart enough to not take even more money from elsewhere")
            print("Pepsi CEO: True. Those damn imbecilles cant do anything right. Nor do they know whats best for them")
            print("Pepsi CEO: Anyway. Its too late to stop us now, We're soon starting the mass production of the new recipe. You are too late to convince me otherwise")
            print("")
            print("Your lines:")
            print("1. Even if it means you will poison everyone that drinks it?, Thats the only reason im here. To stop this unjustice from happening for all those innocent people that have no place in this corporate war.")
            print("2. It actually tastes disgusting, I wouldnt want to drink it. People will try it once and then they will abandon it")
            print("3. I could actually give you the decryption key if you pay me enough so i can live luxurously for the rest of my life ")
            answer5=input()
            if answer5=="1":
                print("1. Even if it means you will poison everyone that drinks it?, Thats the only reason im here. To stop this unjustice from happening for all those innocent people that have no place in this corporate war.")
                right=right+1
                print("")
                print("Pepsi CEO: Its true that it would hurt our sales and possibly reputation.. hmm..")
                print("You: Is that so?")
                print("Pepsi CEO: Yes im starting to think it might not be worht the risk")
                print("You:...")
                print("Pepsi CEO: Yup i decided we're sticking with our guns here. take the recipe")
                #GOOD GUY EPILOGUE
                # GIB RECIPE TO MAIN CHAR
            elif answer5=="2":
                print("2. Don't you feel even a bit threatened by the fact that you dont even know what the recipe actually is, and that it actually requires a key?")
                print("")
                print("Pepsi CEO: What do you mean? Of course its a new coca cola recipe?")
                print("You: What if its actually toxic and you start mass producing it?")
                print("Pepsi CEO: But thats more our style of feint...")
                print("You: Better think this through, its not me who's going to be responsible for all those deaths (Well actually i kinda would be for losing it in the first place.. but hey..!)")
                print("Pepsi CEO: ....")
                wrong=wrong+1
            elif answer5=="3":
                print("3. I could actually give you the decryption key if you pay me enough so i can live luxurously for the rest of my life ")
                print("")
                print("Pepsi CEO: You would?")
                print("You: Yeah. You said you have money. I like nice things.. Do we see eye to eye?")
                print("Pepsi CEO: Indeed we do for the first time. Are you sure you werent a double agent to begin with?")
                print("You: That i will never know.")
                right=right+1
                #BAD GUY EPILOGUE
            else:
                print("What?")
        while right ==1 and wrong ==1:
            print("")
            print("Pepsi CEO: What exactly is your view in all this?")
            print("Pepsi CEO: How are you set to gain anything?")
            print("You: Not everything is about gaining something")
            print("Pepsi CEO: False, Only stupid and poor people think like that. Now spit it out")
            print("")
            print("Your lines:")
            print("1. Im just a lone man trying to do the right thing.")
            print("2. I am what im becoming again, I dont know what i was but I sure as will be something again, What i have to gain is what i am")
            print("3. I will gain dignity, honor and glory!")
            answer6=input()
            if answer6=="1":
                print("1. Im just a lone man trying to do the right thing.")
                print("")
                print("Pepsi CEO: What a bunch of bullc*ap")
                print("You: Really?")
                print("Pepsi CEO: Doing the right thing is almost as outdated as Coca Cola will be in few years ")
                print("You:...")
                print("Pepsi CEO: Yup i decided we're sticking with our guns here. take the recipe")
                wrong=wrong+1
            
            elif answer6=="2":
                print("2. I am what im becoming again, I dont know what i was but I sure as will be something again, What i have to gain is what i am")
                print("")
                print("Pepsi CEO: What is that supposed to mean?")
                print("You: That i lost my memory. Im regaining the old yet becoming a completely new person at the same time")
                print("Pepsi CEO: Sounds cool and all but i really dont have time for this")
                print("You: You were the one who asked the question)")
                print("Pepsi CEO: True enough, just not the answer what i was expecting")
                print("You: Life is full of suprises, just like the recipe you got")
                print("Pepsi CEO: hmm?")
                right=right+1
            elif answer6=="3":
                print("3. I will gain dignity, honor and glory!")
                print("")
                print("Pepsi CEO: You've been watching too many medieval movies recently")
                print("You: What do you mean?")
                print("Pepsi CEO: Because that sounds more like a meme than real life.")
                print("Pepsi CEO: Just go get your head checked after this all right?")
                wrong=wrong+1
            else:
                print("Derp, not understood")
        while right ==2 and wrong ==2:
            print("Pepsi CEO: Can you give me a reason to continue listening to your ramblings?")
            print("Pepsi CEO: Time is of the essence here")
            print("Pepsi CEO: Oh, I can already see it in front of my eyes.. the new 'Pepsi Nuke'")
            print("You: Well thats not far from truth")
            print("Pepsi CEO: So you can see it with your minds eye as well?")
            print("")
            print("Your lines:")
            print("1. Ye sure i can. maybe you should just hire me?")
            print("2. Well, since it might explode on your face, then yeah")
            print("3. Yup, just as radioactive as a nuke. Good luck")
            answer7=input()
            if answer7=="1":
                print("1. Ye sure i can. maybe you should just hire me?")
                print("")
                print("Pepsi CEO: Are you sure you have the vision?")
                print("You: I sure do, as long as the pay is right and i get to ride a blue lamborghini")
                print("Pepsi CEO: Seems like we see eye to eye, that is good.")
                print("You: So where's the contract (with devil itself)")
                print("Pepsi CEO: Maybe one of our slaves.. i mean secretaries could make one for you.")
                right=right+1
                #BAD ENDING
            
            elif answer7=="2":
                print("2. Well, since it might explode on your face, then yeah")
                print("")
                print("Pepsi CEO: Right. Funny,")
                print("You: So you get the joke?")
                print("Pepsi CEO: Yes, soda's tend to do that, now get out of my sight")
                print("You: but..!")
                print("Pepsi CEO: GOOOONS!")
                wrong=wrong+1
            elif answer7=="3":
                print("3. Yup, just as radioactive as a nuke. Good luck")
                print("")
                print("Pepsi CEO: Is it noticeable?")
                print("You: That your face melts? Yes most likely")
                print("Pepsi CEO: Thats not good for business....")
                print("Pepsi CEO: Take your recipe and go!")
                right=right+1
                #GOOD ENDING
            else:
                print("No, just no")
        while right ==2 and wrong ==1:
            print("Pepsi CEO: Im not sure what to expect.")
            print("Pepsi CEO: So you're telling me all these things")
            print("Pepsi CEO: But why should i believe you?")
            print("You: Well that is up to you, but its your money and company on the line")
            print("Pepsi CEO: Isnt that always the case when it comes to business?")
            print("You: Pretty sure its normally not this severe")
            print("")
            print("Your lines:")
            print("1. Im trying to help everyone, this situation is not good for anyone")
            print("2. I Believe we can come to a peaceful solution, this war needs to end")
            print("3. Its not good for business to poison your customers, and its not good for Coca Cola if it comes out it was actually their recipe")
            answer8=input()
            if answer8=="1":
                print("1. Im trying to help everyone, this situation is not good for anyone")
                print("")
                print("Pepsi CEO: Good luck with that, from my perspective you just seem desperate")
                print("You: Umm, thats not what it is")
                print("Pepsi CEO: Im just saying you,")
                print("You: Im actually trying to do good things!")
                print("Pepsi CEO: That's a classic example of a line liar would use.")
                wrong=wrong+1
                    
            
            elif answer8=="2":
                print("2. I Believe we can come to a peaceful solution, this war needs to end")
                print("")
                print("Pepsi CEO: No, this war is actually a decent alternative to dictatorship")
                print("You: But..!")
                print("Pepsi CEO: So if you're willing to blow up the Coca Cola company then suure im willing to listen?")
                print("You: NEVER!")
                print("Pepsi CEO: How dissapointing.")
                wrong=wrong+1
            elif answer8=="3":
                print("3. Its not good for business to poison your customers, and its not good for Coca Cola if it comes out it was actually their recipe")
                print("")
                print("Pepsi CEO: But i invested a lot to this robbery")
                print("You: Well your goons failed anyway so why pay them")
                print("Pepsi CEO: Yes.. I guess i could just pay someone to rob them back")
                print("Pepsi CEO: Here's the recipe just move along")
                right=right+1
                #GOOD ENDING
            else:
                print("Hallelujah, its in the numbers!")
            
        while right ==1 and wrong ==2:
            print("Pepsi CEO: I AM ALPHA, I AM  OMEGA")
            print("Pepsi CEO: WHY WOULD I LISTEN TO FILTHY WORMS LIKE YOU")
            print("Pepsi CEO: I SHALL BE KING OF THIS WORLD")
            print("You: Umm. Dude im gettin worried for your mental health")
            print("Pepsi CEO: Dont worry im being completely realistic")
            print("You: Right...")
            print("")
            print("Your lines:")
            print("1. I like cola, do you like cola?")
            print("2. I can give you some pills, should help you calm down a bit")
            print("3. Did you know Coca-Cola actually invented the cola drinks?")
            answer8=input()
            if answer9=="1":
                print("1. I like cola, do you like cola?")
                print("")
                print("Pepsi CEO: I like anything that makes me money")
                print("You: That wasnt the point")
                print("Pepsi CEO: It was")
                print("You: No!")
                print("Pepsi CEO: GOOOONS! This man doesnt understand.")
                wrong=wrong+1
                    
            
            elif answer9=="2":
                print("2. I can give you some pills, should help you calm down a bit")
                print("")
                print("Pepsi CEO: Thank you, but no need")
                print("You: Are you sure?")
                print("Pepsi CEO: Yes Im gonna get enough relaxation when I hear your bones cracking in front of me")
                print("You: OH...")
                print("Pepsi CEO: GOONS! FRESH MEAT!")
                wrong=wrong+1
            elif answer9=="3":
                print("3. Did you know Coca-Cola actually invented the cola drinks?")
                print("")
                print("Pepsi CEO: Yes. And we're still doing very well by stealing their recipes")
                print("You: Oh so thats where it comes from")
                print("Pepsi CEO: Yes.. Its a tradition. Even if we dont need to do it. We do it")
                print("You: I wish i had known beforehand.  (or did I?)")
                right=right+1
                #GOOD ENDING
            else:
                print("Me no understaando")
        if wrong==3:
            print("You died a rich man")
            losses=losses+1
        elif right==3:
            print("You did it, you saved Coca Cola company!!")
            wins=wins+1
        else:
            print("")
    return




#Pepsilandia Puzzle# ID = 9

def pepsilandiapuzzle():
    import random
    #INTRO
    print("You try to sneak inside pepsilandia thorough the exit")
    print("There are guards standing and watching that nobody sneaks inside")
    print("There are 4 guards. 2 on each side of the exit. Theyve spread out in to four lanes")
    print("Your objective is to avoid theyre line of sight")
    print("'Good luck'")
    #Muuttujat
    playerlane = 1
    player = "alive"
    guard1 = 0
    guard2 = 0
    guard3 = 0
    guard4 = 0
    stare = 0
    completed=0
    #loop starts
    while player != "Caught" and completed!=1:
        print("")
        print("")
        stare=random.randint(1,4)
        print("Guards starting to look:")
        if stare==1 and guard1==0:
            print("You see guard nro.1 turning his head towards you")
            guard1=guard1+1
        if stare==2 and guard2==0:
            guard2=guard2+1
            print("You see guard nro.2 turning his head towards you")
        if stare==3 and guard3==0:
            guard3=guard3+1
            print("You see guard nro.3 turning his head towards you")
        if stare==4 and guard4==0:
            print("You see guard nro.4 turning his head towards you")
            guard4=guard4+1
        print("")
    #Guard1 distance
        print("Guards that you see are turning towards your location:")
        if guard1 == 1:
            print("Guard nro.1 is not looking at you")
        if guard1 == 2:
            print("Guard nro.1 is starting to look at you, but he still hasent spotted you")
        if guard1 == 3:
            print("Guard nro.1 is almost staring at you!")
        
    #Guard2 distance
        if guard2 == 1:
            print("Guard nro.2 is not looking at you")
        if guard2 == 2:
            print("Guard nro.2 is starting to look at you, but he still hasent spotted you")
        if guard2 == 3:
            print("Guard nro.2 is almost staring at you!")
        
    #Guard3 distance
        if guard3 == 1:
            print("Guard nro.3 is not looking at you")
        if guard3 == 2:
            print("Guard nro.3 is starting to look at you, but he still hasent spotted you")
        if guard3 == 3:
            print("Guard nro.3 is almost staring at you!")
       
    #Guard4 distance
        if guard4 == 1:
            print("Guard nro.4 is not looking at you")
        if guard4 == 2:
            print("Guard nro.4 is starting to look at you, but he still hasent spotted you")
        if guard4 == 3:
            print("Guard nro.4 is almost staring at you!")
        print("")
    #Guard moving
        if guard1>=1:
            guard1=guard1+1
        if guard2>=1:
            guard2=guard2+1
        if guard3>=1:
            guard3=guard3+1
        if guard4>=1:
            guard4=guard4+1
    #THEY RESET WHEN THEY LOOK PAST YOU
        if guard1==4:
            guard1=0
        if guard2==4:
            guard2=0
        if guard3==4:
            guard3=0
        if guard4==4:
            guard4=0
    #Player move parser
        print("Your current location:")
        print("You are standing next to guard",playerlane,"")
        print("")
        print("You can go forward, backwards and stop")
        decision=input("What would you like to do?")
        decision=decision.lower()
        if decision =="stop":
            playerlane=playerlane+0
            print("You stay still")
        elif decision =="forward":
            if playerlane<=3:
                playerlane=playerlane+1
                print("You move forward towards the other side of the exit")
            else:
                print("You can't move any further that way")

        elif decision =="backwards":
            if playerlane>=2:
                playerlane=playerlane-1
                print("You go back towards the way you originally came from")
            else:
                playerlane=playerlane-1
                print("You exit the area without completing the task")
        else:print("I didnt quite understand?")
    #Checking if any of the guards line of sight hits the player
        if guard1==3 and playerlane==1:
            player="Caught"
            print("Oh no a guard nro.1 spots you!, You see a fist flying towards your head?!??!")
        elif guard2==3 and playerlane==2:
            player="Caught"
            print("Oh no guard nro.2 spots you!, He roughly escorts you out?!??!")
        elif guard3==3 and playerlane==3:
            player="Caught"
            print("Oh no guard nro.3 spots you!, He grabs our shirts collar and drags you out?!??!")
        elif guard4==3 and playerlane==4:
            player="Caught"
            print("Oh no guard nro.4 spots you!, He politely asks you leave?!??!")
        if playerlane == 4:
            completed=completed+1
            print("You made it all the way to the other side of the exit")
        print("")
        print("")
    return


    
    
    

#TAXI ID = 13

def taxipuzzle():
    taxicoupon=1
    cur=db.cursor()
    sql="SELECT item.playerid from item where ID=4"
    cur.execute(sql)
    if cur.rowcount>=1:
        for row in cur.fetchall():
            if taxicoupon== row[0]:
                print("Where do you wanna ride my man? , hop on in! (go east)")
                setLocationAllowed(3,5)
                
                completePuzzle(13)
            else:
                print("No cash, no credit equals no ride.")
                returnToPreviousLocation(3)
    else:
        print("ERROR")
    return

#Haralds coin check ID = 11
def coinpuzzle():
    coin=1
    cur=db.cursor()
    sql="SELECT item.playerid from item where ID=8"
    cur.execute(sql)
    if cur.rowcount>=1:
        for row in cur.fetchall():
            if coin == row[0]:
                print("You did it my man!")
                
                completePuzzle(11)
                setLocationAllowed(3,4)
            else:
                print("Yarr go retrieve my coin you bum")
                setLocationAllowed(3,6)
                returnToPreviousLocation(3)
    else:
        print("ERROR")
    return
        

#Reporting the crime at the policestation# ID = 12
def reportpuzzle():
    name="Morgan Captive"
    inputname="whatever"
    print("Lazy looking old police officer greets you when you enter the station")
    print("Police officer: Welcome to policestation, what can i do for ya")
    print("His eyes widen when he sees you")
    goback=0
    while name != inputname and goback !=1:
        print("Police officer: 'So ya got robbed eh?'")
        print("Police officer: 'Well im gonna run through the routine check'")
        print("Police officer: 'So please answer my questions truthfully and as precicely as you can'")
        print("Police officer: 'Ok lets start off with your name. what is it?")
        inputname=str(input(""))
        if name == inputname:
            print("Police officer: 'Well that wasnt so hard now was it'")
            print("Police officer: 'Now then lets continue and fill out the other details'")
            print("..........")
            print("........")
            print(".....")
            print("Police officer: 'Ok that should do it , the crime has been reported. Have a good day sir")
            print("Police officer: 'Actually wait a second, we seem to have things that belong to you, some friendly person found them from the other side of the city and brought them to us'")
            print("Police officer: 'now you should be good to go'")
            goback=goback+1
            completePuzzle(12)
            takeItem('Phone')
            takeItem('Wallet')
            givememory(6)
            setLocationAllowed(7,5)
            setLocationAllowed(5,11)
            givememory(8)
        else:
            print("")
            print("Police officer: 'Are you kidding me? This is police station not some circus'")
            print("Police officer: 'What do you mean you cant remember it? Everyone has a name and everyone knows their name!'")
            print("Police officer: 'Now get lost you clown, go joke around somewhere else we are actually busy here!'")
            print("")
            goback=goback+1
            setLocationAllowed(7,10)
            givememory(3)
    return

#Computer use for the workplace computer## ID = 8
def computerpuzzle():
    us = "Morgan"
    pw = "capta1nc0la"
    username = "Not"
    password = "nope"
    #loop starts
    print("Starting up the computer")
    print("")
    while username != us or password != pw:
        print("Welcome to Coca Cola network")
        print("Take a refreshing drink and wait for your account details to load up")
        print("")
        print("Loading....")
    
        username = str(input("Please enter your employee username here "))
        password = str(input("Please enter your employee password "))
        if username == us:
            print(" Username confirmed")
        else:
            print(" Username is not correct")
        if password ==  pw:
            print(" Password confirmed")
        else:
            print("Your password is not correct")
        if password == pw and username ==us:
            print("Logging in to your account.")
            print("Welcome back to Coca Cola mr. Morgan Captive")
            print("Accessing your account")
            print("Accessing your most recent personal notes")
            print("Report #1")
            print("We are closing in on the final breakthrough, still having some trouble with toxicity levels")
            print("but they should be neutralised by adding more sugar like everything else")
            print("")
            print("Report #2")
            print("We finally finished the recipe, it was just as we thought, just needed to add more sugar")
            print("")
            print("Report #3")
            print("So the new recipe is ready, our competitors have pretty good sources so they should be aware of this as well. we should create some sort of insurance policy")
            print("")
            print("Report #4")
            print("So the conclusion we came to was that we need some sort of description key to the recipe, so even if it falls to wrong hands it should still be tough to use without the correct methods")
            print("Encryption key is saved to my personal files and only mine, And i will never travel with it on me")
            completePuzzle(8)
            givememory(10)
            setLocationAllowed(12,14)
            print("You have gained a memory!")
            
            
            
    return


#Papa John's puzzle
def papaJohn():
    print("Old man: 'Well hello there!' Have you seen my turtle? .. Hey, wait a minute!" +"\n" +"I know you don't I? You're the turtle cleaner! Quick, find my dear shelly before he starves to death'")
    input()
    print("Me: I better do what the old guy tells me. I don't want him to get a stroke relax his bowels while I'm here")
    input()
    print("Old man: I think I saw him in one of these pizza boxes here")
    bingo = random.randint(1, 5)
    guess = 0
    print("There's 5 slimy pizza boxes laying on the floor. Choose to open one by typing a number 1-5")
    while guess != bingo:
        input()
        guess=int(input("Open pizza box number:"))
        if guess == 1 and guess != bingo:
            print("Fart! In your face!")
        elif guess == 2 and guess != bingo:
            print("A cat jumps out the pizza box and queefs on your face")
        elif guess == 3 and guess != bingo:
            print("You're opening the pizza box and see a glance of something big and black just before Papa John rushes in and closes the pizza box in front of you.")
            input()
            print("[press enter]")
            print("No! Don't touch that one! That's just a souvenir... from when I was travelling in Europe... [nervous laugh]")
        elif guess == 4 and guess != bingo:
            print("There's still a few slices left here with some mold on them.")
            input()
            print("[press enter]")
            print("Papa John sneaks behind you and grabs a slice and stuffs his face")
            input()
            print("[press enter]")
            print("Papa John: 'Old pizza is still pizza'")
        elif guess == 5 and guess != bingo:
            print("There's just a framed photo of putin here covered in cheese splashes")
        elif guess == bingo:
            print()
            print("Bingo! You grab the turtle rolled in pizza slice and hand him to Papa John")
            input()
            print("[press enter]")
            print("Papa John: 'Bless you son! Here, take this as a token of graditude'")
            print()
            print("[press enter]")
            print("[Papa John hands you a taxi coupon. Some cheese catches your hand while he hands it to you.]")
            input()
            print("[press enter]")
            print("There seems to be some sort of piece of paper stuck to it, looks like some sort of weird notes")
            takeItem('Taxi coupon')
            takeItem('Piece of paper')
            completePuzzle(5)
            returnToPreviousLocation(4)
        else:
            print("Enter a correct pizza box number")
    return


#Phone puzzle ID = 6 # Activated by parser##
def phonepuzzle():
    us = "captaincola"
    pw = "l1qu1d"
    username = "Not"
    password = "nope"
    #loop starts
    print("CPhone is starting up")
    while username != us or password != pw:
        print("Accessing email. just a moment...")
        print("")
        username = str(input("Please enter your username here "))
        password = str(input("Please enter your password "))
        givememory(id)
        print("You've gained a memory!")
        if username == us:
            print(" Username confirmed")
        else:
            print(" Username wrong")
        if password ==  pw:
            print(" Password confirmed")
        else:
            print("Your password is wrong")
        if password == pw and username ==us:
            print("Logging in to your email.")
            print("Welcome back mr Morgan Captive")
            print("Accessing latest emails")
            print("From mr Jack daniels (Jack.D@Whiskers.dom)")
            print("Hey man lets go have a drink someday, I miss the good old days!")
            print("")
            print("From mr. John Jackson(Jackson.J@Coca-Cola.cola)")
            print("Morgan please bring the package to me when you recieve it, straight to our main offices at the enterprise avenue")
            setLocationAllowed(5,11)
            givememory(8)
            print("(Enterprise avenue location unlocked)")
            print("")
            print("From mr.Secret Agent(Secret.A@unknown.dot)")
            print("Hey Morgan. Im gonna bring you the package from our lab at 5amt tuesday morning.")
            print("please be waiting for me at the location X")
            print("")
            print("End of recent emails")
            completePuzzle(6)
            print("You have gained a memory!")
            
                  
            
    return

    

# Andy the pepsi goon puzzle ID = 7#
def andyspuzzle():
    right=0
    wrong=0
    answer1="0"
    asnwer2="0"
    answer3="0"
    answer4="0"
    answer5="0"
    print("Duel with Andy")
    print("")
    print("Well well well, so seems like it was good old police officer andy who mugged me")
    print("With the help of his friends of course, and now he's trying to stop me again")
    print("I wonder how i could convince him to leave me alone?")
    print("Pick a line you would like to use") 
    print("")
    print("")
    #Andys opening lines
    print("Andy: So here you are again, didn't learn from your past mistakes did you?")
    print("Andy: Right, you cannot remember anything... HAHAHAHA life can be so funny sometimes")
    print("")
    completed=0
    while right!=2 or wrong!=2 and completed==0:
        while right ==0 and wrong ==0:
                print("Your lines:")
                print("1. I can actually remember just fine, i was just testing you")
                print("2. I dont know what you're talking about?")
                print("3. But you certainly ain't funny, no wonder women dont like you")
                print("")
                answer1=input("")
                if answer1=="1":
                    print("1. I can actually remember just fine, i was just testing you")
                    right=right+1
                    print("")
                    print("Andy:.. Say what? You're lying!")
                elif answer1=="2":
                    print("2. I dont know what you're talking about?")
                    print("")
                    print("Andy: Of course you don't you probably have 0 clue about anything")
                    wrong=wrong+1
                elif answer1=="3":
                    print("3. But you certainly ain't funny, no wonder women dont like you")
                    print("")
                    print("Andy: *OUTRAGE* YOU LIL PUNK IM GONNA KICK YOUR ARSE SO HARD YOU CANT REMEMBER HOW IT FEELS TO SIT EVEN IF YOU RECOVER YOUR MEMORY")
                    print("Andy: BACK IN MY DAY I MADE MANY A MAIDEN LOOK MY WAY, THEY WERE ALL OVER ME I TELL YA")
                    wrong=wrong+1
                elif answer1=="bye":
                    bye=bye+1
                else:
                    print("Couldnt quite make sense of your answer?")
        while right ==1 and wrong ==0:
            print("Andy: Well then why didn't you just give us the package then?")
            print("Andy: Something smells fishy here.")
            print("")
            print("Your lines:")
            print("1. I was just kidding. I just wanted to see if you'd actually be dumb enough to actually believe that! Turnst out you are!! Great success.")
            print("2. Why would i want to make myself look like an obvious criminal?, I made a deal with your boss to actually let you rob me, I lured you guys to the alley on purpose, It was all done to fool my boss")
            print("3. I wanted to be the one to give it to your boss but you robbed me before i could.")
            print("")
            answer2=input()
            if answer2 == "1":
                    print("1. I was just kidding. I just wanted to see if you'd actually be dumb enough to actually believe that! Turnst out you are!! Great success.")
                    wrong=wrong+1
                    print("Andy: You mothe*r noncoladrinker how dare you, Back in my day we actually used to show some respect to our elders")
                    print("You: Must've been a while back, I doubt anyone would have shown you any respect even back 'in your days' you lazy and greedy bum")
                    print("Andy: OH YOU SHUT UP, YOU KNOW NUTHIN' MORGAN NOT SO FREE MAN")
                    print("")
            elif answer2 =="2":
                      print("2. Why would i want to make myself look like an obvious criminal?, I made a deal with your boss to actually let you rob me, I lured you guys to the alley on purpose, It was all done to fool my boss")
                      right=right+1
                      print("Andy:... That actually makes sense.. so are you going to cola offices to find the missing piece now?")
                      print("You: Yes thats exactly why im going there, now can you let me through")
                      print("Andy: Sure man sure, just remember to put a good word about me to the guys that are higher up the ladder")
                      print("")
                      completed=completed+1
                      completePuzzle(7)
                      setLocationAllowed(11,13)
                      print("Coca cola center unlocked")
                      givememory(10)
                      setLocationAllowed(12,14)
                      returnToPreviousLocation(11)
                      
            elif answer2=="3":
                      print("3. I wanted to be the one to give it to your boss but you robbed me before i could.")
                      wrong=wrong+1
                      print("Andy: Aaand why would i let you through even if that was true? More glory and money for me the better")
                      print("You: ....")
            else:
                      print("Umm excuse me? what were you trying to say?")
        while right ==0 and wrong ==1 and bye==0:
            print("Andy: So what are you on about anyway. Just move along, before i arrest you")
            print("")
            print("Your lines:")
            print("1. I wanted to let you in on a secret:... You're probably the ugliest man i have ever met")
            print("2. Im actually here to retrieve the hidden information for you guys, i've been hired as double agent")
            print("3. Why would you not want to let me in? I can make it worth your while.")
            answer3=input("")
            if answer3 == "1":
                    print("1. I wanted to let you in on a secret:... You're probably the ugliest man i have ever met")
                    wrong=wrong+1
                    print("Andy: YOU ARE SO DEAD, I TELL YA, NEVER SHOW YOUR FACE IN FRONT OF ME AGAIN")
            elif answer3=="2":
                    print("2. Im actually here to retrieve the hidden information for you guys, i've been hired as double agent")
                    print("Andy: Oh really? I dont believe you.")
                    right=right+1
            elif answer3=="3":
                    print("3. Why would you not want to let me in? I can make it worth your while.")
                    print("Andy: HAHA Do you honestly think you could possibly pay me more than my current employer??!! You're either delusional or just stupid")
                    print("Andy: Now get lost you're wasting my time here")
                    wrong=wrong+1
            else:
                    print("Couldnt quite make sense of what you were trying to achieve?")
        while right ==1 and wrong ==1:
            print("Andy: So you're basically telling me you actually remember something even though you didnt even know your name at first, when we met earlier?")
            print("Andy: You seem like a mess to me")
            print("")
            print("Your lines:")
            print("1. I was just playing games with you earlier, I actually planned the robbery myself and gave you the package out of my own free will. Your boss is paying me money.")
            print("2. I was just a little confused earlier. Im actually your boss and I DEMAND You step away from the door!")
            print("3. I like donuts, do you? You certaily look like you do")
            answer4=input()
            if answer4=="1":
                      print("1. I was just playing games with you earlier, I actually planned the robbery myself and gave you the package out of my own free will. Your boss is paying me money.")
                      right=right+1
                      print("")
                      print("Andy: Well damn you. I didnt think i could be fooled anymore at this day and age. So you're here to retrieve the missing information then?")
                      print("You: Yup thats what im here to do. Was fun knowing you")
                      print("Andy: Hold on.....!!!!")
                      print("Andy: Remember to mention how helpful i was to you during your mission to the higher ups. I might get an added bonus")
                      print("You: sure sure. I'll mention it, you can be sure of that")
                      completed=completed+1
                      completePuzzle(7)
                      setLocationAllowed(11,13)
                      print("Coca cola center unlocked")
                      returnToPreviousLocation(11)
            elif answer4=="2":
                      print("2. I was just a little confused earlier. Im actually your boss and I DEMAND You step away from the door!")
                      print("")
                      print("Andy: Like hell you are. We must've hit your head even harder than we thought. You're just rambling like a madman at this point")
                      print("Andy: Get out of my sight you madman")
                      wrong=wrong+1
            elif answer4=="3":
                      print("3. I like donuts, do you? You certaily look like you do")
                      print("")
                      print("Andy: OH SO YOU'RE RESORTING TO FAT MAN JOKES NOW, VERY FUNNY!")
                      print("Andy: If i was a bit younger i'd show you what these big bones are good for, now scram")
                      wrong=wrong+1
            else:
                    print("Wait what?")
       
    return


        
# HIGHWAY PUZZLE ID = 4 #

def highwaypuzzle():
    import random
    #INTRO
    print("Welcome to the highway of hell")
    print("This is one of the busiest roads in the country")
    print("There are 4 lanes and cars approaching you from all directions.")
    print("Your objective is to retrieve Haralds coin from the other side of the road")
    print("'Good luck'")
    #Muuttujat
    playerlane = 1
    coin = 0
    player = "alive"
    car1 = 0
    car2 = 0
    car3 = 0
    car4 = 0
    appears = 0
    decision = "lol"
    #loop starts
    while coin != 2 and player != "Dead" and decision !="leave":
        print("")
        print("")
        appears=random.randint(1,4)
        print("New approaching cars:")
        if appears==1 and car1==0:
            print("You see a new car approaching on lane 1")
            car1=car1+1
        if appears==2 and car2==0:
            car2=car2+1
            print("You see a new car approaching on lane 2")
        if appears==3 and car3==0:
            car3=car3+1
            print("You see a new car approaching on lane 3")
        if appears==4 and car4==0:
            print("You see a new car approaching on lane 4")
            car4=car4+1
        print("")
    #CAR1 distance
        print("Cars that you see are closing in on your location:")
        if car1 == 1:
            print("Car on lane 1 is still far away")
        if car1 == 2:
            print("Car on lane 1 is closing in, but still some distance away")
        if car1 == 3:
            print("Car on lane 1 is right next to you!")
        
    #CAR2 distance
        if car2 == 1:
            print("Car on lane 2 is still far away")
        if car2 == 2:
            print("Car on lane 2 is closing in, but still some distance away")
        if car2 == 3:
            print("Car on lane 2 is right next to you!")
        
    #CAR3 distance
        if car3 == 1:
            print("Car on lane 3 is still far away")
        if car3 == 2:
            print("Car on lane 3 is closing in, but still some distance away")
        if car3 == 3:
            print("Car on lane 3 is right next to you!")
       
    #CAR4 distance
        if car4 == 1:
            print("Car on lane 4 is still far away")
        if car4 == 2:
            print("Car on lane 4 is closing in, but still some distance away")
        if car4 == 3:
            print("Car on lane 4 is right next to you!")
        print("")
    #Player move parser
        print("Your current location:")
        print("You stand on lane",playerlane,"")
        print("")
        if playerlane == 4 and coin!=1:
            print("You can see the coin on the ground right next to you")
        print("")
        print("You can go forward, backwards, stop and pick up coin when you reach the other side of the road")
        decision=input("What would you like to do?")
        if decision =="stop":
            playerlane=playerlane+0
            print("You stay still")
        elif decision =="forward":
            if playerlane<=3:
                playerlane=playerlane+1
                print("You move forward towards the other side of the road")
            else:
                print("You can't move any further that way")

        elif decision =="backwards":
            if playerlane>=2:
                playerlane=playerlane-1
                print("You go back towards the way you originally came from")
            else:
                playerlane=playerlane-1
                print("You exit the area without completing the task")
        elif playerlane==4 and decision =="pick up coin" and coin ==0:
            coin=coin+1
            print("")
            print("")
            print("")
            print("")
            print("You pick up the coin from the other side of the road, now you should go back")
        elif playerlane==1 and decision=="leave":
            print("you're leaving")
        elif playerlane!=1 and decision=="leave":
            decision="notleave"
        else:
            print("I didnt quite understand?")
    #Checking if any of the cars hits the player
        if car1==3 and playerlane==1:
            player="Dead"
            print("Oh no you got hit by a car!, you see your head flying off, arent you embarrassed?!??!")
            print("Just kidding you just got knocked out and returned to other side of the road")
        if car2==3 and playerlane==2:
            player="Dead"
            print("Oh no you got hit by a car!, you see your head flying off, arent you embarrassed?!??!")
            print("Just kidding you just got knocked out and returned to other side of the road")
        if car3==3 and playerlane==3:
            player="Dead"
            print("Oh no you got hit by a car!, you see your head flying off, arent you embarrassed?!??!")
            print("Just kidding you just got knocked out and returned to other side of the road")
        if car4==3 and playerlane==4:
            player="Dead"
            print("Oh no you got hit by a car!, people can see your head flying off,arent you embarrassed?!??!")
            print("Just kidding you just got knocked out and returned to other side of the road")
            
    #Checking if player reached the end with coin in his pocket and giving appropriate rewards
        if playerlane == 1 and coin == 1:
            coin= coin+1
            print("You made it all the way to the other side with the coin.. whooh..")
            completePuzzle(4)
            takeItem('Coin')
            
    #Cars moving
        if car1>=1:
            car1=car1+1
        if car2>=1:
            car2=car2+1
        if car3>=1:
            car3=car3+1
        if car4>=1:
            car4=car4+1
    #LANES RESET WHEN CARS GO PAST YOU SO NEW ONES CAN SPAWN TO THE SAME LANE
        if car1==4:
            car1=0
        if car2==4:
            car2=0
        if car3==4:
            car3=0
        if car4==4:
            car4=0
        print("")
        print("")
    if player=="dead" or decision=="leave":
        print("leaving")
    return
#steve ID = 2 
def stevepuzzle():
    
    light = 0
    print("Phones have lights.")
    while light!=1:
        steve = input()

        if steve == "phones have lights":
            light=light+1
            print("phones have lights!")
            completePuzzle(2)
            takeItem('pants and hat')
            checkbumpuzzles()
            returnToPreviousLocation(2)
        else:
            print("phones have lights?")
            returnToPreviousLocation(2)
    return




#Reggie ID = 3
def reggiepuzzle():

    jesus = 0
    devil = 0
    

    while jesus != 1 and devil !=1:
        print("I am a carpenter, i was born on chirstmas eve, on easter i go to sleep on friday and wake up on sunday and jews hate me.")
        reggie = input("Who am i? ")
        if reggie == "jesus":
            jesus=jesus+1
            print("You truly are a believer, may gods light shine upon your adventure.")
            completePuzzle(3)
            takeItem('shoes and socks')
            checkbumpuzzles()
            returnToPreviousLocation(2)
            print("")
            print("")
        elif reggie =="bye":
            devil=devil+1
            returnToPreviousLocation(2)
            print("")
            print("")
        else:
            print()
    
    return



#Mike ID = 1
def mikepuzzle():
    #intro
    print("Beat mike in rock, paper, scissors.")
    print("Best of three matchup.")
    #arvot
    import random

    hand = 0
    rock = 1
    paper = 2
    scissor = 3
    hook = 4
    bye = 5
    
    
    
   
    Mike = 0
    Morgan = 0
    bye = 0
    mikewins = 0
    morganwins = 0
    byewins = 0

    while mikewins != 1 and morganwins != 1 and byewins !=1:
        hand = random.randint(1,4)
        player = str(input())
        if hand == 1 and player == str("rock"):
            print("Tie, rock vs rock")
        elif hand == 2 and player == str("rock"):
            Mike = Mike+1
            print("You lose, paper")
        elif hand == 3 and player == str("rock"):
            Morgan = Morgan+1
            print("You win, scissor")
        elif hand == 4 and player == str("rock"):
            Mike = Mike+1
            print("You lose hook beats everything.")
        elif hand == 2 and player == str("paper"):
            print("Tie, paper vs paper")
        elif hand == 3 and player == str("paper"):
            Mike = Mike+1
            print("You lose, scissors")
        elif hand == 1 and player == str("paper"):
            Morgan = Morgan+1
            print("You win,rock")
        elif hand == 4 and player == str("paper"):
            Mike = Mike+1
            print("You lose hook beats everything.")
        elif hand == 3 and player == str("scissor"):
            print("Tie, scissors vs scissors")
        elif hand == 1 and player == str("scissor"):
            Mike = Mike+1
            print("You lose, rock")
        elif hand == 2 and player == str("scissor"):
            Morgan = Morgan+1
            print("You win, paper")
        elif hand == 4 and player == str("scissor"):
            Mike = Mike+1
            print("You lose hook beats everything.")
        elif player == str("bye"):
            bye=bye+1
            print("Byebye!")
            
        else:
            print("rock, paper or scissor, do you understand.")
        if Mike == 2:
            mikewins = mikewins+1
            print("Better luck next time. if you want to play again gimmme your best 'yaar'.")
            print("Player: yaaaar...")
            returnToPreviousLocation(2)
        elif Morgan == 2:
            morganwins = morganwins+1
            print("Well done. If we ever get to play again i need to cheat more.")
            completePuzzle(1)
            takeItem('hoodie and sunglasses')
            checkbumpuzzles()
            returnToPreviousLocation(2)
        elif bye == 1:
            byewins = byewins+1
            returnToPreviousLocation(2)
    return


    
    
###################/PUZZLES##########################################

def printHelp():
    print("Type 'inventory' to access your stuff.")
    print("Type 'memory' to access your memories.")
    print("Type 'Look around' to see whats around you.")
    print("You can move with 'east','north','south' and 'west' commands")
    print("You can also go 'Up' and 'Down' in some places")
    print("Type 'quit' to exit game.")
    print("type 'talk to <name>' to talk to people")
    print("Type 'bye' to stop talking to people")
    print("You may also use some items 'use <item>'")
    return
    
def printIntro():
    print("-=|Sparkling Memories|=-")
    print("")
    print("Created by Dani, Roni and Sakari.")
    print("This is a tale of madness, greed and corruption in the modern world.")
    print("Or at least our version of it.")
    print("Prepare yourself for the journey of your lifetime.")
    print("")
    print("")
    return

#siirtää itemin omaan inventoryyn ja poistaa lokaatiosta
def takeItem(item):
    cur = db.cursor()
    sql = "UPDATE item SET locationID=NULL, playerID=1 WHERE name="+"'" +item +"'"
    cur.execute(sql)
    if cur.rowcount>=1:
        print()
        print(item, "Has been added to your inventory")
        print()
    else:
        print("Can't take that")
    return
    
#hakee kaikki npc:t jotka sijaitsevat funktiooon syötetyssä locationid:ssä
def getNpcInLocation(locationid):
    cur = db.cursor()
    sql = "SELECT name from npc where npc.locationid = "+locationid 
    cur.execute(sql)
    if cur.rowcount>=1:
        print("I can see some people of importance in this location: ")
        for row in cur.fetchall():
            print(row[0] + ", ")
    else:
              print("There's no-one here!")
    return

#hakee kaikki npc:t pelaajan lokaatiosta
def getNPCinPLAYERlocation():
    cur = db.cursor()
    sql = "SELECT name from npc join player where npc.locationid = player.locationid"
    cur.execute(sql)
    if cur.rowcount>=1:
        print("I can see some people of importance in this location: ")
        for row in cur.fetchall():
            print(row[0] + ", ")
    else:
              print("You are alone")
    return

#hakee kaikki itemit jotka sijaitsevat funktiooon syötetyssä locationid:ssä
def getItems(locationid):
    cur = db.cursor()
    sql = "SELECT name from item where item.locationid ="+locationid
    cur.execute(sql)
    if cur.rowcount>=1:
        print("There seems to be something here")
        for row in cur.fetchall():
            print(row[0] +", ")
    else:
            print("There is no items worth noting in your current location")
    return

#tulostaa inventoryn sisällön
def inventory():
    cur = db.cursor()
    sql = "SELECT name FROM item WHERE playerID=1"
    cur.execute(sql)
    if cur.rowcount>=1:
        print("You posess the following items: ")
        for row in cur.fetchall():
            print(row[0] + ", ")
    else:
            print("Your inventory is empty.")
    return

#Hakee ja tulostaa annetun itemin tarkemmat tiedot
def itemDetails(item):
    cur = db.cursor()
    sql = "SELECT Info from item join player where item.name = ""'"+item+"'" "And item.playerid = player.id"
    cur.execute(sql)
    if cur.rowcount>=1:
        print("You inspect the item more closely:")
        for row in cur.fetchall():
            print(row[0] +", ")
    else:
        print("You possess no such item")
    return

#tulostaa pelaajan hallussa olevat muistot
def memory():
    cur = db.cursor()
    sql = "SELECT name FROM memory WHERE playerID=1"
    cur.execute(sql)
    if cur.rowcount>=1:
        print("You have the following memories: ")
        for row in cur.fetchall():
            print(row[0] + ", ")
    else:
            print("You remember nothing")
    return

#Hakee ja tulostaa annetun memoryn tarkemmat tiedot
def remembermemory(memory):
    cur = db.cursor()
    sql = "SELECT Info from memory join player where memory.name = ""'"+memory+"'" + " And memory.playerid = player.id"
    cur.execute(sql)
    if cur.rowcount>=1:
        print("You close your eyes and think about your past")
        for row in cur.fetchall():
            print(row[0] +", ")
    else:
        print("You have no such memories")
    return

#hakee pelaajan senhetkisen location id:n
def getLocation():
    cur = db.cursor()
    sql = "SELECT locationID FROM player"
    cur.execute(sql)
    result = cur.fetchall()
    return result[0][0]

#tulostaa pelaajan sijainnin ja sijaintikuvauksen
def printLocation():
    cur = db.cursor()
    sql = "SELECT name, info FROM location join player WHERE player.locationID = location.ID"
    cur.execute(sql)
    result = cur.fetchall()
    print(result[0][0])
    print("")
    print("Location Info:  "+ result[0][1])
    print("")
    return

def move(locto, direction):
    if locto != 0:
        cur = db.cursor()
        sql = "UPDATE player SET locationID=" +str(locto)
        cur.execute(sql)
        if cur.rowcount>=1:
            print()
            print("You move "+direction)
        else:
            print("error moving", locto, direction)
    elif locto == 0:
        print("Can't move that way")
    return

#hakee kohdesijainnin id:n liikkumissuunnan perusteella
def getLocationTo(loc, direction):
    cur = db.cursor()
    sql = "SELECT locationTo FROM locationallowed WHERE locationFrom=" +str(loc) + " AND direction=" + "'" +str(direction)+ "'"
    cur.execute(sql)
    if cur.rowcount>=1:
        result1 = cur.fetchall()
        result = result1[0][0]
#        print(loc, direction, "->", result)
    else:
#        print(loc, direction, "doesnt exist")
        print("Can't move that way")
        result = 0
    return result

#Hakee mahdolliset eventit pelaajan sijainnista
def eventhappening():
    cur = db.cursor()
    sql = "SELECT Info from events join player where events.completed = 2 and events.locationid =  player.locationid"
    sql2 = "Update events set events.completed = 1 where events.completed = 2 and events.locationid =(select player.locationid from player)" 
    cur.execute(sql)
    if cur.rowcount>=1:
        print()
#        print("Event:")
#        print()
        for row in cur.fetchall():
            print(row[0] + ", ")
            cur.execute(sql2)
            print("")
    else:
              print("")
    return

#Siirtää pelaajan target npc sijaintiin ja tulostaa npc esittelyn
def talkTo(locto, npcName):
    cur = db.cursor()
    sql = "UPDATE player SET locationID=" +str(locto)
    cur.execute(sql)
    if cur.rowcount>=1:
        print()
        print("You are now talking to "+npcName)
        print()
        printLocationNpc()
        
    else:
        print("Can't talk to imaginary people")
    return

#tulostaa npc:n kysymykset
def printQuestions(locationid):
    cur = db.cursor()
    sql = "SELECT Question FROM QUESTIONS WHERE Locationid=" +str(locationid)
    cur.execute(sql)
    if cur.rowcount>=1:
        i=1
        for row in cur.fetchall():
            print(i, ")", row[0])
            i+=1
        print("ONLY USE NUMERICAL VALUES OR 'BYE'")
    else:
        print("error producing questions")
    return

#tulostaa npc:n vastauksen kysymykseen
def printAnswer(questionid, locationid):
    if questionid != 0:
        cur = db.cursor()
        sql = "SELECT Answer FROM dialog WHERE locationID=" +str(locationid)+ " AND QuestionsID=" +str(questionid)
        cur.execute(sql)
        if cur.rowcount>=1:
            result = cur.fetchall()
            print(result[0][0])
        else:
            print("Error producing answer")
    else:
        print("What's that?")
    return

#hakee kysymysid:n lokaation perusteella
def getQuestionId(locid, qnum):
    cur = db.cursor()
    sql = "SELECT id FROM dialog WHERE locationID=" +str(locid)
    cur.execute(sql)
    if cur.rowcount>=1 and qnum <= cur.rowcount:
        result1 = cur.fetchall()
        result = result1[qnum-1][0]
    elif qnum > cur.rowcount:
        result = 0
    else:
        result = "Error getting questionId"
    return result

#palauttaa pelaajaan edelliseen lokaatioon
def returnToPreviousLocation(locid):
    cur = db.cursor()
    sql = "Update player SET locationid=" +str(locid)
    cur.execute(sql)
    if cur.rowcount>=1:
        result = "back to previous loc"
    else:
        result = "Error returning to previous location"


        
#Sama kuin printLocation, mutta tuloste muokattu npc:tä varten
def printLocationNpc():
    cur = db.cursor()
    sql = "SELECT name, info FROM location join player WHERE player.locationID = location.ID"
    cur.execute(sql)
    if cur.rowcount>=1:
        result = cur.fetchall()
        print()
        print(result[0][0] +" is a " + result[0][1])
    else:
        print("error printLocationNpc")
    return

#merkkaa puzzlen tehdyksi
def completePuzzle(puzzleid):
    puzzleid = checkforpuzzle()
    cur = db.cursor()
    sql = "UPDATE puzzle SET completed=1 WHERE ID="+ str(puzzleid)
    cur.execute(sql)
    if cur.rowcount>=1:
        print()
        print("Puzzle completed")
        print()
    else:
        print("Error setting puzzle completed")
    return

#tarkistaa onko puzzle tehty
def checkPuzzleCompleted(puzzleid):
    if puzzleid == 'no':
        result = 1
    else:
        cur = db.cursor()
        sql = "SELECT completed FROM puzzle WHERE ID="+ str(puzzleid)
        cur.execute(sql)
        result1 = cur.fetchall()
        result = result1[0][0]
    return result

#Tarkataa onko tietty nimi olemassa tietyssä lokaatiossa
def targetExists(target, loc):
    cur = db.cursor()
    sql = "SELECT * FROM locationallowed WHERE locationTo=" +str(loc)+ " AND Direction='" +str(target) +"'"
    cur.execute(sql)
    if cur.rowcount>=1:
        result = True
    else:
        result = False
    return result

#Tarkastaa onko liikkuminen sallittu
def locationAllowed(locfrom, locto):
    cur = db.cursor()
    sql = "SELECT locationALLOWED FROM locationallowed WHERE locationfrom=" +str(locfrom)+ " AND locationto=" +str(locto)
    cur.execute(sql)
    if cur.rowcount>=1:
        result1 = cur.fetchall()
        result=1
        if result1[0][0] == 1:
            result = result1[0][0]
        else:
            result=2
            print("location not allowed")
    else:
        result=2
    return result

#Asettaa liikkumisen sallituksi
def setLocationAllowed(locfrom, locto):
    cur = db.cursor()
    sql = "UPDATE locationallowed SET locationallowed=1 WHERE locationfrom=" +str(locfrom)+ " AND locationto=" +str(locto)
    cur.execute(sql)
    if cur.rowcount>=1:
        print()
        print("A location has been unlocked")
#    else:
#        print("Error unlocking location")
    return


#Luo Mysterious stranger hahmon#
def mysteriousstranger():
    cur=db.cursor()
    #Mysterious stranger location
    sql='insert into location values("Mysterious stranger","Mysterious looking person with hood casting a shadow on his face you so you cant quite make up what his face looks like properly, seems to hold key information about your situation",25);'
    #Mysterious stranger npc
    sql1='insert into npc value(8,"Mysterious stranger","Mysterious looking hooded man",7);'
    #Locationallowed
    sql2='insert into locationallowed values("Talk to Mysterious Stranger",7,25,null,34);'
    sql3='insert into locationallowed values("Bye",25,7,1,35);'
    
    #kysymys
    sql4='insert into questions values (21, "Who are you?",7);'
    #Vastaus
    sql5='insert into dialog values (21, "Hahahaha!!! Youre quite the jokester today. You know who i am.",7,21);'

    #event
    sql6= 'insert into events values (11,2, "A man approaches you and starts talking." "Mysterious stranger: What up man? didnt know you were comming to the cafe today." "You: What cafe?" "Mysterious stranger: Hahaha! Great joke man, the one across the street.",7);'
    cur.execute(sql)
    cur.execute(sql1)
    cur.execute(sql2)
    cur.execute(sql3)
    cur.execute(sql4)
    cur.execute(sql5)

    print("Mysterious stranger appears!")

    return

#Antaa memoryn
def givememory(id):
    cur = db.cursor()
    sql = "update memory set playerid=1 where id ="+str(id)
    cur.execute(sql)
    if cur.rowcount>=1:
        print("You have gained a memory!")
    return

#Tsekkaa onko pummien puzzlet tehtynä
def checkbumpuzzles():
    cur = db.cursor()
    sql = "select id from puzzle where completed = 1"
    cur.execute(sql)
    if cur.rowcount>=3:
        print("You have all your  clothes, now you should be able to move on now without having to worry about losing your face")
        setLocationAllowed(2,3)
        
    else:
        print("You still need more clothes to dare step out of the alley")
        
    return

#tarkastaa onko puhelin pelaajalla ja ajaa puzzlen jos on
def phoneExists():
    cur = db.cursor()
    sql = "SELECT * FROM item WHERE id=4 AND playerid=1"
    cur.execute(sql)
    if cur.rowcount>=1:
        phonepuzzle()
    else:
        print("You don't have a phone")


def checkMemoryInDialog(questionid, locationid):
#    print("parameters in checkMemory:", questionid, locationid)
    if questionid != 0:
        cur = db.cursor()
        sql = "SELECT id FROM dialog WHERE locationID=" +str(locationid)+ " AND QuestionsID=" +str(questionid)
        cur.execute(sql)
        if cur.rowcount>=1:
            result1 = cur.fetchall()
            result = result1[0][0]
#            print("found dialog id:", result)
        else:
            result = cur.fetchall
            result = result[0][0]
            print("error getting dialog id")
        sql = "SELECT id FROM memory WHERE dialogid="+str(result)
        cur.execute(sql)
        if cur.rowcount>=1:
#            print("found memory matchin dialogid")
            memoryid = cur.fetchall()
            memoryid = memoryid[0][0]
            givememory(memoryid)
    else:
        print("What's that?")
    return
    
        



#Luodaan tietokantayhteys
db = mysql.connector.connect(host="localhost",
                      user="dbuser10",
                      passwd="dbpass",
                      db="colawars",
                      buffered=True)
## PÄÄOHJELMA ALKAA ##

#tulosta intro
printIntro()

#määritetään pelaajan sijainti
loc = getLocation()

#Tulostetaan aloitussijainti
eventhappening()

#### TESTAA FUNKTIOITA TÄÄLLÄ ####







##### PARSER ######
print("type help for gameplay info")
cmd="blah"
while cmd != "quit":
    cmd = input()
    if cmd == "inventory":
        inventory()
        item = input("Would you like to take a closer look at something?(type item name or 'no')")
        item.lower()
        if item=="no":
            print("Moving on then")
        else:
            itemDetails(item)
    elif cmd == "memory":
        memory()
        memoryone = input("Would you like to immerse yourself into one of your memories? (Choose memory name or type 'no')")
        memoryone.lower()
        if memoryone=="no":
            print("Not right now then")
        else:
            remembermemory(memoryone)
    elif cmd == "help":
        printHelp()
    elif cmd == "look around":
        printLocation()
        getNPCinPLAYERlocation()
#       getItems(str(loc))
    elif cmd.lower() == "up" or cmd == "down" or cmd == "north" or cmd == "south" or cmd == "east" or cmd == "west":
        locto = getLocationTo(loc, cmd)
        loc = getLocation()
        locAllowed = locationAllowed(loc, locto)
        if locAllowed == 1 and locto !=0:
            move(locto, cmd)
            loc=getLocation()
            eventhappening()
            puzzle = checkforpuzzle()
            puzzlehappens(puzzle)
            printLocation()
    elif cmd[0:7].lower() == "talk to":
        target = cmd[8:]
        oldloc = getLocation()
        locto = getLocationTo(str(loc), cmd)
        if targetExists(cmd, locto) == True:
            talkTo(locto, target)
            print()
            eventhappening()
            puzzle = checkforpuzzle()
#            print("puzzle=", puzzle)
            puzzleCompleted = checkPuzzleCompleted(puzzle)
#            print("puzzlecompleted=", puzzleCompleted,)
            if puzzleCompleted == 2:
#                print("runnin puzzle")
                puzzlehappens(puzzle)
            puzzleCompleted = checkPuzzleCompleted(puzzle)
            if puzzleCompleted == 1:
#                print("not running puzzle")
                print()
                printQuestions(str(locto))
                qnum = input()
                while qnum != "bye" and qnum != "":
                    qnum = int(qnum)
                    qid = getQuestionId(locto, qnum)
                    printAnswer(qid, locto)
                    print()
                    checkMemoryInDialog(qid, locto)
                    print()
                    printQuestions(str(locto))
                    print()
                    qnum = input()
                returnToPreviousLocation(oldloc)
                printLocation()
        else:
            print("No such person in this location")
    elif cmd[0:4].lower() == "take":
        target = cmd[5:]
        takeItem(target)
    elif cmd == 'use phone':
        phoneExists()
    elif cmd == "quit":
        print("bye")
        break
    else:
        print("Can't do that.")
print("game over")


#hylkää tietokantaan tehdyt muutokset
db.rollback()
