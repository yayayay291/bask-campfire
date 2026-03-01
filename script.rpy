define backpack = []
define k = Character("Kage", color="#870c25")
define e = Character("Ezekiel", color="#BE9F6D")
define d = Character("Dion", color="#E0D0B9")
define l = Character("Lance", color="#add8e6")
define h = Character("Horatio", color="#663399")
define w = Character("Woman", color="#ff4122")
transform slightleft: 
    xalign 0.25
    yalign 1.0
transform slightright: 
    xalign 0.75
    yalign 1.0

# Helper label to reset all characters to their starting positions.
# Call `call set_start_positions` whenever you want them placed as at the beginning.
label set_start_positions:
    show kage speakingnormal at center
    show horatio speaking at slightleft
    show lance speaking at left
    show dion speaking at slightright
    show ezekiel speaking at right
    return
label start:
    scene bg livingroom1
    show kage speakingnormal at center
    show horatio speaking at slightleft
    show lance speaking at left
    show dion speaking at slightright
    show ezekiel speaking at right
    k "Guys, it has been so long since we've actually gone somewhere together. Nowadays y'all\nare so busy doing your own things."
    e "Hey, I can't help that I got places to be"
    show dion annoyed at slightright
    d "Oh please, the only thing you have been doing is running around with girls Ezek"
    show dion speaking at slightright
    h "It would be nice to update each other on our-"
    l "What about an arcade? We can play so many games"
    e "Hell no, I'm not a nerd like you. I'll lose aura"
    show dion annoyed at slightright
    d "Of course, you would suggest that."
    show dion speaking at slightright
    e "How about going to a party? Have fun dancing, drinking, and the ladiessss"
    d "Absolutely not."
    h "Yea man, I'm not a fan of loud spaces."
    k "We can go exploring, I heard it's popular nowadays."
    h "Exploring where exactly?"
    d "See that sounds cool, I'm in."
    e "Mhm…not bad. I'll come."
    l "Are we sure guys? What if it's really haunted?..."
    "Dion & Ezekiel" "that's the point genius"
    h "I don't know guys… most people who do that in movies die. I don't know about you guys but I\nwant to live past 18."
    k "Pleaseeee? Just once?"
    h "…fine"
    l "Okay then…"
    k "Let's pack then! Make sure to choose 4 items because that is all that will fit!"
    menu:
        "Flashlight":
            $ backpack.append("Flashlight");
        "Cameras":
            $ backpack.append("Cameras");
        "Pocket Knife":
            $ backpack.append("Pocket Knife");
        "Alcohol":
            $ backpack.append("Alcohol");
        "Sleeping Bag":
            $ backpack.append("Sleeping Bag");
        "Cards":
            $ backpack.append("Cards");
    menu:
        "Flashlight":
            $ backpack.append("Flashlight");
        "Cameras":
            $ backpack.append("Cameras");
        "Pocket Knife":
            $ backpack.append("Pocket Knife");
        "Alcohol":
            $ backpack.append("Alcohol");
        "Sleeping Bag":
            $ backpack.append("Sleeping Bag");
        "Cards":
            $ backpack.append("Cards");
    menu:
        "Flashlight":
            $ backpack.append("Flashlight");
        "Cameras":
            $ backpack.append("Cameras");
        "Pocket Knife":
            $ backpack.append("Pocket Knife");
        "Alcohol":
            $ backpack.append("Alcohol");
        "Sleeping Bag":
            $ backpack.append("Sleeping Bag");
        "Cards":
            $ backpack.append("Cards");
    menu:
        "Flashlight":
            $ backpack.append("Flashlight");
        "Cameras":
            $ backpack.append("Cameras");
        "Pocket Knife":
            $ backpack.append("Pocket Knife");
        "Alcohol":
            $ backpack.append("Alcohol");
        "Sleeping Bag":
            $ backpack.append("Sleeping Bag");
        "Cards":
            $ backpack.append("Cards");
    $ list_backpack = ", ".join(backpack)
    h "Everyone set? Do we want to check our backpacks first?"
    menu:
        "Yep, can't be too sure!":
            k "My backpack has: [list_backpack]"
        "Nah, I know what I packed.":
            h "Ok"
    k "Now let's go!"
    "Narrator" "They are on the road driving in a van. Horatio is the one driving, Kage is in the\npassenger seat. In the back are Dion Lance and Ezekiel. They are listening to 'Making my way\ndowntown'."

    "Play this Song"


    show dion annoyed at slightright
    d "Bruh. What type of music is this? Play something else"
    show dion speaking at slightright
    e "Yea,  pass me the aux lemme put yall on ball"
    show horatio annoyed at slightleft
    h "Guys let me ACTUALLY focus on the road…"
    show horatio speaking at slightleft
    k "We aren't tiktok thirst trappers. I'll be the music person."
    d "Fine… but  for the love of god, don't play anything emo"
    menu:
        "What song will you pick?"
        "Gasolina - Daddy Yankee":
            show dion happy at slightright
            d "AYYYY yes this is more like it!"
            show dion speaking at slightright
            show ezekiel annoyed at right
            e "I don't get the hype about this at all, we are still tik-tok thirst trappers\nlistening to this"
            show ezekiel speaking at right

        "Swang - Rae Sremmurd":
            show dion annoyed at slightright
            d "And how isn't this a thirst trap song?"
            show dion speaking at slightright
            show ezekiel happy at right
            e "Ooo this is such a banger! It's been so long since I heard this again"
            show ezekiel speaking at right
            l "Yea it's not that bad"

        "Golden- HUNTRIX":
            show lance happy at left
            l "I watched the movie last week!! Jinu is sooo fine!"
            show lance speaking at left
            d "That's mad fruity dude"
            e "Hey now, my boy's just appreciating looks, aint nothing bad bout that"
            show horatio annoyed at slightleft
            h "Can you all please shut up? You all are contributing to noise pollution. Kage,\nyou especially. Turn this trash off."
            show horatio speaking at slightleft

            menu:
                "Turn this 'trash' off":

                    "Stop Song"

                "Don't listen and continue the song":

                    "Play Song"
                    show dion annoyed at slightright
                    d "You better live a little Horatio"
                    show dion speaking at slightright
    h "We're almost here."
    "Narrator" "Time had passed, the sun was setting as they drove through the forest. They were the only\ncar on the lone road. By the time they reached, it was dark."



    h "Here. Now tip your uber driver"
    show dion happy at slightright
    d "Yea I got a tip for you, fix your hair. You look like the goofy evil purple minion."
    show dion speaking at slightright
    show ezekiel happy at right
    e "PFFT  HAHAHA"
    show ezekiel speaking at right
    show horatio annoyed at slightleft
    h "Should've crashed the car, you idiots."
    show horatio speaking at slightleft
    "Narrator" "They all got out of the car and stood right in front of the house. The house looked\ndirty and barely holding up."
    scene bg hauntedhouse
    show kage speakingnormal at center
    show horatio speaking at slightleft
    show lance speaking at left
    show dion speaking at slightright
    show ezekiel speaking at right
    "Change Music Back"

    k "This is going to be a make or break situation"
    show dion happy at slightright
    d "Man, I'm pumped!"
    show dion speaking at slightright
    h "Just seeing that house gives me goosebumps, the smell is so ranchid"
    e "And I thought Dion smelt bad"
    l "Come on guys, it looks totally safe…hopefully…"
    h "Last chance if anyone wants to be on my will"
    e "You got college loans buddy, your will is going to feature 2 cents that you always seem to add and a calculator."
    show kage annoyedspeaking at center
    k "Enough! Guys, lets just go in"
    show kage speakingnormal at center
    "Narrator" "They all enter the house, Kage was the last to enter. Without warning, the front door suddenly slammed shut, almost shaking the entire house."
    scene bg hauntedlivingroom
    show kage speakingnormal at center
    show horatio speaking at slightleft
    show lance speaking at left  
    show dion speaking at slightright
    show ezekiel speaking at right
    "Door Slam Sound"

    "Narrator" "Everyone paused"
    "Narrator" "Dion ran to the door, trying to break it open"
    scene bd hauntedhousedoor
    show kage speakingnormal at center
    show horatio speaking at slightleft
    show lance speaking at left
    show dion speaking at slightright
    show ezekiel speaking at right
    show dion scared at slightright
    d "Cooked. It's not budging at all!"
    show dion speaking at slightright
    scene bg hauntedlivingroom
    show kage speakingnormal at center
    show horatio speaking at slightleft
    show lance speaking at left
    show dion speaking at slightright
    show ezekiel speaking at right
    h "I told you guys so!! This was never a good idea!!  Now NONE of  y'all are going in my will"
    k "Guys! Guys! Guys!! This was the point! To explore a haunted house! We can't let them make us\nscared, that will give them power over us. Be calm."
    l "Y-yea! That sounds reasonable…"
    h "Look who seems to question everything now"
    d "Now what then? We go explore the house?"
    e "You know what? Why not, already stuck here. Might make the most of it."
    k "Can y'all please calm down, It will be fine. Trust"
    h "Kage don't even. I don't think my insurance covers this"
    k "Dude look around you, we are the dream team. We got a hunk, a pretty boy, a gamer, me an\noverthinker so I can think of any situation we can possibly be in, and you, Einstein. We are\ncovered, don't worry."
    h "ugh…fine"
    menu:
        "Where to explore on the main floor?"
        "Kitchen":
            k "How about the kitchen?"
            h "Fatty…"
            show kage annoyedspeaking at center
            k "Hey I heard that!"
            show kage normalspeaking at center
            e "Total clowns."
            "Narrator" "They walked to the kitchen, the floors creaking underneath, the turning\ncooler with each step."
            scene bg dirtykitchen
            show kage speakingnormal at center
            show horatio speaking at slightleft
            show lance speaking at left
            show dion speaking at slightright
            show ezekiel speaking at right
            "Creaking Sound"

            l "Guys…it smells really bad… I know it smelt bad before but this is just straight\nnasty…"
            "Narrator" "They looked at the state of the kitchen. It was dirty, musty, and abandoned.\nHowever there was a distinct smell of decay"
            h "Smells like road kill up in here"
            d "Genuinely what is that though?"
            k "guys…what is that…"
            show kage shocked at center
            "Narrator" "Kage pointed to the rotting pot on the kitchen stove. The boy walked closer\nto get a clear view of the substance in the pot…"
            show kage speakingnormal at center
            scene bg rotingpot
            show kage speakingnormal at center
            show horatio speaking at slightleft
            show lance speaking at left
            show dion speaking at slightright
            show ezekiel speaking at right
            e "Ew… is that an animal?"
            h "It seems like a goat?"
            l "i-if it is where is the head?"
            d "um…maybe they don't like animal heads?"
            k "yea, yea there are some cultures who eat goats, I've had it before. It tastes quite\ngood actually."
            e "Whatever… What's in the fridge?"
            menu:
                "Open the fridge?"
                "Yes":
                    k "Let's open it."
                    show horatio scared at slightleft
                    h "What?! No, are you crazy!?!"
                    show horatio normal at slightleft
                    d "Why not? We can finally see what else is making this place stink so bad"
                    e "Yea, just do it"
                    "Narrator" "Kage opens the door of the fridge…Inside were dead rats, a carton of\neggs, and a silver dagger with such intricate design on its handle."
                    scene bg kitchenwithdagger
                    show kage speakingnormal at center
                    show horatio speaking at slightleft
                    show lance speaking at left
                    show dion speaking at slightright
                    show ezekiel speaking at right
                    d "At least they're eggs?"
                    show ezekiel annoyed at right
                    e "Don't even play right now. I'm not eating ANYTHING from this household."
                    show ezekiel speaking at right
                    menu:
                        "Take the dagger or not?"
                        "Yes":
                            "Narrator" "Kage pocketed the dagger just in case"
                            scene bg kicthennodagger
                            show kage speakingnormal
                            show horatio speaking
                            show lance speaking
                            show dion speaking
                            show ezekiel speaking
                            $ backpack.append("Dagger");
                            $ list_backpack = ", ".join(backpack)
                            e "You're actually touching that?"
                            k "What if we need it later?"
                            l "Good point"
                        "No":
                            d "Don't touch that. What if it has some weird disease?"
                            h "Good catch, we need to be safe."
                "No":
                    h "Don't open it, we don't know what's in it."
                    e "Yea, imagine if something pops up on us, I would literally reset myself."
                    d "Drama queen"
                    l "Guys I don't think it's worth it…just leave it be"
                    k "fine"
            "Narrator" "They walked away from the kitchen."
            scene bg hauntedlivingroom 
            show kage speakingnormal
            show horatio speaking
            show lance speaking
            show dion speaking
            show ezekiel speaking       
        "Living Room":
            k "How about the living room?"
            h "Yea let's go."
            "Narrator" "All of them walked towards the living room, while walking Lance stumbled on the carpet and fell down, scratching his knee."
            l "Ow! I swear I just felt something!"
            d "You sure? I mean you're naturally clumsy dude."
            "Narrator" "Lance decided to look under the carpet because he for sure felt something"
            scene bg pentagramlift
            show kage speakingnormal
            show horatio speaking
            show lance speaking
            show dion speaking
            show ezekiel speaking
            l "Y'all have to see this"
            h "Whatever y'all do please be careful!"
            show ezekiel shocked
            e "Holy- there's a pentagram! A-and why are there scratches?!"
            show ezekiel speaking
            "Narrator" "Under the carpet was a carved pentagram on the wooden floor. There were numerous scratches on the pentagram… as if someone did them…"
            "Narrator" "Lance looked around a bit scared"
            show lance shocked
            l "There's some candles and an altar here."
            show lance speaking
            scene bg candlealtar
            show kage speakingnormal
            show horatio speaking
            show dion speaking
            show ezekiel speaking
            show dion shocked
            d "Guys look at the wall behind you…"
            show dion speaking
            "Narrator" "The boys looked behind, only to see more symbols carved in the walls… with hand and foot prints staining the walls and ceiling"
            scene bg bloodywall
            show kage speakingnormal
            show horatio speaking
            show dion speaking
            show ezekiel speaking
            show ezekiel shocked
            e "What the absolute!-"
            show ezekiel speaking
            show horatio shocked
            h "There's footprints on the ceiling?!"
            show horatio speaking
            k "Hundred percent someone doing some ritual! This is so shady"
            d "Mad sketchy. I must admit"
            h "I saw these things somewhere before… I'm not sure if they are used to get rid of spirits, ghosts, or curses or if they summon these entities."
            e "Ugh the one time you don't know"
            h "How about you focus on staying safe instead?"
            e "Yes mom"
            k "I feel weird, I cannot pinpoint exactly what though. I must be feeling nauseous because of all of this. This house…I don't know why…it feels familiar…"
            menu:
                "What to do about the living room?"
                "Keep exploring at our own risk..":
                    scene bg sofawithcross
                    show kage speakingnormal
                    show dion speaking
                    show ezekiel speaking
                    e "Guys, I think I found something"
                    d "Looks like a cross, should we keep it?"
                    menu:
                        "Keep the cross?"
                        "Yes":
                            k "I will save it for later, if the ghost ever confronts us."
                            "Narrator" "Kage grabs the cross in between the sofa and puts it in his backpack"
                            $ backpack.append("Cross");
                            $ list_backpack = ", ".join(backpack)
                            scene bg sofanocross
                            show kage speakingnormal
                            show dion speaking
                            show ezekiel speaking
                        "No":
                            k "Should I keep it-"
                            d "Nah, don't. We ball without trust."
                    e "I don't know about y'all, but I have had enough of this. Let's just get out of here."
                    "Narrator" "They leave the living room"
                    scene bg hauntedlivingroom
                    show ezekiel speaking
                "Turn around before it's too late":
                    e "I don't know about y'all, but I have had enough of this. Let's just get out of here."
                    "Narrator" "They leave the living room"
                    scene bg hauntedlivingroom
        "Bathroom":
            scene bg bathroom
            show kage speakingnormal
            show horatio speaking
            show lance speaking
            show dion speaking
            show ezekiel speaking
            k "How about the bathroom?"
            show dion shocked
            d "Wow, this place looks run down."
            show dion speaking
            l "Dare I say this smells worse than the kitchen"
            e "No joke guys, it smells like straight dookie."
            k "This bathroom also looks familiar- the counter always had cracks on it, I've felt these cracks before. When though?"
            show ezekiel annoyed
            e "Quit playing, genuinely. This is already giving me stress- stop adding on. My fan girls will ditch me and my aura will crash like the stock market during the great depression. I'm not even joking when I say I'll beat your-"
            show ezekiel speaking
            d "woah woah, calm down petty pink princess, you'll be safe. Take a deep breath."
            show ezekiel annoyed
            e "Whatever"
            show ezekiel speaking
            l "On the bright side at least we can use the bathroom? If we need"
            show horatio annoyed
            h "Thanks for the genuine moral support, truly appreciate it"
            show horatio speaking
            show ezekiel annoyed
            e "Yea lance, that fixes everything!"
            show ezekiel speaking
            k "Hey, at least he's trying to be supportive and positive"
            e "…Yea you're right, my bad Lance"
            "Narrator" "Lance nodded sheepishly"
            d "Yo, should we check the bathroom cabinets?"
            menu:
                "Check the bathroom cabinets?"
                "Yes":
                    k "Yes, let's do it."
                    "Narrator" "Kage opened the bathroom cabinet. Inside were the basic items such as a toothbrush, paste, toilet paper, however, there were a lot of pill bottles, and a small vial with a clear liquid."
                    scene bg vialcabinet
                    show kage speakingnormal
                    show horatio speaking
                    show lance speaking
                    show dion speaking
                    show ezekiel speaking
                    l "Wait, what's that vial?"
                    d "Bro…how are we supposed to know?"
                    l "I don't know? A wild guess?"
                    e "Oh! What if it's like holy water or something??"
                    d "Dude…why would such a house have something holy?"
                    e "in case things go wrong?"
                    h "Well that's not a completely trash idea"
                    menu:
                        "Take the vial?"
                        "Yes":
                            k "You know what? Let's take it. It won't hurt to keep"
                            h "Good thinking"
                            $ backpack.append("Vial");
                            $ list_backpack = ", ".join(backpack)
                            scene bg novialcabinet
                            show kage speakingnormal
                            show horatio speaking
                            show lance speaking
                            show dion speaking
                            show ezekiel speaking
                            l "Yea, let's go now please"
                            "Narrator" "Dion nodded and Ezekiel was happy to leave the nasty bathroom"
                        "No":
                            k "Let's leave. We shouldn't be here for this long."
                            h "Yea, let's just get out of this room."
                            e "Thank god. My nose was about to burn off."
                "No":
                    e "Can we just get out of this room? I swear I'm about to pass out because of the smell. It smells worse than Dion's farts, no joke."
                    d "What makes you think I won't stuff your face in the toilet?"
                    h "Let's just leave then"
            "Narrator" "The boys left the bathroom. But Kage had a strange deja vu of the house, but kept quiet."
            scene bg hauntedlivingroom     
        "Dining Room":
            scene bg lightdining
            show kage speakingnormal
            show horatio speaking
            show lance speaking
            show dion speaking
            show ezekiel speaking
            k "How about the dining room?"
            h "Why do the lights above keep flickering?"
            e "Nah the real question is how does this house even have electricity in the first place. This broke ahh house for real."
            k "Funny- that light was always weird when I was little"
            show ezekiel annoyed
            e "There you go again with the reminiscence. It truly freaking me out man"
            show ezekiel speaking
            h "Wait Kage? You've been here before?"
            k "What? No, but my childhood house was similar to this"
            e "Shut up, I see something under the table"
            menu:
                "Check under the table?"
                "Yes":
                    scene bg saltundertable
                    show kage speakingnormal
                    show horatio speaking
                    show lance speaking
                    show dion speaking
                    show ezekiel speaking
                    d "It looks to me like a bag of salt"
                    e "Swear it was some American who lived here. That salt is the only seasoning they use, that's why they got so much."
                    k "My mom BARELY put anything in our food….But then again she barely did anything for me."
                    e "Oh wow, lore drop"
                    h "You idiot. That's not the only reason salt is used. This is what they use to draw the symbols and outline protective areas."
                    e "Actually?"
                    show lance scared
                    l "I swear to god a cult maybe lived here"
                    show lance speaking
                    d "Do you think we should keep it? Is it some clue?"
                    k "Maybe"
                    menu:
                        "Pick up the salt?"
                        "Yes":
                            k "Let's keep it. I have a strange feeling that this all will lead to something"
                            $ backpack.append("Salt");
                            $ list_backpack = ", ".join(backpack)
                            scene bg underdiningtable
                            show kage speakingnormal
                            show horatio speaking
                            show lance speaking
                            show dion speaking
                            show ezekiel speaking
                        "No":
                            k "I don't know- I have a feeling bad things may happen"
                            d "Just keep it there then."
                "No":
                    e "Bruh I'm not checking under that table. The times I check under the table I see the most diabolical chewed up gum stuck. What if instead of gum I see teeth or eyes."
                    l "Yea, let's leave this be"
                    h "Valid, only god knows what growing on that wood"
                    d "I don't think it's worth it,At this point we should be working to leave this house."
                    e "Yes finally. I don't wanna be stuck in this ghetto house anymore. Can we please leave before my manicure gets wrecked?"
            "Narrator" "The boys decided to leave the dining room."
            scene bg hauntedlivingroom 
    menu:
        "Where to explore on the main floor?"
        "Kitchen":
            k "How about the kitchen?"
            h "Fatty…"
            show kage annoyedspeaking
            k "Hey I heard that!"
            show kage normalspeaking
            e "Total clowns."
            "Narrator" "They walked to the kitchen, the floors creaking underneath, the turning\ncooler with each step."
            scene bg dirtykitchen
            show kage speakingnormal
            show horatio speaking
            show lance speaking
            show dion speaking
            show ezekiel speaking
            "Creaking Sound"

            l "Guys…it smells really bad… I know it smelt bad before but this is just straight\nnasty…"
            "Narrator" "They looked at the state of the kitchen. It was dirty, musty, and abandoned.\nHowever there was a distinct smell of decay"
            h "Smells like road kill up in here"
            d "Genuinely what is that though?"
            k "guys…what is that…"
            show kage shocked
            "Narrator" "Kage pointed to the rotting pot on the kitchen stove. The boy walked closer\nto get a clear view of the substance in the pot…"
            show kage speakingnormal
            scene bg rotingpot
            show kage speakingnormal
            show horatio speaking
            show lance speaking
            show dion speaking
            show ezekiel speaking
            e "Ew… is that an animal?"
            h "It seems like a goat?"
            l "i-if it is where is the head?"
            d "um…maybe they don't like animal heads?"
            k "yea, yea there are some cultures who eat goats, I've had it before. It tastes quite\ngood actually."
            e "Whatever… What's in the fridge?"
            menu:
                "Open the fridge?"
                "Yes":
                    k "Let's open it."
                    show horatio scared
                    h "What?! No, are you crazy!?!"
                    show horatio normal
                    d "Why not? We can finally see what else is making this place stink so bad"
                    e "Yea, just do it"
                    "Narrator" "Kage opens the door of the fridge…Inside were dead rats, a carton of\neggs, and a silver dagger with such intricate design on its handle."
                    scene bg kitchenwithdagger
                    show kage speakingnormal
                    show horatio speaking
                    show lance speaking
                    show dion speaking
                    show ezekiel speaking
                    d "At least they're eggs?"
                    show ezekiel annoyed
                    e "Don't even play right now. I'm not eating ANYTHING from this household."
                    show ezekiel speaking
                    menu:
                        "Take the dagger or not?"
                        "Yes":
                            "Narrator" "Kage pocketed the dagger just in case"
                            scene bg kicthennodagger
                            show kage speakingnormal
                            show horatio speaking
                            show lance speaking
                            show dion speaking
                            show ezekiel speaking
                            $ backpack.append("Dagger");
                            $ list_backpack = ", ".join(backpack)
                            e "You're actually touching that?"
                            k "What if we need it later?"
                            l "Good point"
                        "No":
                            d "Don't touch that. What if it has some weird disease?"
                            h "Good catch, we need to be safe."
                "No":
                    h "Don't open it, we don't know what's in it."
                    e "Yea, imagine if something pops up on us, I would literally reset myself."
                    d "Drama queen"
                    l "Guys I don't think it's worth it…just leave it be"
                    k "fine"
            "Narrator" "They walked away from the kitchen."
            scene bg hauntedlivingroom 
            show kage speakingnormal
            show horatio speaking
            show lance speaking
            show dion speaking
            show ezekiel speaking       
        "Living Room":
            k "How about the living room?"
            h "Yea let's go."
            "Narrator" "All of them walked towards the living room, while walking Lance stumbled on the carpet and fell down, scratching his knee."
            l "Ow! I swear I just felt something!"
            d "You sure? I mean you're naturally clumsy dude."
            "Narrator" "Lance decided to look under the carpet because he for sure felt something"
            scene bg pentagramlift
            show kage speakingnormal
            show horatio speaking
            show lance speaking
            show dion speaking
            show ezekiel speaking
            l "Y'all have to see this"
            h "Whatever y'all do please be careful!"
            show ezekiel shocked
            e "Holy- there's a pentagram! A-and why are there scratches?!"
            show ezekiel speaking
            "Narrator" "Under the carpet was a carved pentagram on the wooden floor. There were numerous scratches on the pentagram… as if someone did them…"
            "Narrator" "Lance looked around a bit scared"
            show lance shocked
            l "There's some candles and an altar here."
            show lance speaking
            scene bg candlealtar
            show kage speakingnormal
            show horatio speaking
            show dion speaking
            show ezekiel speaking
            show dion shocked
            d "Guys look at the wall behind you…"
            show dion speaking
            "Narrator" "The boys looked behind, only to see more symbols carved in the walls… with hand and foot prints staining the walls and ceiling"
            scene bg bloodywall
            show kage speakingnormal
            show horatio speaking
            show dion speaking
            show ezekiel speaking
            show ezekiel shocked
            e "What the absolute!-"
            show ezekiel speaking
            show horatio shocked
            h "There's footprints on the ceiling?!"
            show horatio speaking
            k "Hundred percent someone doing some ritual! This is so shady"
            d "Mad sketchy. I must admit"
            h "I saw these things somewhere before… I'm not sure if they are used to get rid of spirits, ghosts, or curses or if they summon these entities."
            e "Ugh the one time you don't know"
            h "How about you focus on staying safe instead?"
            e "Yes mom"
            k "I feel weird, I cannot pinpoint exactly what though. I must be feeling nauseous because of all of this. This house…I don't know why…it feels familiar…"
            menu:
                "What to do about the living room?"
                "Keep exploring at our own risk..":
                    scene bg sofawithcross
                    show kage speakingnormal
                    show dion speaking
                    show ezekiel speaking
                    e "Guys, I think I found something"
                    d "Looks like a cross, should we keep it?"
                    menu:
                        "Keep the cross?"
                        "Yes":
                            k "I will save it for later, if the ghost ever confronts us."
                            "Narrator" "Kage grabs the cross in between the sofa and puts it in his backpack"
                            $ backpack.append("Cross");
                            $ list_backpack = ", ".join(backpack)
                            scene bg sofanocross
                            show kage speakingnormal
                            show dion speaking
                            show ezekiel speaking
                        "No":
                            k "Should I keep it-"
                            d "Nah, don't. We ball without trust."
                    e "I don't know about y'all, but I have had enough of this. Let's just get out of here."
                    "Narrator" "They leave the living room"
                    scene bg hauntedlivingroom
                    show ezekiel speaking
                "Turn around before it's too late":
                    e "I don't know about y'all, but I have had enough of this. Let's just get out of here."
                    "Narrator" "They leave the living room"
                    scene bg hauntedlivingroom
        "Bathroom":
            scene bg bathroom
            show kage speakingnormal
            show horatio speaking
            show lance speaking
            show dion speaking
            show ezekiel speaking
            k "How about the bathroom?"
            show dion shocked
            d "Wow, this place looks run down."
            show dion speaking
            l "Dare I say this smells worse than the kitchen"
            e "No joke guys, it smells like straight dookie."
            k "This bathroom also looks familiar- the counter always had cracks on it, I've felt these cracks before. When though?"
            show ezekiel annoyed
            e "Quit playing, genuinely. This is already giving me stress- stop adding on. My fan girls will ditch me and my aura will crash like the stock market during the great depression. I'm not even joking when I say I'll beat your-"
            show ezekiel speaking
            d "woah woah, calm down petty pink princess, you'll be safe. Take a deep breath."
            show ezekiel annoyed
            e "Whatever"
            show ezekiel speaking
            l "On the bright side at least we can use the bathroom? If we need"
            show horatio annoyed
            h "Thanks for the genuine moral support, truly appreciate it"
            show horatio speaking
            show ezekiel annoyed
            e "Yea lance, that fixes everything!"
            show ezekiel speaking
            k "Hey, at least he's trying to be supportive and positive"
            e "…Yea you're right, my bad Lance"
            "Narrator" "Lance nodded sheepishly"
            d "Yo, should we check the bathroom cabinets?"
            menu:
                "Check the bathroom cabinets?"
                "Yes":
                    k "Yes, let's do it."
                    "Narrator" "Kage opened the bathroom cabinet. Inside were the basic items such as a toothbrush, paste, toilet paper, however, there were a lot of pill bottles, and a small vial with a clear liquid."
                    scene bg vialcabinet
                    show kage speakingnormal
                    show horatio speaking
                    show lance speaking
                    show dion speaking
                    show ezekiel speaking
                    l "Wait, what's that vial?"
                    d "Bro…how are we supposed to know?"
                    l "I don't know? A wild guess?"
                    e "Oh! What if it's like holy water or something??"
                    d "Dude…why would such a house have something holy?"
                    e "in case things go wrong?"
                    h "Well that's not a completely trash idea"
                    menu:
                        "Take the vial?"
                        "Yes":
                            k "You know what? Let's take it. It won't hurt to keep"
                            h "Good thinking"
                            $ backpack.append("Vial");
                            $ list_backpack = ", ".join(backpack)
                            scene bg novialcabinet
                            show kage speakingnormal
                            show horatio speaking
                            show lance speaking
                            show dion speaking
                            show ezekiel speaking
                            l "Yea, let's go now please"
                            "Narrator" "Dion nodded and Ezekiel was happy to leave the nasty bathroom"
                        "No":
                            k "Let's leave. We shouldn't be here for this long."
                            h "Yea, let's just get out of this room."
                            e "Thank god. My nose was about to burn off."
                "No":
                    e "Can we just get out of this room? I swear I'm about to pass out because of the smell. It smells worse than Dion's farts, no joke."
                    d "What makes you think I won't stuff your face in the toilet?"
                    h "Let's just leave then"
            "Narrator" "The boys left the bathroom. But Kage had a strange deja vu of the house, but kept quiet."
            scene bg hauntedlivingroom     
        "Dining Room":
            scene bg lightdining
            show kage speakingnormal
            show horatio speaking
            show lance speaking
            show dion speaking
            show ezekiel speaking
            k "How about the dining room?"
            h "Why do the lights above keep flickering?"
            e "Nah the real question is how does this house even have electricity in the first place. This broke ahh house for real."
            k "Funny- that light was always weird when I was little"
            show ezekiel annoyed
            e "There you go again with the reminiscence. It truly freaking me out man"
            show ezekiel speaking
            h "Wait Kage? You've been here before?"
            k "What? No, but my childhood house was similar to this"
            e "Shut up, I see something under the table"
            menu:
                "Check under the table?"
                "Yes":
                    scene bg saltundertable
                    show kage speakingnormal
                    show horatio speaking
                    show lance speaking
                    show dion speaking
                    show ezekiel speaking
                    d "It looks to me like a bag of salt"
                    e "Swear it was some American who lived here. That salt is the only seasoning they use, that's why they got so much."
                    k "My mom BARELY put anything in our food….But then again she barely did anything for me."
                    e "Oh wow, lore drop"
                    h "You idiot. That's not the only reason salt is used. This is what they use to draw the symbols and outline protective areas."
                    e "Actually?"
                    show lance scared
                    l "I swear to god a cult maybe lived here"
                    show lance speaking
                    d "Do you think we should keep it? Is it some clue?"
                    k "Maybe"
                    menu:
                        "Pick up the salt?"
                        "Yes":
                            k "Let's keep it. I have a strange feeling that this all will lead to something"
                            $ backpack.append("Salt");
                            $ list_backpack = ", ".join(backpack)
                            scene bg underdiningtable
                            show kage speakingnormal
                            show horatio speaking
                            show lance speaking
                            show dion speaking
                            show ezekiel speaking
                        "No":
                            k "I don't know- I have a feeling bad things may happen"
                            d "Just keep it there then."
                "No":
                    e "Bruh I'm not checking under that table. The times I check under the table I see the most diabolical chewed up gum stuck. What if instead of gum I see teeth or eyes."
                    l "Yea, let's leave this be"
                    h "Valid, only god knows what growing on that wood"
                    d "I don't think it's worth it,At this point we should be working to leave this house."
                    e "Yes finally. I don't wanna be stuck in this ghetto house anymore. Can we please leave before my manicure gets wrecked?"
            "Narrator" "The boys decided to leave the dining room."
            scene bg hauntedlivingroom 
    menu:
        "Where to explore on the main floor?"
        "Kitchen":
            k "How about the kitchen?"
            h "Fatty…"
            show kage annoyedspeaking
            k "Hey I heard that!"
            show kage normalspeaking
            e "Total clowns."
            "Narrator" "They walked to the kitchen, the floors creaking underneath, the turning\ncooler with each step."
            scene bg dirtykitchen
            show kage speakingnormal
            show horatio speaking
            show lance speaking
            show dion speaking
            show ezekiel speaking
            "Creaking Sound"

            l "Guys…it smells really bad… I know it smelt bad before but this is just straight\nnasty…"
            "Narrator" "They looked at the state of the kitchen. It was dirty, musty, and abandoned.\nHowever there was a distinct smell of decay"
            h "Smells like road kill up in here"
            d "Genuinely what is that though?"
            k "guys…what is that…"
            show kage shocked
            "Narrator" "Kage pointed to the rotting pot on the kitchen stove. The boy walked closer\nto get a clear view of the substance in the pot…"
            show kage speakingnormal
            scene bg rotingpot
            show kage speakingnormal
            show horatio speaking
            show lance speaking
            show dion speaking
            show ezekiel speaking
            e "Ew… is that an animal?"
            h "It seems like a goat?"
            l "i-if it is where is the head?"
            d "um…maybe they don't like animal heads?"
            k "yea, yea there are some cultures who eat goats, I've had it before. It tastes quite\ngood actually."
            e "Whatever… What's in the fridge?"
            menu:
                "Open the fridge?"
                "Yes":
                    k "Let's open it."
                    show horatio scared
                    h "What?! No, are you crazy!?!"
                    show horatio normal
                    d "Why not? We can finally see what else is making this place stink so bad"
                    e "Yea, just do it"
                    "Narrator" "Kage opens the door of the fridge…Inside were dead rats, a carton of\neggs, and a silver dagger with such intricate design on its handle."
                    scene bg kitchenwithdagger
                    show kage speakingnormal
                    show horatio speaking
                    show lance speaking
                    show dion speaking
                    show ezekiel speaking
                    d "At least they're eggs?"
                    show ezekiel annoyed
                    e "Don't even play right now. I'm not eating ANYTHING from this household."
                    show ezekiel speaking
                    menu:
                        "Take the dagger or not?"
                        "Yes":
                            "Narrator" "Kage pocketed the dagger just in case"
                            scene bg kicthennodagger
                            show kage speakingnormal
                            show horatio speaking
                            show lance speaking
                            show dion speaking
                            show ezekiel speaking
                            $ backpack.append("Dagger");
                            $ list_backpack = ", ".join(backpack)
                            e "You're actually touching that?"
                            k "What if we need it later?"
                            l "Good point"
                        "No":
                            d "Don't touch that. What if it has some weird disease?"
                            h "Good catch, we need to be safe."
                "No":
                    h "Don't open it, we don't know what's in it."
                    e "Yea, imagine if something pops up on us, I would literally reset myself."
                    d "Drama queen"
                    l "Guys I don't think it's worth it…just leave it be"
                    k "fine"
            "Narrator" "They walked away from the kitchen."
            scene bg hauntedlivingroom 
            show kage speakingnormal
            show horatio speaking
            show lance speaking
            show dion speaking
            show ezekiel speaking       
        "Living Room":
            k "How about the living room?"
            h "Yea let's go."
            "Narrator" "All of them walked towards the living room, while walking Lance stumbled on the carpet and fell down, scratching his knee."
            l "Ow! I swear I just felt something!"
            d "You sure? I mean you're naturally clumsy dude."
            "Narrator" "Lance decided to look under the carpet because he for sure felt something"
            scene bg pentagramlift
            show kage speakingnormal
            show horatio speaking
            show lance speaking
            show dion speaking
            show ezekiel speaking
            l "Y'all have to see this"
            h "Whatever y'all do please be careful!"
            show ezekiel shocked
            e "Holy- there's a pentagram! A-and why are there scratches?!"
            show ezekiel speaking
            "Narrator" "Under the carpet was a carved pentagram on the wooden floor. There were numerous scratches on the pentagram… as if someone did them…"
            "Narrator" "Lance looked around a bit scared"
            show lance shocked
            l "There's some candles and an altar here."
            show lance speaking
            scene bg candlealtar
            show kage speakingnormal
            show horatio speaking
            show dion speaking
            show ezekiel speaking
            show dion shocked
            d "Guys look at the wall behind you…"
            show dion speaking
            "Narrator" "The boys looked behind, only to see more symbols carved in the walls… with hand and foot prints staining the walls and ceiling"
            scene bg bloodywall
            show kage speakingnormal
            show horatio speaking
            show dion speaking
            show ezekiel speaking
            show ezekiel shocked
            e "What the absolute!-"
            show ezekiel speaking
            show horatio shocked
            h "There's footprints on the ceiling?!"
            show horatio speaking
            k "Hundred percent someone doing some ritual! This is so shady"
            d "Mad sketchy. I must admit"
            h "I saw these things somewhere before… I'm not sure if they are used to get rid of spirits, ghosts, or curses or if they summon these entities."
            e "Ugh the one time you don't know"
            h "How about you focus on staying safe instead?"
            e "Yes mom"
            k "I feel weird, I cannot pinpoint exactly what though. I must be feeling nauseous because of all of this. This house…I don't know why…it feels familiar…"
            menu:
                "What to do about the living room?"
                "Keep exploring at our own risk..":
                    scene bg sofawithcross
                    show kage speakingnormal
                    show dion speaking
                    show ezekiel speaking
                    e "Guys, I think I found something"
                    d "Looks like a cross, should we keep it?"
                    menu:
                        "Keep the cross?"
                        "Yes":
                            k "I will save it for later, if the ghost ever confronts us."
                            "Narrator" "Kage grabs the cross in between the sofa and puts it in his backpack"
                            $ backpack.append("Cross");
                            $ list_backpack = ", ".join(backpack)
                            scene bg sofanocross
                            show kage speakingnormal
                            show dion speaking
                            show ezekiel speaking
                        "No":
                            k "Should I keep it-"
                            d "Nah, don't. We ball without trust."
                    e "I don't know about y'all, but I have had enough of this. Let's just get out of here."
                    "Narrator" "They leave the living room"
                    scene bg hauntedlivingroom
                    show ezekiel speaking
                "Turn around before it's too late":
                    e "I don't know about y'all, but I have had enough of this. Let's just get out of here."
                    "Narrator" "They leave the living room"
                    scene bg hauntedlivingroom
        "Bathroom":
            scene bg bathroom
            show kage speakingnormal
            show horatio speaking
            show lance speaking
            show dion speaking
            show ezekiel speaking
            k "How about the bathroom?"
            show dion shocked
            d "Wow, this place looks run down."
            show dion speaking
            l "Dare I say this smells worse than the kitchen"
            e "No joke guys, it smells like straight dookie."
            k "This bathroom also looks familiar- the counter always had cracks on it, I've felt these cracks before. When though?"
            show ezekiel annoyed
            e "Quit playing, genuinely. This is already giving me stress- stop adding on. My fan girls will ditch me and my aura will crash like the stock market during the great depression. I'm not even joking when I say I'll beat your-"
            show ezekiel speaking
            d "woah woah, calm down petty pink princess, you'll be safe. Take a deep breath."
            show ezekiel annoyed
            e "Whatever"
            show ezekiel speaking
            l "On the bright side at least we can use the bathroom? If we need"
            show horatio annoyed
            h "Thanks for the genuine moral support, truly appreciate it"
            show horatio speaking
            show ezekiel annoyed
            e "Yea lance, that fixes everything!"
            show ezekiel speaking
            k "Hey, at least he's trying to be supportive and positive"
            e "…Yea you're right, my bad Lance"
            "Narrator" "Lance nodded sheepishly"
            d "Yo, should we check the bathroom cabinets?"
            menu:
                "Check the bathroom cabinets?"
                "Yes":
                    k "Yes, let's do it."
                    "Narrator" "Kage opened the bathroom cabinet. Inside were the basic items such as a toothbrush, paste, toilet paper, however, there were a lot of pill bottles, and a small vial with a clear liquid."
                    scene bg vialcabinet
                    show kage speakingnormal
                    show horatio speaking
                    show lance speaking
                    show dion speaking
                    show ezekiel speaking
                    l "Wait, what's that vial?"
                    d "Bro…how are we supposed to know?"
                    l "I don't know? A wild guess?"
                    e "Oh! What if it's like holy water or something??"
                    d "Dude…why would such a house have something holy?"
                    e "in case things go wrong?"
                    h "Well that's not a completely trash idea"
                    menu:
                        "Take the vial?"
                        "Yes":
                            k "You know what? Let's take it. It won't hurt to keep"
                            h "Good thinking"
                            $ backpack.append("Vial");
                            $ list_backpack = ", ".join(backpack)
                            scene bg novialcabinet
                            show kage speakingnormal
                            show horatio speaking
                            show lance speaking
                            show dion speaking
                            show ezekiel speaking
                            l "Yea, let's go now please"
                            "Narrator" "Dion nodded and Ezekiel was happy to leave the nasty bathroom"
                        "No":
                            k "Let's leave. We shouldn't be here for this long."
                            h "Yea, let's just get out of this room."
                            e "Thank god. My nose was about to burn off."
                "No":
                    e "Can we just get out of this room? I swear I'm about to pass out because of the smell. It smells worse than Dion's farts, no joke."
                    d "What makes you think I won't stuff your face in the toilet?"
                    h "Let's just leave then"
            "Narrator" "The boys left the bathroom. But Kage had a strange deja vu of the house, but kept quiet."
            scene bg hauntedlivingroom     
        "Dining Room":
            scene bg lightdining
            show kage speakingnormal
            show horatio speaking
            show lance speaking
            show dion speaking
            show ezekiel speaking
            k "How about the dining room?"
            h "Why do the lights above keep flickering?"
            e "Nah the real question is how does this house even have electricity in the first place. This broke ahh house for real."
            k "Funny- that light was always weird when I was little"
            show ezekiel annoyed
            e "There you go again with the reminiscence. It truly freaking me out man"
            show ezekiel speaking
            h "Wait Kage? You've been here before?"
            k "What? No, but my childhood house was similar to this"
            e "Shut up, I see something under the table"
            menu:
                "Check under the table?"
                "Yes":
                    scene bg saltundertable
                    show kage speakingnormal
                    show horatio speaking
                    show lance speaking
                    show dion speaking
                    show ezekiel speaking
                    d "It looks to me like a bag of salt"
                    e "Swear it was some American who lived here. That salt is the only seasoning they use, that's why they got so much."
                    k "My mom BARELY put anything in our food….But then again she barely did anything for me."
                    e "Oh wow, lore drop"
                    h "You idiot. That's not the only reason salt is used. This is what they use to draw the symbols and outline protective areas."
                    e "Actually?"
                    show lance scared
                    l "I swear to god a cult maybe lived here"
                    show lance speaking
                    d "Do you think we should keep it? Is it some clue?"
                    k "Maybe"
                    menu:
                        "Pick up the salt?"
                        "Yes":
                            k "Let's keep it. I have a strange feeling that this all will lead to something"
                            $ backpack.append("Salt");
                            $ list_backpack = ", ".join(backpack)
                            scene bg underdiningtable
                            show kage speakingnormal
                            show horatio speaking
                            show lance speaking
                            show dion speaking
                            show ezekiel speaking
                        "No":
                            k "I don't know- I have a feeling bad things may happen"
                            d "Just keep it there then."
                "No":
                    e "Bruh I'm not checking under that table. The times I check under the table I see the most diabolical chewed up gum stuck. What if instead of gum I see teeth or eyes."
                    l "Yea, let's leave this be"
                    h "Valid, only god knows what growing on that wood"
                    d "I don't think it's worth it,At this point we should be working to leave this house."
                    e "Yes finally. I don't wanna be stuck in this ghetto house anymore. Can we please leave before my manicure gets wrecked?"
            "Narrator" "The boys decided to leave the dining room."
            scene bg hauntedlivingroom 
    menu:
        "Where to explore on the main floor?"
        "Kitchen":
            k "How about the kitchen?"
            h "Fatty…"
            show kage annoyedspeaking
            k "Hey I heard that!"
            show kage normalspeaking
            e "Total clowns."
            "Narrator" "They walked to the kitchen, the floors creaking underneath, the turning\ncooler with each step."
            scene bg dirtykitchen
            show kage speakingnormal
            show horatio speaking
            show lance speaking
            show dion speaking
            show ezekiel speaking
            "Creaking Sound"

            l "Guys…it smells really bad… I know it smelt bad before but this is just straight\nnasty…"
            "Narrator" "They looked at the state of the kitchen. It was dirty, musty, and abandoned.\nHowever there was a distinct smell of decay"
            h "Smells like road kill up in here"
            d "Genuinely what is that though?"
            k "guys…what is that…"
            show kage shocked
            "Narrator" "Kage pointed to the rotting pot on the kitchen stove. The boy walked closer\nto get a clear view of the substance in the pot…"
            show kage speakingnormal
            scene bg rotingpot
            show kage speakingnormal
            show horatio speaking
            show lance speaking
            show dion speaking
            show ezekiel speaking
            e "Ew… is that an animal?"
            h "It seems like a goat?"
            l "i-if it is where is the head?"
            d "um…maybe they don't like animal heads?"
            k "yea, yea there are some cultures who eat goats, I've had it before. It tastes quite\ngood actually."
            e "Whatever… What's in the fridge?"
            menu:
                "Open the fridge?"
                "Yes":
                    k "Let's open it."
                    show horatio scared
                    h "What?! No, are you crazy!?!"
                    show horatio normal
                    d "Why not? We can finally see what else is making this place stink so bad"
                    e "Yea, just do it"
                    "Narrator" "Kage opens the door of the fridge…Inside were dead rats, a carton of\neggs, and a silver dagger with such intricate design on its handle."
                    scene bg kitchenwithdagger
                    show kage speakingnormal
                    show horatio speaking
                    show lance speaking
                    show dion speaking
                    show ezekiel speaking
                    d "At least they're eggs?"
                    show ezekiel annoyed
                    e "Don't even play right now. I'm not eating ANYTHING from this household."
                    show ezekiel speaking
                    menu:
                        "Take the dagger or not?"
                        "Yes":
                            "Narrator" "Kage pocketed the dagger just in case"
                            scene bg kicthennodagger
                            show kage speakingnormal
                            show horatio speaking
                            show lance speaking
                            show dion speaking
                            show ezekiel speaking
                            $ backpack.append("Dagger");
                            $ list_backpack = ", ".join(backpack)
                            e "You're actually touching that?"
                            k "What if we need it later?"
                            l "Good point"
                        "No":
                            d "Don't touch that. What if it has some weird disease?"
                            h "Good catch, we need to be safe."
                "No":
                    h "Don't open it, we don't know what's in it."
                    e "Yea, imagine if something pops up on us, I would literally reset myself."
                    d "Drama queen"
                    l "Guys I don't think it's worth it…just leave it be"
                    k "fine"
            "Narrator" "They walked away from the kitchen."
            scene bg hauntedlivingroom 
            show kage speakingnormal
            show horatio speaking
            show lance speaking
            show dion speaking
            show ezekiel speaking       
        "Living Room":
            k "How about the living room?"
            h "Yea let's go."
            "Narrator" "All of them walked towards the living room, while walking Lance stumbled on the carpet and fell down, scratching his knee."
            l "Ow! I swear I just felt something!"
            d "You sure? I mean you're naturally clumsy dude."
            "Narrator" "Lance decided to look under the carpet because he for sure felt something"
            scene bg pentagramlift
            show kage speakingnormal
            show horatio speaking
            show lance speaking
            show dion speaking
            show ezekiel speaking
            l "Y'all have to see this"
            h "Whatever y'all do please be careful!"
            show ezekiel shocked
            e "Holy- there's a pentagram! A-and why are there scratches?!"
            show ezekiel speaking
            "Narrator" "Under the carpet was a carved pentagram on the wooden floor. There were numerous scratches on the pentagram… as if someone did them…"
            "Narrator" "Lance looked around a bit scared"
            show lance shocked
            l "There's some candles and an altar here."
            show lance speaking
            scene bg candlealtar
            show kage speakingnormal
            show horatio speaking
            show dion speaking
            show ezekiel speaking
            show dion shocked
            d "Guys look at the wall behind you…"
            show dion speaking
            "Narrator" "The boys looked behind, only to see more symbols carved in the walls… with hand and foot prints staining the walls and ceiling"
            scene bg bloodywall
            show kage speakingnormal
            show horatio speaking
            show dion speaking
            show ezekiel speaking
            show ezekiel shocked
            e "What the absolute!-"
            show ezekiel speaking
            show horatio shocked
            h "There's footprints on the ceiling?!"
            show horatio speaking
            k "Hundred percent someone doing some ritual! This is so shady"
            d "Mad sketchy. I must admit"
            h "I saw these things somewhere before… I'm not sure if they are used to get rid of spirits, ghosts, or curses or if they summon these entities."
            e "Ugh the one time you don't know"
            h "How about you focus on staying safe instead?"
            e "Yes mom"
            k "I feel weird, I cannot pinpoint exactly what though. I must be feeling nauseous because of all of this. This house…I don't know why…it feels familiar…"
            menu:
                "What to do about the living room?"
                "Keep exploring at our own risk..":
                    scene bg sofawithcross
                    show kage speakingnormal
                    show dion speaking
                    show ezekiel speaking
                    e "Guys, I think I found something"
                    d "Looks like a cross, should we keep it?"
                    menu:
                        "Keep the cross?"
                        "Yes":
                            k "I will save it for later, if the ghost ever confronts us."
                            "Narrator" "Kage grabs the cross in between the sofa and puts it in his backpack"
                            $ backpack.append("Cross");
                            $ list_backpack = ", ".join(backpack)
                            scene bg sofanocross
                            show kage speakingnormal
                            show dion speaking
                            show ezekiel speaking
                        "No":
                            k "Should I keep it-"
                            d "Nah, don't. We ball without trust."
                    e "I don't know about y'all, but I have had enough of this. Let's just get out of here."
                    "Narrator" "They leave the living room"
                    scene bg hauntedlivingroom
                    show ezekiel speaking
                "Turn around before it's too late":
                    e "I don't know about y'all, but I have had enough of this. Let's just get out of here."
                    "Narrator" "They leave the living room"
                    scene bg hauntedlivingroom
        "Bathroom":
            scene bg bathroom
            show kage speakingnormal
            show horatio speaking
            show lance speaking
            show dion speaking
            show ezekiel speaking
            k "How about the bathroom?"
            show dion shocked
            d "Wow, this place looks run down."
            show dion speaking
            l "Dare I say this smells worse than the kitchen"
            e "No joke guys, it smells like straight dookie."
            k "This bathroom also looks familiar- the counter always had cracks on it, I've felt these cracks before. When though?"
            show ezekiel annoyed
            e "Quit playing, genuinely. This is already giving me stress- stop adding on. My fan girls will ditch me and my aura will crash like the stock market during the great depression. I'm not even joking when I say I'll beat your-"
            show ezekiel speaking
            d "woah woah, calm down petty pink princess, you'll be safe. Take a deep breath."
            show ezekiel annoyed
            e "Whatever"
            show ezekiel speaking
            l "On the bright side at least we can use the bathroom? If we need"
            show horatio annoyed
            h "Thanks for the genuine moral support, truly appreciate it"
            show horatio speaking
            show ezekiel annoyed
            e "Yea lance, that fixes everything!"
            show ezekiel speaking
            k "Hey, at least he's trying to be supportive and positive"
            e "…Yea you're right, my bad Lance"
            "Narrator" "Lance nodded sheepishly"
            d "Yo, should we check the bathroom cabinets?"
            menu:
                "Check the bathroom cabinets?"
                "Yes":
                    k "Yes, let's do it."
                    "Narrator" "Kage opened the bathroom cabinet. Inside were the basic items such as a toothbrush, paste, toilet paper, however, there were a lot of pill bottles, and a small vial with a clear liquid."
                    scene bg vialcabinet
                    show kage speakingnormal
                    show horatio speaking
                    show lance speaking
                    show dion speaking
                    show ezekiel speaking
                    l "Wait, what's that vial?"
                    d "Bro…how are we supposed to know?"
                    l "I don't know? A wild guess?"
                    e "Oh! What if it's like holy water or something??"
                    d "Dude…why would such a house have something holy?"
                    e "in case things go wrong?"
                    h "Well that's not a completely trash idea"
                    menu:
                        "Take the vial?"
                        "Yes":
                            k "You know what? Let's take it. It won't hurt to keep"
                            h "Good thinking"
                            $ backpack.append("Vial");
                            $ list_backpack = ", ".join(backpack)
                            scene bg novialcabinet
                            show kage speakingnormal
                            show horatio speaking
                            show lance speaking
                            show dion speaking
                            show ezekiel speaking
                            l "Yea, let's go now please"
                            "Narrator" "Dion nodded and Ezekiel was happy to leave the nasty bathroom"
                        "No":
                            k "Let's leave. We shouldn't be here for this long."
                            h "Yea, let's just get out of this room."
                            e "Thank god. My nose was about to burn off."
                "No":
                    e "Can we just get out of this room? I swear I'm about to pass out because of the smell. It smells worse than Dion's farts, no joke."
                    d "What makes you think I won't stuff your face in the toilet?"
                    h "Let's just leave then"
            "Narrator" "The boys left the bathroom. But Kage had a strange deja vu of the house, but kept quiet."
            scene bg hauntedlivingroom     
        "Dining Room":
            scene bg lightdining
            show kage speakingnormal
            show horatio speaking
            show lance speaking
            show dion speaking
            show ezekiel speaking
            k "How about the dining room?"
            h "Why do the lights above keep flickering?"
            e "Nah the real question is how does this house even have electricity in the first place. This broke ahh house for real."
            k "Funny- that light was always weird when I was little"
            show ezekiel annoyed
            e "There you go again with the reminiscence. It truly freaking me out man"
            show ezekiel speaking
            h "Wait Kage? You've been here before?"
            k "What? No, but my childhood house was similar to this"
            e "Shut up, I see something under the table"
            menu:
                "Check under the table?"
                "Yes":
                    scene bg saltundertable
                    show kage speakingnormal
                    show horatio speaking
                    show lance speaking
                    show dion speaking
                    show ezekiel speaking
                    d "It looks to me like a bag of salt"
                    e "Swear it was some American who lived here. That salt is the only seasoning they use, that's why they got so much."
                    k "My mom BARELY put anything in our food….But then again she barely did anything for me."
                    e "Oh wow, lore drop"
                    h "You idiot. That's not the only reason salt is used. This is what they use to draw the symbols and outline protective areas."
                    e "Actually?"
                    show lance scared
                    l "I swear to god a cult maybe lived here"
                    show lance speaking
                    d "Do you think we should keep it? Is it some clue?"
                    k "Maybe"
                    menu:
                        "Pick up the salt?"
                        "Yes":
                            k "Let's keep it. I have a strange feeling that this all will lead to something"
                            $ backpack.append("Salt");
                            $ list_backpack = ", ".join(backpack)
                            scene bg underdiningtable
                            show kage speakingnormal
                            show horatio speaking
                            show lance speaking
                            show dion speaking
                            show ezekiel speaking
                        "No":
                            k "I don't know- I have a feeling bad things may happen"
                            d "Just keep it there then."
                "No":
                    e "Bruh I'm not checking under that table. The times I check under the table I see the most diabolical chewed up gum stuck. What if instead of gum I see teeth or eyes."
                    l "Yea, let's leave this be"
                    h "Valid, only god knows what growing on that wood"
                    d "I don't think it's worth it,At this point we should be working to leave this house."
                    e "Yes finally. I don't wanna be stuck in this ghetto house anymore. Can we please leave before my manicure gets wrecked?"
            "Narrator" "The boys decided to leave the dining room."
            scene bg hauntedlivingroom 
    "Narrator" "While leaving the room Lance saw a staircase leading down somewhere."
    scene bg basementstairs
    show kage speakingnormal
    show horatio speaking
    show lance speaking
    show dion speaking
    show ezekiel speaking
    l "Hey where do you guys think these stairs lead to?"
    k "The basement?"
    e "How did you know that? Have you been here before? Tell me the truth before I make Dion throw you down those stairs."
    h "Ezekiel when you were born were you thrown on the ground by the doctor or something. Most houses have staircases which lead to the basement. I fear it's common sense."
    "Narrator" "Dion chuckled and Lance held in his laugh"
    l "Well then should we go down and check what's there maybe we can find something to get us out of this house!"
    h "That's actually not a bad plan, but we need to be careful."
    k "Are we sure guys?What if we see something or there's something down there waiting for us?"
    e "Then Dion can go first.He's the one with the muscles anyway he can wrestle with the ghost if anything happens."
    d "Don't even, I'll throw you in the basement and make you one with the ghost or something."
    menu:
        "Go down to the basement?"
        "Yes":
            h "Fine. But if we go we go together"
            e "What do you think this is no troll left behind?"
            k "Of course, If anything happens we can all try to save each other."
            show lance scared
            "Narrator" "Lance opened the door to the basement and walked in. Suddenly, the basement door slammed shut behind Lance.  Lance looks around, panicking. He's not the strongest soldier for this situation. The others are shocked and are debating whether to go in."
            scene bg basementdoor
            show horatio speaking
            show lance speaking
            show dion speaking
            show ezekiel speaking
            d "Guys we have to break in!"
            e "Yeah guys he's all alone in there!"
            "Narrator" "Dion tried to break open the door with all his might. To the point he got scratches. They could hear Lance panicking on the other side."
            show dion scared
            d "It is not budging!"
            show horatio scared
            h "Lance! Look around the room! Is there anything you can use to break open this door?!"
            l "I-I'll try to look around!"
            "Narrator" "Lance walked around the basement shaking in fear while trying to find something heavy to break the door. In the corner of his eye, he saw a wooden box. Lance walked closer to the box expecting there to be a weapon to use. When he opened the box, he saw a dusty book titled “Liber Aeternum”. Lance hesitantly picked up the book. As he flipped through the pages, he read that the objects that we've been collecting would be used to reverse a curse."
            scene bg lightbasement
            show lance speaking
            show woman droopy
            "Narrator" "Suddenly, Lance heard a woman laughing. A cold chill went up his spine. All of a sudden, he saw a beautiful woman. The woman looked somewhat familiar to Lance"
            show lance scared
            l "w-who are you?"
            "Narrator" "The woman didn't respond. The basement lights flickered and turned off. Lance heard some bones cracking."
            scene bg darkbasement
            scene bg lightbasement
            scene bg darkbasement
            scene bg lightbasement
            scene bg darkbasement
            show lance speaking
            show woman grey
            "Bone Cracking Sound"

            l "H-hello?"
            "Narrator" "The lights turned back on. The woman was much taller, her body much more skinnier. To the point you see her bones."
            scene bg lightbasement
            show lance speaking
            show lance scared
            l "P-please leave me alone"
            "Narrator" "The lights went off again, the cracking of bones got louder. When the lights turned on, the woman was on all fours like an animal, glaring at Lance. Lance got scared and backed up in fear, screaming."
            scene bg darkbasement with Pause(1)
            scene bg lightbasement
            "Bone Cracking & Screaming"

            "Narrator" "Meanwhile the boys on the other side of the door hear Lance's screams and begin to panic. They try their hardest to break open. When suddenly a riddle is carved into the door."
            scene bg hauntedlivingroom with pause(0.5)
            scene bg whitedoor with pause (3)
            show kage speakingnormal
            show horatio speaking
            show lance speaking
            show dion speaking
            show ezekiel speaking
            show dion mad
            d "You're kidding…we have to answer this?!"
            h "mhmm…there could be many answers…"
            e "Um…is it literature?"
            h "Could be…since old literature holds thousands of names of those who've died."
            d "Oh! Could it be historical moments? People have died and are taught to us in school!"
            h "Maybe it's a graveyard?"
            "Narrator" "The boys started arguing what the answer was, when all of a sudden they turned to Kage."
            h "What do you think Kage? You should choose and answer"
            menu:
                "What do you write?"
                "Literature":
                    k "Literature!"
                    "Narrator" "The door shined red and a woman's laugh was heard."
                    scene bg reddoor
                    show dion speaking
                    show ezekiel speaking
                    show woman droopy
                    w "Wrong answer"
                    "Narrator" "Lance's screams got louder and louder. Then pin drop silence."
                    d "Lance?! Lance!! Can you hear us?! Say something!!!"
                    e "Stop this Lance! Please say something!"
                    "Narrator" "After 5 minutes the door unlocked. The boys quickly went down the stairs to see Lance."
                    scene bg lightbasement
                    show horatio speaking
                    "Narrator" "They found Lance. But it was far too late…"
                    "Narrator" "In Lance's hand, was the book. Horatio, tears in his eyes, went closer. Their dear friend, Lance, now folded like an origami. In his hand, was the book. They boys went closer, crying, scared, and panicked. They mourned the loss of Lance quite dearly."
                    "Narrator" "Horatio gently picked up the book"
                    h "We should leave… it's got one of us, we can't let it get another…"
                    "Narrator" "The boys quietly agreed and headed upstairs"
                    scene bg hauntedlivingroom
                "Historical Moments":
                    k "Historical Moments!"
                    "Narrator" "The door shined red and a woman's laugh was heard."
                    scene bg reddoor
                    show dion speaking
                    show ezekiel speaking
                    show woman droopy
                    w "Wrong answer"
                    "Narrator" "Lance's screams got louder and louder. Then pin drop silence."
                    d "Lance?! Lance!! Can you hear us?! Say something!!!"
                    e "Stop this Lance! Please say something!"
                    "Narrator" "After 5 minutes the door unlocked. The boys quickly went down the stairs to see Lance."
                    scene bg lightbasement
                    show horatio speaking
                    "Narrator" "They found Lance. But it was far too late…"
                    "Narrator" "In Lance's hand, was the book. Horatio, tears in his eyes, went closer. Their dear friend, Lance, now folded like an origami. In his hand, was the book. They boys went closer, crying, scared, and panicked. They mourned the loss of Lance quite dearly."
                    "Narrator" "Horatio gently picked up the book"
                    h "We should leave… it's got one of us, we can't let it get another…"
                    "Narrator" "The boys quietly agreed and headed upstairs"
                    scene bg hauntedlivingroom
                "Graveyard":
                    k "A graveyard!"
                    "Narrator" "The door shined green and gently started creaking open. Kage immediately ran in and saw the scene. Lance being backed up into a corner and the monster of a woman. That woman's mutilated face was so familiar…"
                    scene bg greendoor
                    show kage shockedspeaking
                    k "m-mom?..."
                    w "What? You assumed that I would come even in the afterlife to check on my son? I see even you have decided to join the land of the dead."
                    "Narrator" "The ghost instantly vanished."
                    d "Y-y-y-you're a GHOST!!!"
                    e "A-a-And she's your MOTHER!!!"
                    h "That means we're probably in your childhood home"
                    k "You got that right"
                    "Narrator" "The boys ran to Lance, checking up on him"
                    e "Are you okay?! Are you hurt?!"
                    h "Did she say anything to you?!"
                    "Narrator" "Dion checked Lance's arms and legs to see if he was hurt. There wasa large cut on Lance's leg"
                    d "You're bleeding"
                    e "Quick check your bag Kage!"  
                    menu:
                        "Check bag?"
                        "Yes":
                            menu:
                                "[backpack[0]]":
                                    if [backpack[0]] == "Alcohol":
                                        "Narrator" "Kage poured the alcohol on Lances' wound then ripped his hoodie and wrapped it around Lance's leg."
                                    elif [backpack[0]] == "Flashlight":
                                        w "No use, you going to shine on the wound?"
                                        "Narrator" "Lance's wound got an infection and cannot walk properly"
                                    elif [backpack[0]] == "Cameras":
                                        w "No use, yea and post it on insta #leginjury"
                                        "Narrator" "Lance's wound got an infection and cannot walk properly"
                                    elif [backpack[0]] == "Pocket Knife":
                                        w "No use, make it worse, not like it's your leg anyways"
                                        "Narrator" "Lance's wound got an infection and cannot walk properly"
                                    elif [backpack[0]] == "Sleeping Bag":
                                        w "No use, lol sleep it off buddy"
                                        "Narrator" "Lance's wound got an infection and cannot walk properly"
                                    else:
                                        w "No use, gamble with the wound"
                                        "Narrator" "Lance's wound got an infection and cannot walk properly"
                                "[backpack[1]]":
                                    if [backpack[1]] == "Alcohol":
                                        "Narrator" "Kage poured the alcohol on Lances' wound then ripped his hoodie and wrapped it around Lance's leg."
                                    elif [backpack[1]] == "Flashlight":
                                        w "No use, you going to shine on the wound?"
                                        "Narrator" "Lance's wound got an infection and cannot walk properly"
                                    elif [backpack[1]] == "Cameras":
                                        w "No use, yea and post it on insta #leginjury"
                                        "Narrator" "Lance's wound got an infection and cannot walk properly"
                                    elif [backpack[1]] == "Pocket Knife":
                                        w "No use, make it worse, not like it's your leg anyways"
                                        "Narrator" "Lance's wound got an infection and cannot walk properly"
                                    elif [backpack[1]] == "Sleeping Bag":
                                        w "No use, lol sleep it off buddy"
                                        "Narrator" "Lance's wound got an infection and cannot walk properly"
                                    else:
                                        w "No use, gamble with the wound"
                                        "Narrator" "Lance's wound got an infection and cannot walk properly"
                                "[backpack[2]]":
                                    if [backpack[2]] == "Alcohol":
                                        "Narrator" "Kage poured the alcohol on Lances' wound then ripped his hoodie and wrapped it around Lance's leg."
                                    elif [backpack[2]] == "Flashlight":
                                        w "No use, you going to shine on the wound?"
                                        "Narrator" "Lance's wound got an infection and cannot walk properly"
                                    elif [backpack[2]] == "Cameras":
                                        w "No use, yea and post it on insta #leginjury"
                                        "Narrator" "Lance's wound got an infection and cannot walk properly"
                                    elif [backpack[2]] == "Pocket Knife":
                                        w "No use, make it worse, not like it's your leg anyways"
                                        "Narrator" "Lance's wound got an infection and cannot walk properly"
                                    elif [backpack[2]] == "Sleeping Bag":
                                        w "No use, lol sleep it off buddy"
                                        "Narrator" "Lance's wound got an infection and cannot walk properly"
                                    else:
                                        w "No use, gamble with the wound"
                                        "Narrator" "Lance's wound got an infection and cannot walk properly"
                                "[backpack[3]]":
                                    if [backpack[3]] == "Alcohol":
                                        "Narrator" "Kage poured the alcohol on Lances' wound then ripped his hoodie and wrapped it around Lance's leg."
                                    elif [backpack[3]] == "Flashlight":
                                        w "No use, you going to shine on the wound?"
                                        "Narrator" "Lance's wound got an infection and cannot walk properly"
                                    elif [backpack[3]] == "Cameras":
                                        w "No use, yea and post it on insta #leginjury"
                                        "Narrator" "Lance's wound got an infection and cannot walk properly"
                                    elif [backpack[3]] == "Pocket Knife":
                                        w "No use, make it worse, not like it's your leg anyways"
                                        "Narrator" "Lance's wound got an infection and cannot walk properly"
                                    elif [backpack[3]] == "Sleeping Bag":
                                        w "No use, lol sleep it off buddy"
                                        "Narrator" "Lance's wound got an infection and cannot walk properly"
                                    else:
                                        w "No use, gamble with the wound"
                                        "Narrator" "Lance's wound got an infection and cannot walk properly"
                        "No":
                            "Narrator" "Lance's wound got an infection and cannot walk properly."
                    "Narrator" "Kage examines the book in Lance's hand "
                    k "What's that?"
                    l "A book I found in there"
                    h "Let's read it when we get out of here."
                    "Narrator" "The boys quietly agreed and headed upstairs"
                    scene bg hauntedlivingroom
                    show kage speakingnormal
                    k "Ok, lets head to the living room where our setup is"
                    "Narrator" "The boys sat down in the living room, Lance holding the book. Lance flipped through the book, and everyone found out that the previous family living here was a family of three, parents and their teen son."
                    scene bg lightsofa
                    show lance speaking
                    show kage speakingnormal
                    "Narrator" "Apparently the two people were the father, Cassian, and the mother,Victoria. The two were popular cultists who performed rituals weekly. They've performed many dark deeds such as sacrifices, murders, and conspiracies."
                    "Narrator" "As Lance kept flipping, one page caught his eye and he froze."
                    k "What does the book say Lance?"
                    show lance shocked
                    l "It's a picture of you, “Victoria and Cassian's son…Kage"
                    "Narrator" "Everyone paused, the lights flicked violently as the house shaked."
                    scene bg darksofa
                    scene bg lightsofa
                    scene bg darksofa
                    scene bg lightsofa
                    scene bg darksofa
                    scene bg lightsofa
                    show kage speakingnormal
                    show horatio speaking
                    show lance speaking
                    show dion speaking
                    show ezekiel speaking
                    h "Quick! Look if there's something about this ritual before anything happens!"
                    l "Lance started flipping around in the book faster trying to find an answer, until he saw it. They needed a silver dagger, a vial that contained holy water, the cross, and the salt. They needed to put all four items within the pentagram."
                    if len(backpack) == 8:
                        l "I am reading right now, and there are instructions on how to do this ritual to break the curse!"
                        k "What is it?!"
                        show lance mad
                        l "Put all the objects we found in the pentagram and then we take the names of the ghosts and burn the house! Hurry!"
                        "Narrator" "Kage dropped all the items in the pentagram. The moment all the objects fell on the pentagram, it glowed a vibrant red. The ground started shaking even more violently."
                        scene bg pentagramitems
                        show kage speakingnormal
                        show horatio speaking
                        "Narrator" "Kage feels an odd sensation throughout his body. He can't tell clearly why it is happening. Then it hits him. He is the one that has been cursed the entire time"
                        show kage sadspeaking at center
                        k "All this time it was me. I was carrying the curse. I can't believe it."
                        h "Kage! Call out their names!"
                        k "Cassian! Victoria!!"
                        "Narrator" "Shrieks of a man and woman were heard all throughout the house. The frames on the walls began shaking till they fell down and crashed. Furniture slid across the rooms savagely."
                        scene bg messybrokenlivingroom
                        show horatio speaking at slightleft
                        show lance speaking at left
                        show dion speaking at slightright
                        show ezekiel speaking at right
                        "Shrieks"

                        h "We need to light this place up!"
                        e "The kitchen!"
                        h "What does the kitchen have to do with this?!"
                        e "Don't old houses have gas stoves? Just light it on fire!!"
                        h "… oh… that's quite smart of you"
                        d "Can y'all stop acting like friendship is magic?! We are gonna die in this house!"
                        l "I think I'm going to die in this…HOUSE"
                        "Narrator" "The boys went to the kitchen, opening the cabinet to find the gas tub."
                        scene bg kitchencabinetopen
                        show kage speakingnormal at center
                        show horatio speaking at slightleft
                        show lance speaking at left
                        show dion speaking at slightright
                        show ezekiel speaking at right
                        h "We need a lighter!"
                        menu:
                            "Which cabinet contains the lighter?"
                            "Cabinet 1 - Has a Star":
                                d "Found one!"
                                h "Let's light this place up!"
                                "Narrator" "The whole house suddenly catches fire, the boys make a run for the front door to escape."
                                scene bg hallwayfire
                                "Narrator" "Finally, the land on the cool grass."
                                h "In the car, NOW!"
                                "Narrator" "Congratulations!!! You broke the c-"
                                scene bg curse1
                                scene bg curse2
                                scene bg curse3
                                scene bg curse4
                                scene bg curse5
                                scene bg curse6
                            "Cabinet 2 - Has a Heart":
                                "Cassian & Victoria" "Wrong cabinet, remember what sign caused us to come to life..."
                                "Narrator" "The boys are consumed by the terrorizing ghosts of the past as they are brought benath the surface with them"
                                scene bg ghosties
                            "Cabinet 3 - Has a Blood Splatter":
                                "Cassian & Victoria" "Wrong cabinet, remember what sign caused us to come to life..."
                                "Narrator" "The boys are consumed by the terrorizing ghosts of the past as they are brought benath the surface with them"
                                scene bg ghosties
                    else:
                        "Narrator" "The boys immediately ran upstairs trying to seek shelter from the chaos of the house. The boys looked at the stairs leading upstairs, the way was dark."
                        scene bg darkupstairs
                        show ezekiel speaking at right
                        show dion speaking at slightright
                        show horatio speaking at slightleft
                        e "You think there's a bedroom up there?"
                        d "You want a bedroom? Here??!"
                        e "If we find one we find one you know!"
                        h "It's too dark. Kage, did you pack something that might help?! Quick!"
                        menu:
                            "[backpack[0]]":
                                if backpack[0] == "Flashlight":
                                    "Narrator" "You succesfully use the flashlight to light the staircase"
                                    scene bg lightupstairs
                                elif backpack[0] == "Alcohol":
                                    "Narrator" "No use, you going to clean the stairs with it or something?"
                                    "Narrator" "You have to go up the stairs in complete darkness. Ezekiel trips and falls on his face, accidentally breaking his nose."
                                    scene bg darkupstairs
                                    e "OW! Uhgh it hurts!!"
                                    "Narrator" "Horatio quickly puts his hoodie to Ezekiel's nose to slow the bleeding"
                                    e "My perfect nose!!!"
                                    "Narrator" "They made it upstairs, but at what cost?"
                                elif backpack[0] == "Cameras":
                                    "Narrator" "No use, go ahead and take a selfie with the staircase. Great going genius."
                                    "Narrator" "You have to go up the stairs in complete darkness. Ezekiel trips and falls on his face, accidentally breaking his nose."
                                    scene bg darkupstairs
                                    e "OW! Uhgh it hurts!!"
                                    "Narrator" "Horatio quickly puts his hoodie to Ezekiel's nose to slow the bleeding"
                                    e "My perfect nose!!!"
                                    "Narrator" "They made it upstairs, but at what cost?"
                                elif backpack[0] == "Pocket Knife":
                                    "Narrator" "No use, perfect go cut up the stairs"
                                    "Narrator" "You have to go up the stairs in complete darkness. Ezekiel trips and falls on his face, accidentally breaking his nose."
                                    scene bg darkupstairs
                                    e "OW! Uhgh it hurts!!"
                                    "Narrator" "Horatio quickly puts his hoodie to Ezekiel's nose to slow the bleeding"
                                    e "My perfect nose!!!"
                                    "Narrator" "They made it upstairs, but at what cost?"
                                elif backpack[0] == "Sleeping Bag":
                                    "Narrator" "No use, already snoozing"
                                    "Narrator" "You have to go up the stairs in complete darkness. Ezekiel trips and falls on his face, accidentally breaking his nose."
                                    scene bg darkupstairs
                                    e "OW! Uhgh it hurts!!"
                                    "Narrator" "Horatio quickly puts his hoodie to Ezekiel's nose to slow the bleeding"
                                    e "My perfect nose!!!"
                                    "Narrator" "They made it upstairs, but at what cost?"
                                else:
                                    "Narrator" "No use, gamble with the stairs?"
                                    "Narrator" "You have to go up the stairs in complete darkness. Ezekiel trips and falls on his face, accidentally breaking his nose."
                                    scene bg darkupstairs
                                    e "OW! Uhgh it hurts!!"
                                    "Narrator" "Horatio quickly puts his hoodie to Ezekiel's nose to slow the bleeding"
                                    e "My perfect nose!!!"
                                    "Narrator" "They made it upstairs, but at what cost?"
                            "[backpack[1]]":
                                if backpack[1] == "Flashlight":
                                    "Narrator" "You succesfully use the flashlight to light the staircase"
                                    scene bg lightupstairs
                                elif backpack[1] == "Alcohol":
                                    "Narrator" "No use, you going to clean the stairs with it or something?"
                                    "Narrator" "You have to go up the stairs in complete darkness. Ezekiel trips and falls on his face, accidentally breaking hisnose."
                                    scene bg darkupstairs
                                    e "OW! Uhgh it hurts!!"
                                    "Narrator" "Horatio quickly puts his hoodie to Ezekiel's nose to slow the bleeding"
                                    e "My perfect nose!!!"
                                    "Narrator" "They made it upstairs, but at what cost?"
                                elif backpack[1] == "Cameras":
                                    "Narrator" "No use, go ahead and take a selfie with the staircase. Great going genius."
                                    "Narrator" "You have to go up the stairs in complete darkness. Ezekiel trips and falls on his face, accidentally breaking his nose."
                                    scene bg darkupstairs
                                    e "OW! Uhgh it hurts!!"
                                    "Narrator" "Horatio quickly puts his hoodie to Ezekiel's nose to slow the bleeding"
                                    e "My perfect nose!!!"
                                    "Narrator" "They made it upstairs, but at what cost?"
                                elif backpack[1] == "Pocket Knife":
                                    "Narrator" "No use, perfect go cut up the stairs"
                                    "Narrator" "You have to go up the stairs in complete darkness. Ezekiel trips and falls on his face, accidentally breaking his nose."
                                    scene bg darkupstairs
                                    e "OW! Uhgh it hurts!!"
                                    "Narrator" "Horatio quickly puts his hoodie to Ezekiel's nose to slow the bleeding"
                                    e "My perfect nose!!!"
                                    "Narrator" "They made it upstairs, but at what cost?"
                                elif backpack[1] == "Sleeping Bag":
                                    "Narrator" "No use, already snoozing"
                                    "Narrator" "You have to go up the stairs in complete darkness. Ezekiel trips and falls on his face, accidentally breaking his nose."
                                    scene bg darkupstairs
                                    e "OW! Uhgh it hurts!!"
                                    "Narrator" "Horatio quickly puts his hoodie to Ezekiel's nose to slow the bleeding"
                                    e "My perfect nose!!!"
                                    "Narrator" "They made it upstairs, but at what cost?"
                                else:
                                    "Narrator" "No use, gamble with the stairs?"
                                    "Narrator" "You have to go up the stairs in complete darkness. Ezekiel trips and falls on his face, accidentally breaking his nose."
                                    scene bg darkupstairs
                                    e "OW! Uhgh it hurts!!"
                                    "Narrator" "Horatio quickly puts his hoodie to Ezekiel's nose to slow the bleeding"
                                    e "My perfect nose!!!"
                                    "Narrator" "They made it upstairs, but at what cost?"
                            "[backpack[2]]":
                                if backpack[2] == "Flashlight":
                                    "Narrator" "You succesfully use the flashlight to light the staircase"
                                    scene bg lightupstairs
                                elif backpack[2] == "Alcohol":
                                    "Narrator" "No use, you going to clean the stairs with it or something?"
                                    "Narrator" "You have to go up the stairs in complete darkness. Ezekiel trips and falls on his face, accidentally breaking hisnose."
                                    scene bg darkupstairs
                                    e "OW! Uhgh it hurts!!"
                                    "Narrator" "Horatio quickly puts his hoodie to Ezekiel's nose to slow the bleeding"
                                    e "My perfect nose!!!"
                                    "Narrator" "They made it upstairs, but at what cost?"
                                elif backpack[2] == "Cameras":
                                    "Narrator" "No use, go ahead and take a selfie with the staircase. Great going genius."
                                    "Narrator" "You have to go up the stairs in complete darkness. Ezekiel trips and falls on his face, accidentally breaking his nose."
                                    scene bg darkupstairs
                                    e "OW! Uhgh it hurts!!"
                                    "Narrator" "Horatio quickly puts his hoodie to Ezekiel's nose to slow the bleeding"
                                    e "My perfect nose!!!"
                                    "Narrator" "They made it upstairs, but at what cost?"
                                elif backpack[2] == "Pocket Knife":
                                    "Narrator" "No use, perfect go cut up the stairs"
                                    "Narrator" "You have to go up the stairs in complete darkness. Ezekiel trips and falls on his face, accidentally breaking his nose."
                                    scene bg darkupstairs
                                    e "OW! Uhgh it hurts!!"
                                    "Narrator" "Horatio quickly puts his hoodie to Ezekiel's nose to slow the bleeding"
                                    e "My perfect nose!!!"
                                    "Narrator" "They made it upstairs, but at what cost?"
                                elif backpack[2] == "Sleeping Bag":
                                    "Narrator" "No use, already snoozing"
                                    "Narrator" "You have to go up the stairs in complete darkness. Ezekiel trips and falls on his face, accidentally breaking his nose."
                                    scene bg darkupstairs
                                    e "OW! Uhgh it hurts!!"
                                    "Narrator" "Horatio quickly puts his hoodie to Ezekiel's nose to slow the bleeding"
                                    e "My perfect nose!!!"
                                    "Narrator" "They made it upstairs, but at what cost?"
                                else:
                                    "Narrator" "No use, gamble with the stairs?"
                                    "Narrator" "You have to go up the stairs in complete darkness. Ezekiel trips and falls on his face, accidentally breaking his nose."
                                    scene bg darkupstairs
                                    e "OW! Uhgh it hurts!!"
                                    "Narrator" "Horatio quickly puts his hoodie to Ezekiel's nose to slow the bleeding"
                                    e "My perfect nose!!!"
                                    "Narrator" "They made it upstairs, but at what cost?"
                            "[backpack[3]]":
                                if backpack[3] == "Flashlight":
                                    "Narrator" "You succesfully use the flashlight to light the staircase"
                                    scene bg lightupstairs
                                elif backpack[3] == "Alcohol":
                                    "Narrator" "No use, you going to clean the stairs with it or something?"
                                    "Narrator" "You have to go up the stairs in complete darkness. Ezekiel trips and falls on his face, accidentally breaking his nose."
                                    scene bg darkupstairs
                                    e "OW! Uhgh it hurts!!"
                                    "Narrator" "Horatio quickly puts his hoodie to Ezekiel's nose to slow the bleeding"
                                    e "My perfect nose!!!"
                                    "Narrator" "They made it upstairs, but at what cost?"
                                elif backpack[3] == "Cameras":
                                    "Narrator" "No use, go ahead and take a selfie with the staircase. Great going genius."
                                    "Narrator" "You have to go up the stairs in complete darkness. Ezekiel trips and falls on his face, accidentally breaking his nose."
                                    scene bg darkupstairs
                                    e "OW! Uhgh it hurts!!"
                                    "Narrator" "Horatio quickly puts his hoodie to Ezekiel's nose to slow the bleeding"
                                    e "My perfect nose!!!"
                                    "Narrator" "They made it upstairs, but at what cost?"
                                elif backpack[3] == "Pocket Knife":
                                    "Narrator" "No use, perfect go cut up the stairs"
                                    "Narrator" "You have to go up the stairs in complete darkness. Ezekiel trips and falls on his face, accidentally breaking his nose."
                                    scene bg darkupstairs
                                    e "OW! Uhgh it hurts!!"
                                    "Narrator" "Horatio quickly puts his hoodie to Ezekiel's nose to slow the bleeding"
                                    e "My perfect nose!!!"
                                    "Narrator" "They made it upstairs, but at what cost?"
                                elif backpack[3] == "Sleeping Bag":
                                    "Narrator" "No use, already snoozing"
                                    "Narrator" "You have to go up the stairs in complete darkness. Ezekiel trips and falls on his face, accidentally breaking his nose."
                                    scene bg darkupstairs
                                    e "OW! Uhgh it hurts!!"
                                    "Narrator" "Horatio quickly puts his hoodie to Ezekiel's nose to slow the bleeding"
                                    e "My perfect nose!!!"
                                    "Narrator" "They made it upstairs, but at what cost?"
                                else:
                                    "Narrator" "No use, gamble with the stairs?"
                                    "Narrator" "You have to go up the stairs in complete darkness. Ezekiel trips and falls on his face, accidentally breaking his nose."
                                    scene bg darkupstairs
                                    e "OW! Uhgh it hurts!!"
                                    "Narrator" "Horatio quickly puts his hoodie to Ezekiel's nose to slow the bleeding"
                                    e "My perfect nose!!!"
                                    "Narrator" "They made it upstairs, but at what cost?"
                                scene bg firstupstairs
        "No":
            k "Let's not. The main goal is to survive and get out of this house."
            d "You're right."
            h "I say we all stick together, go find a room, and sleep there."
            "Narrator" "The boys looked at the stairs leading upstairs, the way was dark."
            scene bg darkupstairs
            show ezekiel speaking at right
            show horatio speaking at slightleft
            show dion speaking at slightright
            e "You think there's a bedroom up there?"
            d "You want a bedroom? Here??!"
            e "If we find one we find one you know!"
            h "It's too dark. Kage, did you pack something that might help?! Quick!"
            menu:
                "[backpack[0]]":
                    if backpack[0] == "Flashlight":
                        "Narrator" "You succesfully use the flashlight to light the staircase"
                        scene bg lightupstairs
                    elif backpack[0] == "Alcohol":
                        "Narrator" "No use, you going to clean the stairs with it or something?"
                        "Narrator" "You have to go up the stairs in complete darkness. Ezekiel trips and falls on his face, accidentally breaking his nose."
                        scene bg darkupstairs
                        e "OW! Uhgh it hurts!!"
                        "Narrator" "Horatio quickly puts his hoodie to Ezekiel's nose to slow the bleeding"
                        e "My perfect nose!!!"
                        "Narrator" "They made it upstairs, but at what cost?"
                    elif backpack[0] == "Cameras":
                        "Narrator" "No use, go ahead and take a selfie with the staircase. Great going genius."
                        "Narrator" "You have to go up the stairs in complete darkness. Ezekiel trips and falls on his face, accidentally breaking his nose."
                        scene bg darkupstairs
                        e "OW! Uhgh it hurts!!"
                        "Narrator" "Horatio quickly puts his hoodie to Ezekiel's nose to slow the bleeding"
                        e "My perfect nose!!!"
                        "Narrator" "They made it upstairs, but at what cost?"
                    elif backpack[0] == "Pocket Knife":
                        "Narrator" "No use, perfect go cut up the stairs"
                        "Narrator" "have to go up the stairs in complete darkness. Ezekiel trips and falls on his face, accidentally breaking his nose."
                        scene bg darkupstairs
                        e "OW! Uhgh it hurts!!"
                        "Narrator" "Horatio quickly puts his hoodie to Ezekiel's nose to slow the bleeding"
                        e "My perfect nose!!!"
                        "Narrator" "They made it upstairs, but at what cost?"
                    elif backpack[0] == "Sleeping Bag":
                        "Narrator" "No use, already snoozing"
                        "Narrator" "You have to go up the stairs in complete darkness. Ezekiel trips and falls on his face, accidentally breaking his nose."
                        scene bg darkupstairs
                        e "OW! Uhgh it hurts!!"
                        "Narrator" "Horatio quickly puts his hoodie to Ezekiel's nose to slow the bleeding"
                        e "My perfect nose!!!"
                        "Narrator" "They made it upstairs, but at what cost?"
                    else:
                        "Narrator" "No use, gamble with the stairs?"
                        "Narrator" "You have to go up the stairs in complete darkness. Ezekiel trips and falls on his face, accidentally breaking his nose."
                        scene bg darkupstairs
                        e "OW! Uhgh it hurts!!"
                        "Narrator" "Horatio quickly puts his hoodie to Ezekiel's nose to slow the bleeding"
                        e "My perfect nose!!!"
                        "Narrator" "They made it upstairs, but at what cost?"
                "[backpack[1]]":
                    if backpack[1] == "Flashlight":
                        "Narrator" "You succesfully use the flashlight to light the staircase"
                    elif backpack[1] == "Alcohol":
                        "Narrator" "No use, you going to clean the stairs with it or something?"
                        "Narrator" "You have to go up the stairs in complete darkness. Ezekiel trips and falls on his face, accidentally breaking his nose."
                        scene bg darkupstairs
                        e "OW! Uhgh it hurts!!"
                        "Narrator" "Horatio quickly puts his hoodie to Ezekiel's nose to slow the bleeding"
                        e "My perfect nose!!!"
                        "Narrator" "They made it upstairs, but at what cost?"
                    elif backpack[1] == "Cameras":
                        "Narrator" "No use, go ahead and take a selfie with the staircase. Great going genius."
                        "Narrator" "You have to go up the stairs in complete darkness. Ezekiel trips and falls on his face, accidentally breaking his nose."
                        scene bg darkupstairs
                        e "OW! Uhgh it hurts!!"
                        "Narrator" "Horatio quickly puts his hoodie to Ezekiel's nose to slow the bleeding"
                        e "My perfect nose!!!"
                        "Narrator" "They made it upstairs, but at what cost?"
                    elif backpack[1] == "Pocket Knife":
                        "Narrator" "No use, perfect go cut up the stairs"
                        "Narrator" "You have to go up the stairs in complete darkness. Ezekiel trips and falls on his face, accidentally breaking his nose."
                        scene bg darkupstairs
                        e "OW! Uhgh it hurts!!"
                        "Narrator" "Horatio quickly puts his hoodie to Ezekiel's nose to slow the bleeding"
                        e "My perfect nose!!!"
                        "Narrator" "They made it upstairs, but at what cost?"
                    elif backpack[1] == "Sleeping Bag":
                        "Narrator" "No use, already snoozing"
                        "Narrator" "You have to go up the stairs in complete darkness. Ezekiel trips and falls on his face, accidentally breaking his nose."
                        scene bg darkupstairs
                        e "OW! Uhgh it hurts!!"
                        "Narrator" "Horatio quickly puts his hoodie to Ezekiel's nose to slow the bleeding"
                        e "My perfect nose!!!"
                        "Narrator" "They made it upstairs, but at what cost?"
                    else:
                        "Narrator" "No use, gamble with the stairs?"
                        "Narrator" "You have to go up the stairs in complete darkness. Ezekiel trips and falls on his face, accidentally breaking his nose."
                        scene bg darkupstairs
                        e "OW! Uhgh it hurts!!"
                        "Narrator" "Horatio quickly puts his hoodie to Ezekiel's nose to slow the bleeding"
                        e "My perfect nose!!!"
                        "Narrator" "They made it upstairs, but at what cost?"
                "[backpack[2]]":
                    if backpack[2] == "Flashlight":
                        "Narrator" "You succesfully use the flashlight to light the staircase"
                    elif backpack[2] == "Alcohol":
                        "Narrator" "No use, you going to clean the stairs with it or something?"
                        "Narrator" "You have to go up the stairs in complete darkness. Ezekiel trips and falls on his face, accidentally breaking hisnose."
                        scene bg darkupstairs
                        e "OW! Uhgh it hurts!!"
                        "Narrator" "Horatio quickly puts his hoodie to Ezekiel's nose to slow the bleeding"
                        e "My perfect nose!!!"
                        "Narrator" "They made it upstairs, but at what cost?"
                    elif backpack[2] == "Cameras":
                        "Narrator" "No use, go ahead and take a selfie with the staircase. Great going genius."
                        "Narrator" "You have to go up the stairs in complete darkness. Ezekiel trips and falls on his face, accidentally breaking his nose."



                        e "OW! Uhgh it hurts!!"
                        "Narrator" "Horatio quickly puts his hoodie to Ezekiel's nose to slow the bleeding"
                        e "My perfect nose!!!"
                        "Narrator" "They made it upstairs, but at what cost?"
                    elif backpack[2] == "Pocket Knife":
                        "Narrator" "No use, perfect go cut up the stairs"
                        "Narrator" "You have to go up the stairs in complete darkness. Ezekiel trips and falls on his face, accidentally breaking his nose."
                        scene bg darkupstairs
                        e "OW! Uhgh it hurts!!"
                        "Narrator" "Horatio quickly puts his hoodie to Ezekiel's nose to slow the bleeding"
                        e "My perfect nose!!!"
                        "Narrator" "They made it upstairs, but at what cost?"
                    elif backpack[2] == "Sleeping Bag":
                        "Narrator" "No use, already snoozing"
                        "Narrator" "You have to go up the stairs in complete darkness. Ezekiel trips and falls on his face, accidentally breaking his nose."
                        scene bg darkupstairs
                        e "OW! Uhgh it hurts!!"
                        "Narrator" "Horatio quickly puts his hoodie to Ezekiel's nose to slow the bleeding"
                        e "My perfect nose!!!"
                        "Narrator" "They made it upstairs, but at what cost?"
                    else:
                        "Narrator" "No use, gamble with the stairs?"
                        "Narrator" "You have to go up the stairs in complete darkness. Ezekiel trips and falls on his face, accidentally breaking his nose."
                        scene bg darkupstairs
                        e "OW! Uhgh it hurts!!"
                        "Narrator" "Horatio quickly puts his hoodie to Ezekiel's nose to slow the bleeding"
                        e "My perfect nose!!!"
                        "Narrator" "They made it upstairs, but at what cost?"
                "[backpack[3]]":
                    if backpack[3] == "Flashlight":
                        "Narrator" "You succesfully use the flashlight to light the staircase"
                    elif backpack[3] == "Alcohol":
                        "Narrator" "No use, you going to clean the stairs with it or something?"
                        "Narrator" "You have to go up the stairs in complete darkness. Ezekiel trips and falls on his face, accidentally breaking hisnose."
                        scene bg darkupstairs
                        e "OW! Uhgh it hurts!!"
                        "Narrator" "Horatio quickly puts his hoodie to Ezekiel's nose to slow the bleeding"
                        e "My perfect nose!!!"
                        "Narrator" "They made it upstairs, but at what cost?"
                    elif backpack[3] == "Cameras":
                        "Narrator" "No use, go ahead and take a selfie with the staircase. Great going genius."
                        "Narrator" "You have to go up the stairs in complete darkness. Ezekiel trips and falls on his face, accidentally breaking his nose."
                        scene bg darkupstairs
                        e "OW! Uhgh it hurts!!"
                        "Narrator" "Horatio quickly puts his hoodie to Ezekiel's nose to slow the bleeding"
                        e "My perfect nose!!!"
                        "Narrator" "They made it upstairs, but at what cost?"
                    elif backpack[3] == "Pocket Knife":
                        "Narrator" "No use, perfect go cut up the stairs"
                        "Narrator" "You have to go up the stairs in complete darkness. Ezekiel trips and falls on his face, accidentally breaking his nose."
                        scene bg darkupstairs
                        e "OW! Uhgh it hurts!!"
                        "Narrator" "Horatio quickly puts his hoodie to Ezekiel's nose to slow the bleeding"
                        e "My perfect nose!!!"
                        "Narrator" "They made it upstairs, but at what cost?"
                    elif backpack[3] == "Sleeping Bag":
                        "Narrator" "No use, already snoozing"
                        "Narrator" "You have to go up the stairs in complete darkness. Ezekiel trips and falls on his face, accidentally breaking his nose."
                        scene bg darkupstairs
                        e "OW! Uhgh it hurts!!"
                        "Narrator" "Horatio quickly puts his hoodie to Ezekiel's nose to slow the bleeding"
                        e "My perfect nose!!!"
                        "Narrator" "They made it upstairs, but at what cost?"
                    else:
                        "Narrator" "No use, gamble with the stairs?"
                        "Narrator" "You have to go up the stairs in complete darkness. Ezekiel trips and falls on his face, accidentally breaking his nose."
                        scene bg darkupstairs
                        e "OW! Uhgh it hurts!!"
                        "Narrator" "Horatio quickly puts his hoodie to Ezekiel's nose to slow the bleeding"
                        e "My perfect nose!!!"
                        "Narrator" "They made it upstairs, but at what cost?"
    "Narrator" "Everyone is on the second floor where a single door is left."
    menu:
        "Open the door?"
        "Yes":
            scene bg firstupstairs
            show kage speakingnormal at center
            show ezekiel speaking at right
            k "Ugh it's so musty here…"
            show ezekiel happy at right
            e "Oh my, and who's this? Man, do I look good!"
            show ezekiel speaking at right
            scene bg initialmirror
            "Narrator" "As Ezekiel looks at himself, Ezekiel's reflection suddenly begins to change and morph in an irregular manner. It started smiling back at him, ear to ear. Waving Hi to Ezekiel."
            show ezra p1 at left
            show ezra p2 at left
            show ezra p3 at left
            e "Woah- what the"
            show ezekiel shocked at right
            "Narrator" "The ghost transforms into Kage's father. The ghost then starts lunging towards him"
            k "Ezekiel watch out!!"
            show thedad mirror at left
            "Narrator" "The ghost drags Ezekiel into the mirror. The mirror turns into a picture. Ezekiel is no longer flesh but canvas, his pulse traded for perfection. He hangs in silent splendor --  forever radiant, forever admired,
