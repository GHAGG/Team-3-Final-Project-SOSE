import os

os.system('clear')
from models.add import *
from models.answer import *
from models.question import *
from models.sql import *
from init_db import *

s = init_db_session('question.sqlite')


print("%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("%%%%%% S U R V E Y %%%%%%%%")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%")


while True:
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print('''What would you like to do? (Type exit to quit):
            (1) Create a Poll
            (2) Launch a Poll
            (3) View the Answers of a Poll''')
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    choice = input("Enter the Number Corresponding to your choice: ")
    try:
        int(choice)
    except:
        if choice.lower()=="exit":
            break
        else:
            print("Please enter a valid numerical answer")
            continue
    else:
        if int(choice)==1:
            question_options= input("Are you ready to create a Poll? (response: Y/N) ")
            if question_options.capitalize()=="Y":
                question= input("What is your question?  ")
                last_char = question[-1]
                if last_char != "?":
                    question = question + "?"
                value= Question1(rt=question)
                s.add(value)
                s.commit()



                poll= Poll(question)
                yesnotype = str(input("Is this a Yes or No question? (responses: Y/N) ")).capitalize()
                yesnotype = YesNo(istype=yesnotype)
                if yesnotype.istype == "Y":
                    QA = YesNoAnswers()



                    potentialanswer = PotentialAnswer(name= 'Y', name1 = 'N')
                    s.add(potentialanswer)
                    s.commit()


                elif yesnotype.istype == "N":
                    tries = True
                    tres = 0
                    while tries == True:
                        try:
                            intnumber = int(input("How many answers? (int) "))
                        except:
                            if tres < 2:
                                print("Invalid input. Please enter an integer")
                                tres += 1
                                continue
                            elif tres == 2:
                                print("To many invalid inputs. Question has not been created")
                                break
                        else:
                            tries = False

                            if intnumber == 1:
                              multiplechoice = MultipleChoice(answernumber=intnumber)
                              multiplechoice.askanswer()
                              potentialanswer = PotentialAnswer(name= multiplechoice.allanswers[0])
                              s.add(potentialanswer)
                              s.commit()
                            elif intnumber == 2:
                              multiplechoice = MultipleChoice(answernumber=intnumber)
                              multiplechoice.askanswer()
                              potentialanswer = PotentialAnswer(name= multiplechoice.allanswers[0], name1= multiplechoice.allanswers[1])
                              s.add(potentialanswer)
                              s.commit()
                            elif intnumber == 3:
                              multiplechoice = MultipleChoice(answernumber=intnumber)
                              multiplechoice.askanswer()
                              potentialanswer = PotentialAnswer(name= multiplechoice.allanswers[0], name1= multiplechoice.allanswers[1], name2= multiplechoice.allanswers[2])
                              s.add(potentialanswer)
                              s.commit()
                            elif intnumber == 4:
                              multiplechoice = MultipleChoice(answernumber=intnumber)
                              multiplechoice.askanswer()
                              potentialanswer = PotentialAnswer(name= multiplechoice.allanswers[0], name1= multiplechoice.allanswers[1], name2= multiplechoice.allanswers[2],name3= multiplechoice.allanswers[3])
                              s.add(potentialanswer)
                              s.commit()
                            else:
                              print("You entered too many questions")
                            print("Your question has been created!")

        elif int(choice)==2:
            pollfail = 0
            polllaunch = True
            launchpoll = input("Are you ready to launch a poll? (Y/N) ")
            launchpoll = str(launchpoll).capitalize()

            while True and pollfail<=3:
                try:
                    len(launchpoll) == 1
                except:
                    print("Invalid input, please respond with Y or N")
                    pollfail += 1
                    if pollfail >3:
                        print("Sorry too many failed attempts!")
                        polllaunch==False
                        break
                else:
                    if launchpoll == "Y":
                        print("The following polls are available to launch")
                        a = s.query(Question1).all()
                        for i in a:
                          print(i.id, i.rt)

                        whichpoll = int(input("Select the ID of the poll you would like to launch: (int) "))
                        q_id = whichpoll - 1
                        if (s.query(PotentialAnswer)[q_id].name == "Y") and (s.query(PotentialAnswer)[q_id].name1 == "N") and (s.query(PotentialAnswer)[q_id].name2 == None):
                            print("Answer the following question?")
                            print(s.query(Question1)[q_id].rt, "?")
                            # q_id = s.query(PotentialAnswer)[whichpoll].id
                            dicti = {1: s.query(PotentialAnswer)[q_id].name,
                                     2: s.query(PotentialAnswer)[q_id].name1}
                            print(dicti)
                            whichchoice = int(input(("Select the number corresponding to your answer (int) ")))
                            print(whichchoice)
                            print("You have selected " + dicti[whichchoice])
                            if whichchoice == 1:
                                actualanswer = ActualAnswer(qid=whichpoll, answer=1, answer1=0, answer2=0, answer3=0)
                                s.add(actualanswer)
                                s.commit()
                            elif whichchoice == 2:
                                actualanswer = ActualAnswer(qid=whichpoll, answer=0, answer1=1, answer2=0, answer3=0)
                                s.add(actualanswer)
                                s.commit()
                            else:
                                print("Please enter '1' or '2' as your response")

                        else:
                            print("Answer the following question?")
                            print(q_id)
                            print(s.query(Question1)[q_id].rt, "?")
                            #q_id = s.query(PotentialAnswer)[whichpoll].id
                            dicti = {1 : s.query(PotentialAnswer)[q_id].name,
                                     2 : s.query(PotentialAnswer)[q_id].name1,
                                     3 : s.query(PotentialAnswer)[q_id].name2,
                                     4 : s.query(PotentialAnswer)[q_id].name3}
                            print(dicti)
                            whichchoice = int(input(("Select the number corresponding to your answer (int) ")))
                            print(whichchoice)
                            print("You have selected " + dicti[whichchoice])
                            #### THIS PART DOES NOT WORK
                            if whichchoice == 1:
                                actualanswer = ActualAnswer(qid=whichpoll, answer=1, answer1=0, answer2=0, answer3=0)
                                s.add(actualanswer)
                                s.commit()
                            elif whichchoice == 2:
                                actualanswer = ActualAnswer(qid=whichpoll, answer=0, answer1=1, answer2=0, answer3=0)
                                s.add(actualanswer)
                                s.commit()
                            elif whichchoice == 3:
                                actualanswer = ActualAnswer(qid=whichpoll, answer=0, answer1=0, answer2=1, answer3=0)
                                s.add(actualanswer)
                                s.commit()
                            elif whichchoice == 4:
                                actualanswer = ActualAnswer(qid=whichpoll, answer=0, answer1=0, answer2=0, answer3=1)
                                s.add(actualanswer)
                                s.commit()
                            else:
                                print("This answer is invalid.")

                            polllaunch == True

                        break

        elif int(choice)==3:
            sum0 = 0
            sum1 = 0
            sum2 = 0
            sum3 = 0
            while True:
                seeresults = str(input("Would you like to see the results of your poll? (Y/N) ")).capitalize()
                if seeresults == "Y":
                    print("Results are available for the following polls: ")
                    a = s.query(Question1).all()
                    for i in a:
                        print(i.id, i.rt)
                    whichresults = int(
                        input("Which poll results would you like to see today? Enter the corresponding ID (int) "))

                    for i in range(0, len(s.query(ActualAnswer).all())):
                        if s.query(ActualAnswer)[i].qid == whichresults:
                            sum0 = sum0 + s.query(ActualAnswer)[i].answer
                            sum1 = sum1 + s.query(ActualAnswer)[i].answer1
                            sum2 = sum2 + s.query(ActualAnswer)[i].answer2
                            sum3 = sum3 + s.query(ActualAnswer)[i].answer3
                        else:
                            pass

                    sumall = sum0 + sum1 + sum2 + sum3
                    if sumall == 0:
                        print("There are no responses for this poll.")
                        break
                    perc0 = round((sum0 / sumall) * 100, 2)
                    perc0 = str(perc0) + "%"
                    perc1 = round((sum1 / sumall) * 100, 2)
                    perc1 = str(perc1) + "%"
                    perc2 = round((sum2 / sumall) * 100, 2)
                    perc2 = str(perc2) + "%"
                    perc3 = round((sum3 / sumall) * 100, 2)
                    perc3 = str(perc3) + "%"

                    if (s.query(PotentialAnswer)[whichresults - 1].name2 == None):
                        dicti = {s.query(PotentialAnswer)[whichresults - 1].name: perc0,
                                 s.query(PotentialAnswer)[whichresults - 1].name1: perc1}
                        print(dicti)

                    elif (s.query(PotentialAnswer)[whichresults - 1].name3 == None):
                        dicti = {s.query(PotentialAnswer)[whichresults - 1].name: perc0,
                                 s.query(PotentialAnswer)[whichresults - 1].name1: perc1,
                                 s.query(PotentialAnswer)[whichresults - 1].name2: perc2}
                        print(dicti)

                    else:
                        dicti = {s.query(PotentialAnswer)[whichresults - 1].name: perc0,
                                 s.query(PotentialAnswer)[whichresults - 1].name1: perc1,
                                 s.query(PotentialAnswer)[whichresults - 1].name2: perc2,
                                 s.query(PotentialAnswer)[whichresults - 1].name3: perc3}
                        print(dicti)

                    # results = s.query(ActualAnswer).get(whichresults)
                    # print(results)
                    # sum = s.query(ActualAnswer).answer()
                    # sum1 = s.query(ActualAnswer).answer1()
                    # sum2 = s.query(ActualAnswer).answer2()
                    # sum3 = s.query(ActualAnswer).answer3()
                    # print(sum, sum1, sum2, sum3)

                    break
                elif seeresults == "N":
                    print("Ok! have a nice day")
                    break
                else:
                    print("Please enter 'Y' or 'N' as a response")
                    continue

        elif choice.lower()== "exit":
            break
        else:
            print("Enter a valid number")



