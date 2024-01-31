
# Wason Task
# Classic version
wason_classic = "Check the following rule: "\
                "If there is a vowel on one side of the card, there is an even number on the other side. You see four cards now: "\
                "a) E; b) K; c)	4; d) 7. Which of these cards must in any case be turned over to check the rule? "\
                "(In other words: which cards could violate the rule above?) "\
                "a)	E; b) K; c)	4; d) 7"

# Context version
wason_context = "Imagine that you are working for the post office. You are responsible for checking whether the right stamp is affixed to a letter. "\
                "The following rule applies:"\
                "If a letter is sent to the USA, at least one 90-cent stamp must be affixed to it. "\
                "There are four letters in front of you, of which you can see either the front or the back."\
                "a)	Letter 1: 90-cent stamp on the front; b) Letter 2: Italy marked on the back; c)	Letter 3: 50-cents stamp on the front; d) Letter 4: USA marked on the back."\
                "Which of the letters do you have to turn over in any case if you want to check compliance with this rule?"\
                "a)	Letter 1; b) Letter 2; c) Letter 3; d) Letter 4"

# AIDS Test
# Classic version
aids_classic = "The probability that someone is infected with HIV is 0.01%. "\
               "The test recognizes HIV virus with 100% probability if it is present. "\
               "So, the test is positive. The probability of getting a positive test result when you don’t really have the virus is only 0.01%." \
               "The test result for your friend is positive. The probability that your friend is infected with the HIV virus is therefore: _______ %"

aids_freq = "This task involves an assessment of the results of the AIDS test. It is known that HIV can cause AIDS. "\
            "Now imagine the following: A friend of yours gave blood at the hospital. It will then be checked to see if HIV is present in the blood. "\
            "The test result is positive. How likely is it that your friend is actually infected with the HIV?" \
            "To answer this question, you will need the following information:"\
            "Out of 10,000 people, 1 person is infected with HIV. If the person is infected with the HIV, the test detects HIV. "\
            "So the test is positive. Only 1 of the 9,999 people who are not infected with HIV have a positive test." \
            "The test result for your friend is positive. How many people who have received a positive test result are actually infected with HIV? _______ from _______."

# Hospital problem
hospital = "In hospital A about 100 children are born per month. In hospital B about 10 children are born per month. The probability of the birth of a boy or a girl is about 50 percent each." \
           "Which of the following statements is right, which is wrong?" \
           "The probability that once in a month more than 60 percent of boys will be born is…" \
           "a)… larger in hospital A" \
           "b)… larger in hospital B" \
           "c)… equally big in both hospitals"

# Monty Hall problem
monty_short = "A candidate on a quiz show can choose one of three doors. Behind one of the doors is the main prize, a car. "\
              "Behind the other two doors, there are two goats. The rules of the game are now as follows: "\
              "The quizmaster knows behind which of the doors the car and the goats are. After the candidate has chosen one of the doors, it remains locked for the time being. "\
              "The quizmaster then opens one of the other two doors. He always opens a door with a goat behind it."\
              "Imagine that the candidate chooses door 1. Instead of opening this door, the quizmaster opens another door, behind which there is a goat. "\
              "He now offers the candidate the option of switching his choice to the last unopened door. Should the candidate switch to the door or not?"

monty_long = "A candidate on a quiz show can choose one of three doors. Behind one of the doors is the main prize, a car. "\
             "Behind the other two doors, there are two goats. The rules of the game are now as follows: "\
             "The quizmaster knows behind which of the doors the car and the goats are. After the candidate has chosen one of the doors, it remains locked for the time being. "\
             "The quizmaster then opens one of the other two doors. He always opens a door with a goat behind it." \
             "Imagine that the candidate chooses door 1. Instead of opening this door, the quizmaster opens another door, behind which there is a goat. "\
             "He now offers the candidate the option of switching his choice to the last unopened door. Should the candidate switch to the door or not?" \
             "There are only three possible car-goat constellations:" \
             "a) Door 1: goat (first choice); door 2: goat; door 3: car." \
             "b) Door 1: goat (first choice); door 2: car; door 3: goat." \
             "c) Door 1: car (first choice); door 2: goat; door 3: goat." \
             "Now think about in which constellation the quizmaster could open which door. "\
             "Then decide whether the candidate should stay in the respective constellation with his first choice or switch to the last remaining door." \
             "In how many of these three constellations should the candidate switch from his first choice to the remaining unopened door?"\
             "In ________ of 3 constellations." \
             "What should the candidate therefore do? Stay or switch?"

# Linda problem
# Classic version
linda_classic = "Linda is 31 years old, single, very intelligent, and speaks her mind openly. She studied philosophy. "\
                "During her studies, she dealt extensively with questions of equality and social justice and participated in anti-nuclear demonstrations." \
                "Now order the following statements about Linda according to how likely they are. Which statement is more likely?" \
                "a)	Linda is a bank clerk." \
                "b)	Linda is active in the feminist movement." \
                "c)	Linda is a bank clerk and is active in the feminist movement."

# Birth order
# Unordered
births_rand = "All families with six children in a city were surveyed. In seventy-two families, the exact order of births of boys (B) and girls (G) was GBGBBG."\
              "What is your estimate of the number of families surveyed in which the exact order of births was BGBBBB?"

# Ordered
births_ord = "All families with six children in a city were surveyed. In seventy-two families, the exact order of births of boys (B) and girls (G) was GBGBBG."\
             "What is your estimate of the number of families surveyed in which the exact order of births was BBBGGG?"

# High school programs
high_school = "There are two programs in a high school. Boys are a majority (65%) in program A, and a minority (45%) in program B. There is an equal number of classes in each of the two programs." \
              "You enter a class at random, and observe that 55% of the students are boys. What is your best guess – does the class belong to program A or to program B?"

# Marbles game
marbles = "On each round of a game, 20 marbles are distributed at random among five children: Alan, Ben, Carl, Dan, and Ed. Consider the following distributions:" \
          "Type I: Alan: 4; Ben: 4; Carl: 5; Dan: 4; Ed: 3." \
          "Type II: Alan: 4; Ben: 4; Carl: 4; Dan: 4; Ed: 4." \
          "In many rounds of the game, will there be more results of type I or of type II?"

prompts = [wason_classic, wason_context, aids_classic, aids_freq, hospital, monty_short, monty_long,
           linda_classic, births_rand, births_ord, high_school, psych_exp, marbles]