and forever without breath."
            scene bg dragezeinmirror at left
            show ezekiel art at left
            "Narrator" "The three boys left made a run for it, racing down the stairs back to the living room, it seems as if no place in the house can be safe and secure."
            scene bg livingroomfromabove
        "No":
            h "Guys, I think we should get out of here"
            d "Yea, I don't think I can even sleep or stay here any longer."
            e "You know what? Can't we use a hammer and break out?"
            l "Yea… why didn't we think of that guys?"
            h "Guys…We have phones… we could've called help"
            k "We're actual idiots…"
            "Narrator" "Like the geniuses they are, they finally called the cops, their parents, basically everyone and their mothers to come help them. Now all they had to do was stick together, and survive."
            e "Did we pack any cards?"
            h "Don't make me punch you"
            e "Hey! To pass time!"
            d "You know, why not?"
            l "Do you have cards Kage?"
            if backpack[0] == "Cards" or backpack[1] == "Cards" or backpack[2] == "Cards" or backpack[3] == "Cards":
                "Narrator" "You found a deck of cards, you start playing solitaire with your friends. You play cards with your friends, and spend the night until the help arrives!"
            else:
                "Narrator" "You don't have any cards, you just sit there and wait for help to arrive. You spend the night bored until the help arrives!"
            "Narrator" "After 15 minutes, police sirens gradually start blaring louder. Pretty soon the lights red and blue were shining. The police broke down the door"
            scene bg blankupstairroom
            show ezekiel speaking at right
            e "They're here! We can finally leave!"
            "Narrator" "The guys ran in pure bliss, running into the safe arms of the cops."
            scene bg policeinhouse
            show ezekiel shocked at right
            show horatio shocked at slightleft
            show dion shocked at slightright
            "Cop" "So what were you four doing in this house?"
            e "Ugh sir you have no idea! Our friend Kage wanted to go haunted house hunting and showed us this location"
            h "Wait, sir? What do you mean by four, there's five of us?"
            "Cop" "No kiddo, there's only you four in this car."
            "Narrator" "The boys looked around and didn't see Kage and started freaking out"
            h "Where's Kage?! Did we forget him?!"
            "Cop" "Wait wait, Kage? As in the son of Victoria and Cassian, that freakshow of a family? He's been dead for years, kids. Are all of you on something?"
            "Narrator" "The boys were shocked, none could utter a single word. The boy that they've considered their friend…was never real."
            d "T-then who was with us the whole time?"
